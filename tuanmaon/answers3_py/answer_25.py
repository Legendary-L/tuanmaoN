import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Nereset Neighbor interpolation
def nn_interpolate(img, ax=1, ay=1):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	y = np.arange(aH).repeat(aW).reshape(aW, -1)
	x = np.tile(np.arange(aW), (aH, 1))
	y = np.round(y / ay).astype(np.int)
	x = np.round(x / ax).astype(np.int)

	out = img[y,x]

	out = out.astype(np.uint8)

	return out


# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float)

# Nearest Neighbor
out = nn_interpolate(img, ax=1.5, ay=1.5)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_25_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_25_out1_"+str(i)+".jpg"              #需更改answer_12_out



cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
