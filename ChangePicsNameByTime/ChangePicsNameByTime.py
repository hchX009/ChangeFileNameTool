import os
import time
import exifread

# 得到exif信息
def getExif(full_filename, format):
    # 以二进制的方式读取照片文件
    fd = open(full_filename, 'rb')
    # 提取元信息exif到字典tags中
    try:
        tags = exifread.process_file(fd)
    except KeyError:
        t = os.path.getctime(full_filename)
        print(full_filename + ' => ' + time.strftime("%Y%m%d_%H%M%S", time.localtime(t)))
        return
    # 关闭文件
    fd.close()
    # 显示图片所有的exif信息
    # print("Show all Exif_info of " + full_filename + " :")
    # print(tags)
    # 设置只查找DateTimeOriginal的项
    DTO = 'EXIF DateTimeOriginal'
    if DTO in tags:
        # 获取到的结果格式类似为：2018:12:07 03:10:34
        # print(str(tags[DTO]))
        # 获取结果格式类似为：20181207_031034
        # print(str(tags[DTO]).replace(':', '').replace(' ', '_'))
        name = 'IMG_' + str(tags[DTO]).replace(':', '').replace(' ', '_') + format
        print(full_filename + ' => ' + name)
    '''
        time = new_name.split(".")[0][:13]
        new_name2 = new_name.split(".")[0][:8] + '_' + filename
        print("\nfilename: %s" % filename)
        print("\n%s的拍摄时间是: %s年%s月%s日%s时%s分" % (filename, time[0:4], time[4:6], time[6:8], time[9:11], time[11:13]))

        # 可对图片进行重命名
        # new_full_file_name = os.path.join(imgpath, new_name2)
        # print(old_full_file_name," ---> ", new_full_file_name)
        # os.rename(old_full_file_name, new_full_file_name)
    else:
        print('No {} found'.format(FIELD), ' in: ', old_full_file_name)
    '''
# 获得图片格式
def getFormat(full_filename):
    # 将文件名和扩展名分开 ex：full_filename.txt => full_filename + .txt
    format = os.path.splitext(full_filename)[1]
    # 打印格式
    # print('文件格式：' + format)
    return format

# 主函数
def main():
    imgFolderPath = "C:/Users/hecen/Desktop/Image" #"../tmp/"

    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    for filename in os.listdir(imgFolderPath):
        # os.path.join用于路径拼接，将imgpath和filename连在一起得到完整的路径，后面的参数可有多个，从第一个以”/”开头的参数开始拼接
        full_filename = os.path.join(imgFolderPath, filename)
        # 打印路径
        # print('照片路径名称：' + full_file_name)
        # os.path.isfile用于判断路径指向的是否为文件，相类似的os.path.isdir用于判断是否为文件夹
        if os.path.isfile(full_filename):
            format = getFormat(full_filename);
            if(format == '.jpg'):
                getExif(full_filename, format)


if __name__ == '__main__':
    main()


