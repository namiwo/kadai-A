def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    temperature_sum = 0
    for japan in weather_information:
        temperature_sum += japan["temperature"]
    temperture_ave = temperature_sum / len(weather_information)

    print(f"全国の平均気温は{temperture_ave}")

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    for osaka in weather_information[3:6]:
        if osaka["station"] == "堺":
            print(osaka["station"])
        else:
            print(f"{osaka['station']},", end="")

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temperature_sum = 0
    for fukuoka in weather_information[6:8]:
        fukuoka_temperature_sum += fukuoka["temperature"]
    fukuoka_temperature_ave = fukuoka_temperature_sum / 2

    print(f"福岡の平均気温は{fukuoka_temperature_ave}")


if __name__ == "__main__":
    main()
