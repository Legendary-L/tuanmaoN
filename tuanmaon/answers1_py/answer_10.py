import cv2
import numpy as np
import glob

# Median filter
def median_filter(img, K_size=3):
    H, W, C = img.shape

    ## Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
    out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])

    out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

    return out


# Read image
image_source_file_name_list = glob.glob('../answers1_py/*.jpg')   #需更改answers2
for file_name in image_source_file_name_list:
    str_read=file_name[15:]                                        #answers10需更改为16
str_write=str_read[:-4]


img = cv2.imread(str_read)


# Median Filter
out = median_filter(img, K_size=3)


# Save result


i=1
strfolder="../answers_out/"+str_write+"_answer_10_out1_*.jpg"
all_file_name_list = glob.glob(strfolder)        #需更改answer_12_out
for file_name in all_file_name_list:
    i=i+1

str="../answers_out/"+str_write+"_answer_10_out1_"+str(i)+".jpg"              #需更改answer_12_out




cv2.imwrite(str, out)
cv2.imshow("result", out)
cv2.waitKey(100)
cv2.destroyAllWindows()
