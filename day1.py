import random
a=int(random.randint(1,100))
b=(input("来玩猜数字吧，请选择一个一到一百之间的数："))
if b.isdigit():
    b=int(b)
else:
    print("请输入整数!")
c=0
while b != a:
    c+=1
    if b>a:
        print("猜大了,",end="")
    if b<a:
        print("猜小了,",end="")
    if c<7:
        print(f"你一共有七次机会，现在还有{7-c}次机会，七次猜不出来我会给提示，加油")
    if c==7:
        print(f"机会用完了，给你个提示吧，答案在{a-random.randint(4,15)}和{a+random.randint(4,15) if a+random.randint(4,15)<=100 else '100'}之间")
    b=int(input("再来猜一次吧："))
else:
    print(f"恭喜你猜对了，答案是{b},你一共猜了{c}次")