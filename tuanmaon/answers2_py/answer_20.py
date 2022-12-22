import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Read image
image_source_file_name_list = glob.glob('../answers2_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read).astype(np.float)

# Display histogram
plt.hist(img.ravel(), bins=255, rwidth=0.8, range=(0, 255))



i=1
strfolder="../answers_out/"+str_write+"_answer_20_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_20_out1_"+str(i)+".jpg"              #需更改answer_12_out



plt.savefig(str)
plt.show()
