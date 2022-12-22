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


# sobel filter
def sobel_filter(img, K_size=3):
	if len(img.shape) == 3:
		H, W = img.shape
	else:
		img = np.expand_dims(img, axis=-1)
		H, W, C = img.shape

	# Zero padding
	pad = K_size // 2
	out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
	tmp = out.copy()

	out_v = out.copy()
	out_h = out.copy()

	## Sobel vertical
	Kv = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]
	## Sobel horizontal
	Kh = [[1., 0., -1.],[2., 0., -2.],[1., 0., -1.]]

	# filtering
	for y in range(H):
		for x in range(W):
			out_v[pad + y, pad + x] = np.sum(Kv * (tmp[y: y + K_size, x: x + K_size]))
			out_h[pad + y, pad + x] = np.sum(Kh * (tmp[y: y + K_size, x: x + K_size]))

	out_v = np.clip(out_v, 0, 255)
	out_h = np.clip(out_h, 0, 255)

	out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
	out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out_v, out_h

# Read image



image_source_file_name_list = glob.glob('../answers2_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float)

# grayscale
gray = BGR2GRAY(img)

# sobel filtering
out_v, out_h = sobel_filter(gray, K_size=3)

# Save result



i=1
all_file_name_list = glob.glob('../answers_out/answer_15_out1_*.jpg')        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1
#str="../answers_out/answer_12_out"+str(i)+".jpg"
str1="../answers_out/"+str_write+"_answer_15_out1_"+str(i)+".jpg"              #需更改answer_12_out


j=1
strfolder="../answers_out/"+str_write+"_answer_15_out2_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    j=j+1

str2="../answers_out/"+str_write+"_answer_15_out2_"+str(j)+".jpg"              #需更改answer_12_out




cv2.imwrite(str1, out_v)
cv2.imshow("result_v", out_v)
cv2.waitKey(100)
cv2.destroyWindow('result_v')

cv2.imwrite(str2, out_h)
cv2.imshow("result_h", out_h)
# loop if not get ESC or click x
cv2.waitKey(100)
cv2.destroyWindow('result_h')
cv2.destroyAllWindows()
