import cv2
import numpy as np
import glob

# Gaussian filter
def gaussian_filter(img, K_size=3, sigma=1.3):
	if len(img.shape) == 3:
		H, W, C = img.shape
	else:
		img = np.expand_dims(img, axis=-1)
		H, W, C = img.shape

		
	## Zero padding
	pad = K_size // 2
	out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
	out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

	## prepare Kernel
	K = np.zeros((K_size, K_size), dtype=np.float)
	for x in range(-pad, -pad + K_size):
		for y in range(-pad, -pad + K_size):
			K[y + pad, x + pad] = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
	K /= (2 * np.pi * sigma * sigma)
	K /= K.sum()

	tmp = out.copy()

	# filtering
	for y in range(H):
		for x in range(W):
			for c in range(C):
				out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

	out = np.clip(out, 0, 255)
	out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out


# Read image

image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read)


# Gaussian Filter
out = gaussian_filter(img, K_size=3, sigma=1.3)


# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_9_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_9_out1_"+str(i)+".jpg"              #需更改answer_12_out




cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
