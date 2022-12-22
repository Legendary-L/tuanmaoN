import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# Bi-Linear interpolation
def bl_interpolate(img, ax=1., ay=1.):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	# get position of resized image
	y = np.arange(aH).repeat(aW).reshape(aW, -1)
	x = np.tile(np.arange(aW), (aH, 1))

	# get position of original position
	y = (y / ay)
	x = (x / ax)

	ix = np.floor(x).astype(np.int)
	iy = np.floor(y).astype(np.int)

	ix = np.minimum(ix, W-2)
	iy = np.minimum(iy, H-2)

	# get distance 
	dx = x - ix
	dy = y - iy

	dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)
	dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)

	# interpolation
	out = (1-dx) * (1-dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix+1] + (1 - dx) * dy * img[iy+1, ix] + dx * dy * img[iy+1, ix+1]

	out = np.clip(out, 0, 255)
	out = out.astype(np.uint8)

	return out


# Read image


image_source_file_name_list = glob.glob('../answers3_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float)

# Bilinear interpolation
out = bl_interpolate(img, ax=1.5, ay=1.5)

# Save result



i=1
strfolder="../answers_out/"+str_write+"_answer_26_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_26_out1_"+str(i)+".jpg"              #需更改answer_12_out



cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
