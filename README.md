# AutoLabelImg
[labelImg](https://github.com/HumanSignal/labelImg)，内置基于 [YOLOv8](https://github.com/ultralytics/ultralytics) 的自动检测功能。<br/>
目前为英文版，未汉化。<br/>

Built-in labelImg with YOLOv8 based automatic detection function.<br/>
Currently in English version, without localization.

## 预览图

![CE057907-DEA1-4ce7-B567-CA9913DE8F0C](https://github.com/T-SW/AutoLabelImg/assets/69509115/f59cfe39-0ddf-4397-b567-803e2d67c217)


## 新增功能：
对应快捷键如下所示。<br/>

### 1.自动标注
(1).Auto Label：当前图片<br/>
(2).Auto Label All：<br/>
&emsp;Current image and after：自动标注当前及之后的图片<br/>
&emsp;All images：自动标注全部图片<br/>
&emsp;Index range of images：自动标注指定序号(包含)间的图片<br/>

### 2.一键载入
load_data：快速载入上次标注记录点<br/>

### 3.重框筛选（Label Filter）
filterate计算iou筛选得到列表，Prev、Next前后载入疑似重框标注data。<br/>

## 使用
(1).default.yaml自动生成<br/>
(2).自动标注使用前**确认参数**<br/>
&emsp;- parameter_settings：含conf、iou、classes参数<br/>
&emsp;- model_selection：支持yolov8n、yolov8s、yolov8m、yolov8l、yolov8x<br/>
&emsp;- "./tools/change_labels.py"修改检测类别序号(coco --> 当前任务)<br/>
&emsp;&emsp;- def rework_classes(default=False):禁用修改<br/>
&emsp;&emsp;- def replace(line):按任务及使用情况灵活修改，默认2,5,7 --> 2。<br/>
(3).重框筛选使用前**确认参数**<br/>
&emsp;filter_conf、check_ls两个参数，在default.yaml中修改<br/>

## Installation
#### Windows + Anaconda
个人配置：NVIDIA GTX 1650 + cuda11.7<br/>

1.配置环境：<br/>
```pythonscript
conda create -n yourvenv python=3.8
conda activate yourvenv
pip install pyqt5
conda install -c anaconda lxml
安装torch：https://pytorch.org/

cd "your dir path"
pip install -r requirements.txt
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
```

2.下载模型：<br/>
根目录创建models文件夹，从[YOLOv8](https://github.com/ultralytics/ultralytics)中下载pt权重文件并放至文件夹内。<br/>

注：python3.10以上易崩，labelimg标框所用库数据格式不兼容等原因。<br/>

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
filterate  | F8
Prev  | F10
Next  | F12

## 程序崩溃原因

1."./data/predefined_classes.txt"与classes.txt不一致。<br/>
2.载入崩溃：删除C:\Users\用户名路径下的.labelImgSettings.pkl文件。
3.小概率画框/调框/删框时崩溃，未解决。重启、F5载入即可。

<br/>

## Contact information

*WeChat*：SW_7396        <br/>
*Email 163*：personalmailboxbyT@163.com



