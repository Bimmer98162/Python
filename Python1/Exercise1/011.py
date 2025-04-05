month=int(input('请输入月份：'))
if month==1 or month==2:  #前两个月没有长大，没有规律，所以单拿出来
    print('一共有1只兔子')
else:
    a=1   #第一个月
    b=1   #第二个月
    c=0   #一会求和用的变量，需要提前使其为0
    for i in range(3,month + 1):  #因为1,2月的已经说明，所以从三月开始
        c=a+b   #第n个月等于第n-1个月+第n-2个月
        a=b    #将n-2=n-1
        b=c    #将n-1=n
    print(c)
