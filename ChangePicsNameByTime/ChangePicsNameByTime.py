import os
import time
import exifread
import hachoir
from tqdm import tqdm


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


# 修改图片名称,返回新图片名字符串
def change_filename(old_filename, new_filename):
    # 打印修改对照
    # print(old_filename + " => " + new_filename)
    os.rename(old_filename, new_filename)
    return new_filename


# 创建或添加修改列表名单备注文件信息
def write_change_filename_info(old_filename, new_filename):
    # 修改列表名单备注文件名称
    info_name = "filename_change_info.txt"
    # 获得文件夹路径
    dirname = os.path.split(old_filename)[0]
    # 判断是否存在 name_change_info.txt 文件，不存在则创建并输入元信息，存在则写入信息
    if os.path.exists(os.path.join(dirname, info_name)):
        fd = open(os.path.join(dirname, info_name), "a")
        # 将文件路径修改为文件名
        old_filename = os.path.split(old_filename)[1]
        new_filename = os.path.split(new_filename)[1]
        fd.write(format(old_filename, '<60') + " => " + new_filename + '\n')
        fd.close()
    else:
        fd = open(os.path.join(dirname, info_name), "w")
        # 文件开头文字
        init_str = '''
  _____ _
 / ____| |
| |    | |__   __ _ _ __   __ _  ___
| |    | '_ \ / _` | '_ \ / _` |/ _ \\
| |____| | | | (_| | | | | (_| |  __/
 \_____|_| |_|\__,_|_|_|_|\__, |\___|
|  __ (_)        | \ | |   __/ |
| |__) |  ___ ___|  \| | _|___/ __ ___   ___
|  ___/ |/ __/ __| . ` |/ _` | '_ ` _ \ / _ \\
| |   | | (__\__ \ |\  | (_| | | | | | |  __/
|_|__ |_|\___|___/_| \_|\__,_|_| |_| |_|\___|
|  _ \   |__   __(_)
| |_) |_   _| |   _ _ __ ___   ___
|  _ <| | | | |  | | '_ ` _ \ / _ \\
| |_) | |_| | |  | | | | | | |  __/
|____/ \__, |_|  |_|_| |_| |_|\___|
        __/ |
       |___/                  made by hchX009\n\n'''
        init_str += "修改时间：" + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())) + '\n'
        init_str += "修改文件夹：" + os.path.abspath(dirname) + "\n\n"
        init_str += format("旧文件名", '<57') + " => 新文件名\n"
        # 写入修改列表名单备注文件中
        fd.write(init_str)
        fd.close()
    return


# 文件夹输入模块


# 主函数
def change_pics_name_by_time():
    # 文件格式字典
    picture_types = [".bmp", ".jpg", ".tiff", ".gif", ".png", ".webp", ".jpeg"]
    video_types = [".mp4", ".mkv"]

    # 路径
    img_folder_path = "../tmp/"
    # img_folder_path = "C:/Users/hecen/Desktop/Image/"
    # img_folder_path = "I:\BackupPictures\hch14"

    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    # 使用tqdm描述进度
    dirlist = tqdm(os.listdir(img_folder_path))
    for filename in dirlist:
        # os.path.join用于路径拼接，将imgpath和filename连在一起得到完整的路径，后面的参数可有多个，从第一个以”/”开头的参数开始拼接
        full_filename = os.path.join(img_folder_path, filename)
        # 打印路径
        # print('照片路径名称：' + full_file_name)
        # os.path.isfile用于判断路径指向的是否为文件，相类似的os.path.isdir用于判断是否为文件夹
        if os.path.isfile(full_filename):
            # 得到文件的后缀，并转化为全小写
            file_ext = get_file_ext(full_filename).lower()
            # 根据文件后缀分类处理
            if file_ext in picture_types:
                # 得到文件最早出现时间
                file_create_time = get_first_time(full_filename)
                # 构建初始新名称
                new_full_filename = os.path.join(img_folder_path, "IMG_" + file_create_time + "_0000" + file_ext)
                # 查询新名称是否被占用，占用则修改
                while os.path.exists(new_full_filename):
                    index = "%04d" % (int(new_full_filename.split('/')[-1][20:24]) + 1)
                    tmp_filename = "IMG_" + file_create_time + "_" + str(index) + file_ext
                    new_full_filename = os.path.join(img_folder_path, tmp_filename)
                # 修改文件名
                change_filename(full_filename, new_full_filename)
                # 修改信息写入备注文件中
                write_change_filename_info(full_filename, new_full_filename)
            elif file_ext in video_types:
                # print("Sorry you can not rename now")
                write_change_filename_info(full_filename, "Sorry you can not rename now")
            else:
                # print("Can not find the file's format")
                write_change_filename_info(full_filename, "Can not find the file's format")
        # 在命令行进度条中输出已经处理的数据
        dirlist.set_description("Processing" + format(filename, '^50'))


if __name__ == '__main__':
    change_pics_name_by_time()


# 暂时没用的代码
def vedio_rename(target_dir, filename, file_ext):
    # 解析文件
    the_file = hachoir.parser.createParser(target_dir + filename)
    if the_file:
        try:
            info = hachoir.metadata.extractMetadata(the_file)
        except Exception as err:
            print("元数据提取错误： %s" % err)
            info = None

        if info:
            for line in info.exportPlaintext():
                if 'Creation date' in line:
                    original_date = line.replace(
                        '- Creation date:', '').strip().split()
                    formated_name = original_date[0] + '_' + \
                                    original_date[1].replace(':', '') + file_ext
                    os.rename(target_dir + filename,
                              target_dir + formated_name)
                    print('新文件名：' + formated_name)

        else:
            print('无法提取元数据！')
    else:
        print('无法解析文件！')
