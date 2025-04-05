#以写入模式创建一个新文件，并写入5行内容
#在第三行插入一个新的行
#返回现在指针所在的位置
#在文件末尾添加一行
with open("example_2.txt", "w") as f:
    f.write("aaa\n")
    f.write("bbb\n")
    f.write("ccc\n")
    f.write("ddd\n")
    f.write("eee\n")
with open("example_2.txt", "r") as f:
    lines = f.readlines()

if len(lines) >= 3:
    lines[2] = "new three\n"

while len(lines) < 6:
    lines.append("\n")
lines[5] = "new three\n"
with open("example_2.txt", "w") as f:
    f.writelines(lines)
print("修改完成")