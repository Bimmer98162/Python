'''题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.程序源代码：
'''
x=input("please enter the date:(such as:2022.10.27 )")
a,b,c=x.split(".")
a=int(a)
b=int(b)
c=int(c)
d=[0,31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
if a%4==0 and a%100!=0 or a%400==0:#为闰年，二月为29
    d[2]=29
    for i in range(b):
        sum+=d[i]
    print("The day is ",sum+c)
else:
    d[2]=28
    for i in range(b):
        sum+=d[i]
    print("The day is ",sum+c)
    print