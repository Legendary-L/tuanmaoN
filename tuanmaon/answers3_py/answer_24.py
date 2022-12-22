import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# gamma correction
def gamma_correction(img, c=1, g=2.2):
	out = img.copy()
	out /= 255.
	out = (1/c * out) ** (1/g)

	out *= 255
	out = out.astype(np.uint8)

	return out


# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float)

# Gammma correction
out = gamma_correction(img)

# Save result



i=1
strfolder="../answers_out/"+str_write+"_answer_24_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_24_out1_"+str(i)+".jpg"              #需更改answer_12_out




cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
