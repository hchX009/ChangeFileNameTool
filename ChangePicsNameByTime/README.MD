## ChangePicsNameByTime 说明

文件夹中大量图片规律重命名好帮手！

### 简介说明
这个程序目前的功能为通过读取文件夹中每个图片中的Exif信息或者图片文件的创建和修改日期，找到合理的最早时间，将这个最早时间对每个图片进行重命名，方便对文件夹中大量图片的整理和管理。（新增对同文件夹下的拍摄视频按拍摄事间重命名，原理同上，但测试不全）  
+ 举例：如果一张照片被命名为example.jpg，拍摄于2020年4月14日上午8点30分26秒，运行程序后将命名为IMG_20200414_083026_0000.jpg
+ 命名格式解析：IMG代表图片（VID代表拍摄视频），20200414_083026代表该文件能够找到的最早时间（一般是拍摄时间或者图片文件创建时间），0000则为防止同时间图片设置的编号（发生重命名时递增，范围0000~9999）

### 支持格式
图片格式：bmp，jpg，tiff，gif，png，webp，jpeg  
视频格式：mp4，mov，mkv

### 文件目录说明
源码：ChangePicsNameByTime.py  
可执行文件位置：dist/ChangePicsNameByTime_0.8.5.exe  

### python版本说明
python版本：python3.7  
目前使用的库：
+ os
+ time
+ pytz
+ datetime
+ exifread
+ hachoi.parser
+ tqdm
+ tkinter

### 使用方式
1.打开  
+ 使用python3.7安装以上库后运行源码（推荐）  
+ 直接点击exe文件开始运行（由于未知原因，点开后会出现终端并需等待5-6秒才可以开始操作）

2.运行（后续版本会增加GUI）
+ 在弹出的窗口中选择需要批量重命名的照片所在的文件夹
+ 通过弹出的终端观察进度条并等待重命名完成（1秒100到300张左右）

3.完成
+ 重命名完成后会在目标文件夹下自动生成filename_change_info.txt文件，记录旧文件名和新文件名以供查阅

### 注意事项
+ 暂时有部分乱码命名无法处理，在运行过程中会被中断
+ 同文件夹下的视频重命名可能会产生问题（还在研究中）