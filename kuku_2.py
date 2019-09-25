def main():
    # 入力
    行 = 4
    列 = 6

    # 計算・出力

    for i in range(1, 行 + 1):
        for j in range(1, 列 + 1):
            print(f"{i * j} ", end="")
        print("\n")


if __name__ == "__main__":
    main()
