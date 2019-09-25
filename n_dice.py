import random


def main():
    何面 = int(input("サイコロの面の数は?: "))
    何回 = int(input("何回振りますか?: "))

    for i in range(何回):
        if i == 何回 - 1:
            print(random.randint(1, 何面))
        else:
            print(f"{random.randint(1, 何面)},", end="")


if __name__ == "__main__":
    main()
