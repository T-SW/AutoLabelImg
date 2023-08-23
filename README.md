# AutoLabelImg
[labelImg](https://github.com/HumanSignal/labelImg)，内置基于 [YOLOv8](https://github.com/ultralytics/ultralytics) 的自动检测功能。<br/>
目前为英文版，无汉化。<br/>

Built-in labelImg with YOLOv8 based automatic detection function.<br/>
Currently in English version, without localization.

## 新增项

![F783A5E4-6AFE-4878-9E98-46BB6C1BF9FB](https://github.com/T-SW/AutoLabelImg/assets/69509115/b01c455e-546d-4991-b085-2d2af3976786)

### 1.功能：
对应快捷键如下所示。

Auto Label：自动标注当前显示的图片

Auto Label All：<br/>
&emsp;(1).Current image and after：自动标注当前及之后的图片<br/>
&emsp;(2).All images：自动标注全部图片<br/>
&emsp;(3).Index range of images：自动标注指定序号(包含)间的图片<br/>

load_data：自动载入上次标注记录点

### 2.菜单：

(1).parameter_settings：含conf、iou、classes参数更改<br/><br/>
(2).model_selection：支持yolov8n、yolov8s、yolov8m、yolov8l、yolov8x

### 3.修改clasee类别序号（coco --> 当前任务）
检测coco类别标签后，自动按设定修改类别序号。<br/>
路径:"./tools/change_labels.py"<br/><br/>
(1).def rework_classes(labelpath, default)<br/>
    default=True:启用修改<br/>
    default=False:禁用修改(保持coco类别)<br/><br/>
(2).def replace(line)<br/>
    按任务及使用情况自行灵活修改，默认2,5,7 --> 2。

## Installation
#### Windows + Anaconda
个人配置：NVIDIA GTX 1650 + cuda11.7

1.创建虚拟环境<br/>
```pythonscript
conda create -n yourvenv python=3.8
```
注：python3.10以上易崩，labelimg标框所用库数据格式不兼容等原因。<br/>

2.安装 pyqt5 + lxml<br/>
```pythonscript
pip install pyqt5
conda install -c anaconda lxml
```

3.安装 [torch](https://pytorch.org/)<br/><br/>

4.安装其余依赖库<br/>
```pythonscript
cd "your dir path"
pip install -r requirements.txt
```
<br/>

5.运行<br/>
```pythonscript
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
```
<br/>

6.根目录创建models文件夹，从[YOLOv8](https://github.com/ultralytics/ultralytics)中下载pt权重文件并放至文件夹内。

## Hotkeys

快捷键     | 功能
-------- | -----
Ctrl + u  | 从文件夹路径加载图片
Ctrl + r  | 设置保存路径
Ctrl + s  | 保存
Ctrl + d  | 复制矩形框
Ctrl + Shift + d  | 删除当前图像
w  | 创建一个矩形框
d  | 下一张图像
a  | 上一张图像
del  | 删除所选矩形框
↑→↓←  | 移动选定矩形框

新增快捷键     | 对应项
-------- | -----
Ctrl + p  | Auto Label
Ctrl + m  | Auto Label All
F5  | load_data


## 程序崩溃原因

1."./data/predefined_classes.txt"与classes.txt不一致。<br/>
2.载入崩溃：删除C:\Users\用户名路径下的.labelImgSettings.pkl文件。

<br/>

## Contact information

*WeChat*：SW_7396        <br/>
*Email 163*：personalmailboxbyT@163.com



