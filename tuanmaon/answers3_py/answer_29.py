import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Affine
def affine(img, a, b, c, d, tx, ty):
    H, W, C = img.shape
    tem = img.copy()
    # temporary image
    img = np.zeros((H+2, W+2, C), dtype=np.float32)
    img[1:H+1, 1:W+1] = tem
    
    # get new image shape
    H_new = np.round(H * d).astype(np.int)
    W_new = np.round(W * a).astype(np.int)
    out = np.zeros((H_new+1, W_new+1, C), dtype=np.float32)
    
    # get position of new image
    x_new = np.tile(np.arange(W_new), (H_new, 1))
    y_new = np.arange(H_new).repeat(W_new).reshape(H_new, -1)
    
    # get position of original image by affine
    adbc = a * d - b * c
    x = np.round((d * x_new  - b * y_new) / adbc).astype(np.int) - tx + 1
    y = np.round((-c * x_new + a * y_new) / adbc).astype(np.int) - ty + 1
    
    x = np.minimum(np.maximum(x, 0), W+1).astype(np.int)
    y = np.minimum(np.maximum(y, 0), H+1).astype(np.int)
    
    # assgin pixcel to new image
    out[y_new, x_new] = img[y, x]
    
    out = out[:H_new, :W_new]
    out = out.astype(np.uint8)
    
    return out


# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float32)

# Affine
out = affine(img, a=1.3, b=0, c=0, d=0.8, tx=30, ty=-30)


# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_29_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_29_out1_"+str(i)+".jpg"              #需更改answer_12_out


cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
