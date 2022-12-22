import cv2
import numpy as np
import glob
# function: BGR -> RGB


def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # RGB > BGR
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img


# Read image
image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read)

# BGR -> RGB
img = BGR2RGB(img)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_1_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_1_out1_"+str(i)+".jpg"              #需更改answer_12_out


cv2.imwrite(str, img)
cv2.imshow("result", img)
cv2.waitKey(100)
cv2.destroyAllWindows()
