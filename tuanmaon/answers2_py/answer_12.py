import cv2
import numpy as np
import glob

# motion filter
def motion_filter(img, K_size=3):
    H, W, C = img.shape

    # Kernel
    K = np.diag( [1] * K_size ).astype(np.float)
    K /= K_size

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# Read image

image_source_file_name_list = glob.glob('../answers2_py/*.jpg')
for file_name in image_source_file_name_list:
    str_read=file_name[15:]
str_write=str_read[:-4]
#str_read="imori.jpg"
img = cv2.imread(str_read)
#img = cv2.imread("imori.jpg")

# motion filtering
out = motion_filter(img, K_size=3)

#str="../answers_2_out/answer_12_out.jpg"

i=1
strfolder="../answers_out/"+str_write+"_answer_12_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_12_out1_"+str(i)+".jpg"              #需更改answer_12_out



# Save result
cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
