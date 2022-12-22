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

# max-min filter


def max_min_filter(img, K_size=3):
    H, W = img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.max(tmp[y: y + K_size, x: x + K_size]) - \
                np.min(tmp[y: y + K_size, x: x + K_size])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# Read image

image_source_file_name_list = glob.glob('../answers2_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]

img = cv2.imread(str_read).astype(np.float)

# grayscale
gray = BGR2GRAY(img)

# Max-Min filtering
out = max_min_filter(gray, K_size=3)

i=1
strfolder="../answers_out/"+str_write+"_answer_13_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out 
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_13_out1_"+str(i)+".jpg"              #需更改answer_12_out



# Save result
cv2.imwrite(str, out)                   #需更改
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
