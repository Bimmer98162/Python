#定义一个用户类(User),用户名(username)和密码(password)是这个类的属性。
#实例化两个用户,分别有不同的用户名和密码。
#设计一个方法 修改密码
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print(self.username, self.password)

    def changePassword(self, newpassword):
        self.password = newpassword
        print(f"New password: {newpassword}")

User1 = User("Unknown001", "unknown001password")
User2 = User("Unknown002", "unknown002password")

User1.changePassword("<Unknown001PASSWORD>")
User2.changePassword("<Unknown002PASSWORD>")