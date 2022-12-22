import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# histogram equalization
def hist_equal(img, z_max=255):
	H, W, C = img.shape
	S = H * W * C * 1.

	out = img.copy()

	sum_h = 0.

	for i in range(1, 255):
		ind = np.where(img == i)
		sum_h += len(img[ind])
		z_prime = z_max / S * sum_h
		out[ind] = z_prime

	out = out.astype(np.uint8)

	return out


# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float)

# histogram normalization
out = hist_equal(img)

# Display histogram




i=1
strfolder="../answers_out/"+str_write+"_answer_23_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_23_out1_"+str(i)+".jpg"              #需更改answer_12_out


j=1
strfolder="../answers_out/"+str_write+"_answer_23_out2_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    j=j+1

str2="../answers_out/"+str_write+"_answer_23_out2_"+str(j)+".jpg"              #需更改answer_12_out




plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig(str1)
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str2, out)
