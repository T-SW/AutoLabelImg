import os
import numpy as np
import cv2
from tqdm import tqdm


def main(imgfol_path, labfol_path, conf, check_ls):
    labfol_ls = os.listdir(labfol_path)
    labfol_ls.remove("classes.txt")
    labfol_ls = tqdm(labfol_ls)
    check_file_ls = list()
    for file in labfol_ls:
        lab_path = os.path.join(labfol_path, file)
        prefix = os.path.splitext(file)[0]
        img_path = os.path.join(imgfol_path, f'{prefix}.jpg')

        with open(lab_path, 'r') as txt:
            lab = txt.readlines()
            lab_ls = list()
            for i in lab:
                sub_list = i.split()
                if check_ls:
                    if sub_list[0] in check_ls:
                        lab_ls.append(sub_list)
                else:
                    lab_ls.append(sub_list)

            bool = calculate_iou_for_grouped_labels(lab_ls, img_path, conf)
            if bool:
                check_file_ls.append(img_path)

    labfol_ls.close()
    return check_file_ls


def xywh2xyxy(box, img_path):
        x, y, w, h = box
        img = cv2.imread(img_path)
        height, wide = img.shape[:2]
        xmin = int(wide * (float(x) - (float(w) / 2)))
        ymin = int(height * (float(y) - (float(h) / 2)))
        xmax = int(wide * (float(x) + (float(w) / 2)))
        ymax = int(height * (float(y) + (float(h) / 2)))

        return [xmin, ymin, xmax, ymax]


def compute_iou(box1, box2, wh=False):
        """
        compute the iou of two boxes.
        Args:
                box1, box2: [xmin, ymin, xmax, ymax] (wh=False) or [xcenter, ycenter, w, h] (wh=True)
                wh: the format of coordinate.
        Return:
                iou: iou of box1 and box2.
        """
        if wh:
                xmin1, ymin1, xmax1, ymax1 = box1
                xmin2, ymin2, xmax2, ymax2 = box2
        else:
                xmin1, ymin1 = int(box1[0] - box1[2] / 2.0), int(box1[1] - box1[3] / 2.0)
                xmax1, ymax1 = int(box1[0] + box1[2] / 2.0), int(box1[1] + box1[3] / 2.0)
                xmin2, ymin2 = int(box2[0] - box2[2] / 2.0), int(box2[1] - box2[3] / 2.0)
                xmax2, ymax2 = int(box2[0] + box2[2] / 2.0), int(box2[1] + box2[3] / 2.0)

        # 获取矩形框交集对应的左上角和右下角的坐标（intersection）
        xx1 = np.max([xmin1, xmin2])
        yy1 = np.max([ymin1, ymin2])
        xx2 = np.min([xmax1, xmax2])
        yy2 = np.min([ymax1, ymax2])

        # 计算两个矩形框面积
        area1 = (xmax1 - xmin1) * (ymax1 - ymin1)
        area2 = (xmax2 - xmin2) * (ymax2 - ymin2)

        inter_area = (np.max([0, xx2 - xx1])) * (np.max([0, yy2 - yy1]))  # 计算交集面积
        iou = inter_area / (area1 + area2 - inter_area + 1e-6)   # 计算交并比

        return iou


def calculate_iou_for_grouped_labels(labels, img_path, conf):
    # iou_values = []
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            if labels[i][0] == labels[j][0]:
                box_i, box_j = xywh2xyxy(labels[i][1:], img_path), xywh2xyxy(labels[j][1:], img_path)
                iou = compute_iou(box_i, box_j)
                # iou_values.append(iou)
                if iou >= conf:
                    return True


if __name__ == '__main__':
    imgfol_path = r"F:\data\labelimages\23.8.2\output_folder_20\images"
    labfol_path = r"F:\data\labelimages\23.8.2\output_folder_20\lables"
    conf = 0.9
    check_ls = ['2']
    file_ls = main(imgfol_path, labfol_path, conf, check_ls)
    print(file_ls)
