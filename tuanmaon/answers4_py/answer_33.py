import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

# DFT hyper-parameters
K, L = 128, 128
channel = 3

# bgr -> gray
def bgr2gray(img):
	gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
	return gray


# DFT
def dft(img):
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


# LPF
def lpf(G, ratio=0.5):
	H, W, _ = G.shape	

	# transfer positions
	_G = np.zeros_like(G)
	_G[:H//2, :W//2] = G[H//2:, W//2:]
	_G[:H//2, W//2:] = G[H//2:, :W//2]
	_G[H//2:, :W//2] = G[:H//2, W//2:]
	_G[H//2:, W//2:] = G[:H//2, :W//2]

	# get distance from center (H / 2, W / 2)
	x = np.tile(np.arange(W), (H, 1))
	y = np.arange(H).repeat(W).reshape(H, -1)

	# make filter
	_x = x - W // 2
	_y = y - H // 2
	r = np.sqrt(_x ** 2 + _y ** 2)
	mask = np.ones((H, W), dtype=np.float32)
	mask[r > (W // 2 * ratio)] = 0

	mask = np.repeat(mask, channel).reshape(H, W, channel)

	# filtering
	_G *= mask

	# reverse original positions
	G[:H//2, :W//2] = _G[H//2:, W//2:]
	G[:H//2, W//2:] = _G[H//2:, :W//2]
	G[H//2:, :W//2] = _G[:H//2, W//2:]
	G[H//2:, W//2:] = _G[:H//2, :W//2]

	return G


# Read image




image_source_file_name_list = glob.glob('../answers4_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]




img = cv2.imread(str_read).astype(np.float32)
H, W, C = img.shape

# Gray scale
gray = bgr2gray(img)

# DFT
G = dft(img)

# LPF
G = lpf(G)

# IDFT
out = idft(G)

# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_33_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str1="../answers_out/"+str_write+"_answer_33_out1_"+str(i)+".jpg"              #需更改answer_12_out




cv2.imshow("result", out)
cv2.waitKey(100)
cv2.imwrite(str1, out)
