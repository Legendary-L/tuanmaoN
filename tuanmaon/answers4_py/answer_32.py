import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# DFT hyper-parameters
K, L = 128, 128
channel = 3


# DFT
def dft(img):
	H, W, _ = img.shape

	# Prepare DFT coefficient
	G = np.zeros((L, K, channel), dtype=np.complex)

	# prepare processed index corresponding to original image positions
	x = np.tile(np.arange(W), (H, 1))
	y = np.arange(H).repeat(W).reshape(H, -1)

	# dft
	for c in range(channel):
		for l in range(L):
			for k in range(K):
				G[l, k, c] = np.sum(img[..., c] * np.exp(-2j * np.pi * (x * k / K + y * l / L))) / np.sqrt(K * L)
				#for n in range(N):
				#    for m in range(M):
				#        v += gray[n, m] * np.exp(-2j * np.pi * (m * k / M + n * l / N))
				#G[l, k] = v / np.sqrt(M * N)

	return G

# IDFT
def idft(G):
	# prepare out image
	H, W, _ = G.shape
	out = np.zeros((H, W, channel), dtype=np.float32)

	# prepare processed index corresponding to original image positions
	x = np.tile(np.arange(W), (H, 1))
	y = np.arange(H).repeat(W).reshape(H, -1)

	# idft
	for c in range(channel):
		for l in range(H):
			for k in range(W):
				out[l, k, c] = np.abs(np.sum(G[..., c] * np.exp(2j * np.pi * (x * k / W + y * l / H)))) / np.sqrt(W * H)

	# clipping
	out = np.clip(out, 0, 255)
	out = out.astype(np.uint8)

	return out



# Read image


image_source_file_name_list = glob.glob('../answers4_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read).astype(np.float32)

# DFT
G = dft(img)

# write poser spectal to image
ps = (np.abs(G) / np.abs(G).max() * 255).astype(np.uint8)




i=1
strfolder="../answers_out/"+str_write+"_answer_32_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_32_out1_"+str(i)+".jpg"              #需更改answer_12_out


j=1
strfolder="../answers_out/"+str_write+"_answer_32_out2_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    j=j+1

str2="../answers_out/"+str_write+"_answer_32_out2_"+str(j)+".jpg"              #需更改answer_12_out






cv2.imwrite(str1, ps)

# IDFT
out = idft(G)

# Save result
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str2, out)



"""
fimg = np.fft.fft2(gray)
    
# 第1象限と第3象限, 第2象限と第4象限を入れ替え
fimg =  np.fft.fftshift(fimg)
print(fimg.shape)
# パワースペクトルの計算
mag = 20*np.log(np.abs(fimg))
    
# 入力画像とスペクトル画像をグラフ描画
plt.subplot(121)
plt.imshow(gray, cmap = 'gray')
plt.subplot(122)
plt.imshow(mag, cmap = 'gray')
plt.show()
"""