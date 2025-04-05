#OS库练习：

#创建一个新目录
import os
import pandas
from fileinput import filename

new_dir = "example_directory"
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    print(f"{new_dir} created!")
else:
    print(f"{new_dir} already exists!")
print("")

#列出当前目录中所有的文件和子目录
print("All files and sub_directories in current folder are:")
for item in os.listdir('.'):    #'.'表示当前目录
    print(item)
print("")

#创建一个新文件并写入内容
filename = os.path.join(new_dir, "example_file.txt")
with open(filename, "w") as f:
    f.write("Example text.\nWelcome!")
print(f"{filename} written successfully!")

#读取文件内容

#删除文件
os.remove(filename)

#删除目录
os.rmdir(new_dir)