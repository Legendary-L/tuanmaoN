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

# Otsu Binarization
def otsu_binarization(img, th=128):
	max_sigma = 0
	max_t = 0

	# determine threshold
	for _t in range(1, 255):
		v0 = out[np.where(out < _t)]
		m0 = np.mean(v0) if len(v0) > 0 else 0.
		w0 = len(v0) / (H * W)
		v1 = out[np.where(out >= _t)]
		m1 = np.mean(v1) if len(v1) > 0 else 0.
		w1 = len(v1) / (H * W)
		sigma = w0 * w1 * ((m0 - m1) ** 2)
		if sigma > max_sigma:
			max_sigma = sigma
			max_t = _t

	# Binarization
	print("threshold >>", max_t)
	th = max_t
	out[out < th] = 0
	out[out >= th] = 255

	return out


# Read image

image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read).astype(np.float32)
H, W, C =img.shape


# Grayscale
out = BGR2GRAY(img)

# Otsu's binarization
out = otsu_binarization(out)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_4_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_4_out1_"+str(i)+".jpg"              #需更改answer_12_out


cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
