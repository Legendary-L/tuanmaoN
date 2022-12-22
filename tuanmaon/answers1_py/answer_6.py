import cv2
import numpy as np
import glob

# Dicrease color
def dicrease_color(img):
	out = img.copy()

	out = out // 64 * 64 + 32

	return out


# Read image


image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]



img = cv2.imread(str_read)

# Dicrease color
out = dicrease_color(img)



i=1
strfolder="../answers_out/"+str_write+"_answer_6_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_6_out1_"+str(i)+".jpg"              #需更改answer_12_out



cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
