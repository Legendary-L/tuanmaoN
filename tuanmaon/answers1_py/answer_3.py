import cv2
import numpy as np
import glob

# Gray scale


def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    return out

# binalization


def binarization(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255
    return img


# Read image

image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float32)

# Grayscale
out = BGR2GRAY(img)

# Binarization
out = binarization(out)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_3_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_3_out1_"+str(i)+".jpg"              #需更改answer_12_out


cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
