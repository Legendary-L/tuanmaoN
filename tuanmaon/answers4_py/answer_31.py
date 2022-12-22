import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Affine
def affine(img, dx=30, dy=30):
    # get shape
    H, W, C = img.shape

    # Affine hyper parameters
    a = 1.
    b = dx / H
    c = dy / W
    d = 1.
    tx = 0.
    ty = 0.

    # prepare temporary
    _img = np.zeros((H+2, W+2, C), dtype=np.float32)

    # insert image to center of temporary
    _img[1:H+1, 1:W+1] = img

    # prepare affine image temporary
    H_new = np.ceil(dy + H).astype(np.int)
    W_new = np.ceil(dx + W).astype(np.int)
    out = np.zeros((H_new, W_new, C), dtype=np.float32)

    # preprare assigned index
    x_new = np.tile(np.arange(W_new), (H_new, 1))
    y_new = np.arange(H_new).repeat(W_new).reshape(H_new, -1)

    # prepare inverse matrix for affine
    adbc = a * d - b * c
    x = np.round((d * x_new  - b * y_new) / adbc).astype(np.int) - tx + 1
    y = np.round((-c * x_new + a * y_new) / adbc).astype(np.int) - ty + 1

    x = np.minimum(np.maximum(x, 0), W+1).astype(np.int)
    y = np.minimum(np.maximum(y, 0), H+1).astype(np.int)

    # assign value from original to affine image
    out[y_new, x_new] = _img[y, x]
    out = out.astype(np.uint8)

    return out


# Read image


image_source_file_name_list = glob.glob('../answers4_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]



img = cv2.imread(str_read).astype(np.float32)

# Affine
out = affine(img, dx=30, dy=30)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_31_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_31_out1_"+str(i)+".jpg"              #需更改answer_12_out



cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
