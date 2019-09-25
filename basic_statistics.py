def main():
    # 入力
    num_list = input("データを入力してください(スペース区切り) > ").split()

    # 計算
    sum = 0
    ave = 0
    max = int(num_list[0])
    min = int(num_list[0])

    for i in num_list:
        inti = int(i)
        I = inti
        sum += I
        if I > max:
            max = I
        if I < min:
            min = I
    ave = sum / len(num_list)

    # 出力
    print(f"合計値: {sum}")
    print(f"最大値: {max}")
    print(f"最小値: {min}")
    print(f"平均値: {int(ave)}")


if __name__ == "__main__":
    main()
