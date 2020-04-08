import os
import time
import exifread


#

# 得到图片最早的时间信息函数
def get_first_time(full_filename):
    # 以二进制的方式读取照片文件
    fd = open(full_filename, 'rb')

    # 尝试提取元信息exif到字典tags中
    try:
        tags = exifread.process_file(fd)
    except KeyError:
        # 判断创建时间与修改时间哪一个更早
        t = get_early_time(os.path.getmtime(full_filename), os.path.getctime(full_filename))
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(t))
        # print(full_filename + "未得到Exif信息！")
        # print(full_filename + ' => ' + time_str)
        return time_str
    else:
        # 正常提取exif则关闭文件
        fd.close()

    # 显示图片所有的exif信息
    # print("Show all Exif_info of " + full_filename + " :")
    # print(tags)

    # 在元数据exif寻找"EXIF DateTimeOriginal"项，获得拍摄时间
    if "EXIF DateTimeOriginal" in tags:
        # 直接获取到的结果格式类似为：2018:12:07 03:10:34
        # 修改为一定格式的时间信息：20181207_031034
        time_str = str(tags["EXIF DateTimeOriginal"]).replace(':', '').replace(' ', '_')[0:15]
        # print(full_filename + ' => ' + time_str)
        return time_str
    else:
        # 如果没有元数据，则返回创建日期或者修改日期中最早的时间
        # 判断创建时间与修改时间哪一个更早
        t = get_early_time(os.path.getmtime(full_filename), os.path.getctime(full_filename))
        time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(t))
        # print(full_filename + "未得到Exif信息！")
        # print(full_filename + ' => ' + time_str)
        return time_str


# 从两个时间中获得更早的时间
def get_early_time(t1, t2):
    if t1 >= t2:
        return t2
    else:
        return t1


# 获得图片格式
def get_file_ext(full_filename):
    # 将文件名和扩展名分开 ex：full_filename.txt => full_filename + .txt
    file_ext = os.path.splitext(full_filename)[1]

    # 打印格式
    # print('文件格式：' + file_ext)

    return file_ext


# 修改图片名称
def change_filename(old_filename, new_filename):
    # 打印修改对照
    print(old_filename + " => " + new_filename)
    os.rename(old_filename, new_filename)
    return


# 输出图片修改列表名单


# 文件夹输入模块


# 主函数
def change_pics_name_by_time():
    # 字典

    # 路径
    img_folder_path = "../tmp/"
    # img_folder_path = "C:/Users/hecen/Desktop/Image/"
    # img_folder_path = "I:\BackupPictures\hch14"

    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    for filename in os.listdir(img_folder_path):
        # os.path.join用于路径拼接，将imgpath和filename连在一起得到完整的路径，后面的参数可有多个，从第一个以”/”开头的参数开始拼接
        full_filename = os.path.join(img_folder_path, filename)
        # 打印路径
        # print('照片路径名称：' + full_file_name)
        # os.path.isfile用于判断路径指向的是否为文件，相类似的os.path.isdir用于判断是否为文件夹
        if os.path.isfile(full_filename):
            file_ext = get_file_ext(full_filename)
            file_create_time = get_first_time(full_filename)
            new_full_filename = os.path.join(img_folder_path, "IMG_" + file_create_time + "_0000" + file_ext)
            while os.path.exists(new_full_filename):
                index = "%04d" % (int(new_full_filename.split('/')[-1][20:24]) + 1)
                new_full_filename = os.path.join(img_folder_path, "IMG_" + file_create_time + "_" + str(index) + file_ext)
            change_filename(full_filename, new_full_filename)


if __name__ == '__main__':
    change_pics_name_by_time()
