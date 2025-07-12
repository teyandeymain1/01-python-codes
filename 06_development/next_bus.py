import csv
from datetime import datetime

def load_schedule(csv_file):
    """
    CSVファイルを読み込んで、各駅ごとの発車時刻リストを返す
    CSVの一行目が駅名、以降が時刻データ
    """
    schedule = {}
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        stations = [h.strip() for h in headers if h.strip()]
        for s in stations:
            schedule[s] = []
        for row in reader:
            for i, cell in enumerate(row[:len(stations)]):
                t = cell.strip()
                if t:
                    schedule[stations[i]].append(t)
    return schedule


def get_next_buses(times_list, count=3):
    """
    現在時刻以降の次の発車時刻を最大count件返す
    """
    now = datetime.now().time()
    upcoming = []
    for t in times_list:
        try:
            bus_time = datetime.strptime(t, "%H:%M").time()
        except ValueError:
            continue
        if bus_time >= now:
            upcoming.append(t)
            if len(upcoming) >= count:
                break
    return upcoming


if __name__ == '__main__':
    schedule = load_schedule('time_table.csv')
    station = input('出発駅を入力 (デフォルト: 鶴来発): ').strip() or '鶴来発'
    if station not in schedule:
        print(f"駅 '{station}' が見つかりません。")
    else:
        next_buses = get_next_buses(schedule[station], count=3)
        if not next_buses:
            print('本日の運行は終了しました。')
        else:
            print(f"次のバスは {', '.join(next_buses)} です。")
