import os
import cv2
import matplotlib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

matplotlib.use('TkAgg')


def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                     (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def runAllImageSimilaryFun(para1, para2):
    # 通过imread方法直接读取物理路径
    img1 = cv2.imread(para1)
    img2 = cv2.imread(para2)

    sim = calculate(img1, img2)
    return sim


def general(test, dest):
    mmax = 0
    for path, d, filelist in dest:
        for filename in filelist:
            if filename.endswith('jpg'):
                if (float(runAllImageSimilaryFun(test, (os.path.join(path, filename)))) > mmax):
                    mmax = float(runAllImageSimilaryFun(test, (os.path.join(path, filename))))
                    mname = filename
    return mmax, mname
