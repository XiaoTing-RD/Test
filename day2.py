history=[]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    c=int(input("欢迎使用计算器，请选择模式，1：加法，2：减法，3：乘法，4：除法，5：回顾历史，6：退出："))
    if c==6:
        print("已退出")
        break
    if c>6 or c<1:
        print("请重新输入数字，以选择正确模式：")
        continue
    if c==5:
        print("你现在的历史记录是：")
        for record in history:
            print(record)
        continue
    a=int(input("请输入第一个数："))
    b=int(input("请输入第二个数："))
    if c==1:
        result=add(a,b)
        history.append(f"{a}+{b}={result}")
    if c==2:
        result=sub(a,b)
        history.append("{a}-{b}={result}")
    if c==3:
        result=mul(a,b)
        history.append(f"{a}*{b}={result}")
    if c==4:
        if b==0:
            print("0不能作为除数，请重新输入:")
            continue
        result=div(a,b)
        history.append(f"{a}/{b}={result}")
    print(f"答案是：{result}")

    