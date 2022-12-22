tuanmaon: 一个数字图像的批处理系统

一、环境准备：
Linux全局环境下
pip install numpy
pip install matplotlib
将tuanmaon.tar.gz包解压

二、使用方式
2.1 到tuanmaon文件夹中
2.2 将需要处理的图片放到image_source文件夹中 （图片需是.jpg格式）
2.3 在tuanmaon文件夹下运行 [ ./result.sh 资源文件名 X X X X X X ]
2.4 得到的结果在answers_out文件夹内


2.5 例1：
将 imori_1.jpg imori_2.jpg 放到image_source中
....../tuanmaon$ ./result.sh imori_1.jpg 1 1 3 4 7
				 （让imori_1.jpg这张图片分别被 1、1、3、4、7功能处理 （图片可被重复处理，
																	 如这张图片被功能1处理了两次））

在answers_out文件内会产生
imori_1_answer_1_out1_1.jpg
imori_1_answer_1_out1_2.jpg
imori_1_answer_3_out1_1.jpg
imori_1_answer_4_out1_1.jpg
imori_1_answer_7_out1_1.jpg
这些文件
[imori_1]_[answer_1]_[out1]_[1]
[图片的文件名]_[被第几个功能处理]_[输出图1 (out2是输出图2)]_[第几幅图]

2.6 例2：全部批处理
./result.sh imori_1 1 2 3; ./result.sh ida.jpg 21 32 45; ./result.sh wan.jpg 50 1 2


2.7 注意：
需处理的图片的名字随意，但执行命令时图片的后缀.jpg必须带上。
建议每次使用前，将answers_out文件夹中的图片保存好后清空。

三、功能表

具体可见 https://mp.weixin.qq.com/s/f8JVwxQtXVRbHemIWhsnnQ

	1通道替换
    2灰度化（Grayscale）
    3二值化（Thresholding）
    4大津算法
    5HSV 变换
    6减色处理
    7平均池化（Average Pooling）
    8最大池化（Max Pooling）
    9高斯滤波（Gaussian Filter）
    10中值滤波（Median filter）

	11均值滤波
    12Motion Filter
    13MAX-MIN 滤波
    14微分滤波
    15Sobel 滤波
    16Prewitt 滤波
    17Laplacian 滤波
    18Emboss 滤波
    19LoG 滤波
    20直方图表示
	
	21直方图归一化（Histogram Normalization）
    22直方图操作
    23直方图均衡化（Histogram Equalization）
    24伽玛校正（Gamma Correction）
    25最邻近插值（Nearest-neighbor Interpolation）
    26双线性插值（Bilinear Interpolation）
    27双三次插值（Bicubic Interpolation）
    28仿射变换（Afine Transformations）——平行移动
    29仿射变换（Afine Transformations）——放大缩小
    30仿射变换（Afine Transformations）——旋转
	
	31仿射变换（Afine Transformations）——倾斜
    32傅立叶变换（Fourier Transform）
    33傅立叶变换——低通滤波
    34傅立叶变换——高通滤波
    35傅立叶变换——带通滤波
    36JPEG 压缩——第一步：离散余弦变换（Discrete Cosine Transformation）
    37峰值信噪比（Peak Signal to Noise Ratio）
    38JPEG 压缩——第二步：离散余弦变换+量化
    39JPEG 压缩——第三步：YCbCr 色彩空间
    40JPEG 压缩——第四步：YCbCr+DCT+量化
	
	41Canny边缘检测：第一步——边缘强度
    42Canny边缘检测：第二步——边缘细化
    43Canny边缘检测：第三步——滞后阈值
    44霍夫变换（Hough Transform）／直线检测——第一步：霍夫变换
    45霍夫变换（Hough Transform）／直线检测——第二步：NMS
    46霍夫变换（Hough Transform）／直线检测——第三步：霍夫逆变换
    47形态学处理：膨胀（Dilate）
    48形态学处理：腐蚀（Erode）
    49开运算（Opening Operation）
    50闭运算（Closing Operation）