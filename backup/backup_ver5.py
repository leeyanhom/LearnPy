# 维护阶段-改进
import os
import time
import zipfile

# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
source = ['C:\\Users\\Administrator\\Documents\\PycharmProjects\\LearnPy']
# 除了使用双反斜杠转义序列，你还可以使用原始字符串。例如使用 'C:\\Documents' 或 r'C:\Documents'
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称
file = input('添加其他压缩文件目录：')
running = True
if os._exists(file):
    source.extend(file)
    print("添加成功")
else:
    print('文件目录不存在')
    running = False
#2. 备份文件必须存储在一个
#主备份目录中
target_dir = 'E:\\Backup'
# 3. 备份文件将打包压缩成 zip 文件。
# 4. 将当前日期作为主备份目录下的子目录名称
# 子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S') # 当前时间作为 zip 文件的文件名
target = today + os.sep + now + '.zip'
# os.sep 变量的使用方式——它将根据你的操作系统给出相应的分隔符
# 在 GNU/Linux 与 Unix 中它会是 '/'，在 Windows 中它会是 '\\'，在 Mac OS 中它会是 ':'
# 使用 os.sep 而非直接使用这些字符有助于使我们的程序变得可移植，从而可以在上述这些系统中都能正常工作
# %Y 将被替换成带有具体世纪的年份。%m 将会被替换成以 01 至 12 的十进制数所表示的月份

# 添加一条来自用户的注释以创建
# zip 文件的文件名
comment = input('Enter a comment -->')
# 检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ','_') + '.zip'
# len 函数来检查输入内容的长度，以检查用户是否确实输入了什么内容。如果用户未输入任何内容而直接敲下了 enter 键

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. 我们使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target,''.join(source))
# -r 递归地对目录进行工作
#字符串方法 join 来将列表 source 转换成字符串

#执行
print('Zip command is:')
print(zip_command)
print('Running:')
# os.system 函数可以使命令像是从系统中运行的
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

