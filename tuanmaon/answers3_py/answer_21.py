import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# histogram normalization
def hist_normalization(img, a=0, b=255):
	# get max and min
	c = img.min()
	d = img.max()

	out = img.copy()

	# normalization
	out = (b-a) / (d - c) * (out - c) + a
	out[out < a] = a
	out[out > b] = b
	out = out.astype(np.uint8)
	
	return out


# Read image

image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read).astype(np.float)
H, W, C = img.shape

# histogram normalization
out = hist_normalization(img)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))


i=1
strfolder="../answers_out/"+str_write+"_answer_21_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_21_out1_"+str(i)+".jpg"              #需更改answer_12_out


j=1
strfolder="../answers_out/"+str_write+"_answer_21_out2_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    j=j+1

str2="../answers_out/"+str_write+"_answer_21_out2_"+str(j)+".jpg"              #需更改answer_12_out



plt.savefig(str1)
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str2, out)
