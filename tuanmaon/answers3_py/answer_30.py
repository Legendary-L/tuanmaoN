import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# affine
def affine(img, a, b, c, d, tx, ty):
    H, W, C = img.shape
    tem = img.copy()
    # temporary image
    img = np.zeros((H+2, W+2, C), dtype=np.float32)
    img[1:H+1, 1:W+1] = tem
    
    # get shape of new image
    H_new = np.round(H).astype(np.int)
    W_new = np.round(W).astype(np.int)
    out = np.zeros((H_new, W_new, C), dtype=np.float32)
    
    # get position of new image
    x_new = np.tile(np.arange(W_new), (H_new, 1))
    y_new = np.arange(H_new).repeat(W_new).reshape(H_new, -1)
    
    # get position of original image by affine
    adbc = a * d - b * c
    x = np.round((d * x_new  - b * y_new) / adbc).astype(np.int) - tx + 1
    y = np.round((-c * x_new + a * y_new) / adbc).astype(np.int) - ty + 1
    
    # adjust center by affine
    dcx = (x.max() + x.min()) // 2 - W // 2
    dcy = (y.max() + y.min()) // 2 - H // 2
    
    x -= dcx
    y -= dcy
    
    x = np.clip(x, 0, W + 1)
    y = np.clip(y, 0, H + 1)
    
    # assign pixcel
    out[y_new, x_new] = img[y, x]
    out = out.astype(np.uint8)
    
    return out

# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float32)


# Affine
A = 30.
theta = - np.pi * A / 180.

out = affine(img, a=np.cos(theta), b=-np.sin(theta), c=np.sin(theta), d=np.cos(theta),
 tx=0, ty=0)


# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_30_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_30_out1_"+str(i)+".jpg"              #需更改answer_12_out



cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
