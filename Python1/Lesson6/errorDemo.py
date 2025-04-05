#输入两个数字，计算它们的除法运算
#检查：1 用户输入的是否为数字。 2 除数不能为0。 3 遇到问题要捕获错误并提示用户，不中断程序
#使用try-except来处理异常，else用于没有异常的情况，finally输出一句“程序结束，感谢使用”

def numberDivision():
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))

            assert b != 0, "错误，除数不能为0"

        except ValueError:
            print("请输入数字！")
            continue

        except AssertionError as e:
            print(e)
            continue
        else:
            print(f"结果为{a / b}")
            break
        finally:
            print("程序结束")

numberDivision()