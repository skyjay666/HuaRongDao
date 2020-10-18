from similarity import *


def Judge(arr, record,position,target):
    for i in range(0, 10):
        record.append(0)
    for i in range(1, 10):
        image1 = 'cutmodify/' + str(i) + '.jpg'
        flag = 0  # 是否匹配到图（找白色图片）
        for j in range(1, 10):
            image2 = 'cutorigin/' + str(j) + '.jpg'
            calc_sim = runAllImageSimilaryFun(image1, image2)  # 计算相似度
            if calc_sim == 1:
                flag = 1
                arr.append(j)
                record[j-1] = 1
                break
        if flag == 0:
            arr.append(0)
    # 目标状态
    target = []
    for i in range(9):
        if (record[i] != 0):
            target.append(i + 1)
        else:
            target.append(0)
    return arr, record, position, target
