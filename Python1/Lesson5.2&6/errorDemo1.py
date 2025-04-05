#定义一个BankAccount类，包含账户名和账户余额两个属性
#deposite() -> 存款（如果输入为负数，则抛出ValueError的异常）
#withdraw() -> 取款（负数/大于余额，抛出ValueError）
#get_balanced -> 返回账户余额
#创建用户，执行该用户存款取款的操作，每次操作后显示余额并记录用户行为和余额到一个log日志中
#对用户输入进行异常处理，确保用户输入为有效数字
from datetime import datetime

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            raise ValueError
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

'''class logger:
    def __init__(self, filename:str):
        self.filename = filename

    def info(self):
        with open(self.filename, 'a+') as file:
            file.write(f"{str(datetime.now())} \n")'''
logger = Logger("Bank_log.txt")
account = BankAccount("Ming", 1000,logger)

while True:
    print("\n请选择操作")
    print("1. 存款")
    print("2. 取款")
    print("3. 查询金额")
    print("4. 退出")

    choice = input("请输入操作编号")

    try:
        if choice == "1":
            amount = float(input("请输入存款金额"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("请输入取款金额"))
            account.withdraw(amount)
        elif choice == "3":
            print(f"当前余额为: {account.get_balance()}元")
        elif choice == "4":
            print("退出系统")
            break
        else:
            print("无效操作，请重新输入")
    except ValueError:
        print("无效操作，请输入有效数字")

A = BankAccount("a", 5000)
A.deposit(100)
print(A.balance)
log = logger(filename="log.txt")
log.info()