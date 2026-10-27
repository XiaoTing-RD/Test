import random

while True:
    answer = random.randint(1, 100)
    count = 0

    while count < 7:
        try:
            guess = int(input("猜一个 1-100 的整数："))
        except ValueError:
            print("请输入整数!")
            continue

        count += 1
        if guess > answer:
            print("太大了")
        elif guess < answer:
            print("太小了")
        else:
            print(f"猜对了！你一共猜了 {count} 次")
            break

        print(f"还剩 {7 - count} 次机会")

    if count == 7 and guess != answer:
        print(f"机会用完，答案是 {answer}")

    if input("再玩一局？(y/n)：").lower() != "y":
        break