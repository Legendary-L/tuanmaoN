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

# LoG filter
def LoG_filter(img, K_size=5, sigma=3):
	H, W = img.shape

	# zero padding
	pad = K_size // 2
	out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
	tmp = out.copy()

	# LoG Kernel
	K = np.zeros((K_size, K_size), dtype=np.float)
	for x in range(-pad, -pad + K_size):
		for y in range(-pad, -pad + K_size):
			K[y + pad, x + pad] = (x ** 2 + y ** 2 - sigma ** 2) * np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
	K /= (2 * np.pi * (sigma ** 6))
	K /= K.sum()

	# filtering
	for y in range(H):
		for x in range(W):
			out[pad + y, pad + x] = np.sum(K * tmp[y: y + K_size, x: x + K_size])

	out = np.clip(out, 0, 255)
	out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out


# Read image
image_source_file_name_list = glob.glob('../answers2_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]



img = cv2.imread(str_read)

# grayscale
gray = BGR2GRAY(img)

# LoG filtering
out = LoG_filter(gray, K_size=5, sigma=3)

# Save result



i=1
all_file_name_list = glob.glob('../answers_out/answer_19_out1_*.jpg')        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1
#str="../answers_out/answer_12_out"+str(i)+".jpg"
str1="../answers_out/"+str_write+"_answer_19_out1_"+str(i)+".jpg"              #需更改answer_12_out




cv2.imwrite(str1, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
