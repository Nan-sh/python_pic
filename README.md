# python_pic
python爬取回车壁纸网风景照片

该脚本能每隔十分钟从回车壁纸网站自动下载一张风景照片，下载的照片位于/opt/python_pic/python_jpg/1和2里面，十分钟图片将被覆盖一次，你可以将桌面壁
纸设置为幻灯片，并将壁纸文件夹设置为1和2这两个文件夹，即可实现自动下载壁纸并设置为壁纸的功能。

注意，请在运行此脚本前安装好python，并且给予该脚本运行权限，即sudo chmod a+x auto_start.sh。
选择开机自启动：sudo ./auto_start.sh
