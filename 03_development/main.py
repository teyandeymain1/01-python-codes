from timetable_reader import *


# -----------------------------------------constants-----------------------------------------
# path of csv file
TIMETABLE_PATH = os.path.join(os.path.dirname(__file__), 'jaist_bus_timetable.csv')

# days and directions
week_or_holiday = {1:'平日用', 2:'休日用'}
bus_stops       = {1:'JAIST', 2:'ハイテクセンタ-前', 3:'宮竹ヘルスロ-ド', 4:'灯台笹', 5:'岩本', 6:'本鶴来', 7:'鶴来本町', 8:'鶴来駅'}
directions      = {1:'JAIST発', 2:'鶴来駅発'}
# ----------------------------------------------------------------------------------


# variables
current_time    = datetime.now() 
day             = week_or_holiday[1] if current_time.weekday() < 5 else week_or_holiday[2]  # Determine if current_time is a weekday or weekend


def main():

    print(f"現在時刻: {current_time}")
    n_b = int(input(f"バス停を選択し整数で入力してください。\n{bus_stops}\n: ").strip())

    if 1 <= n_b <= len(bus_stops):
        selected_bus_stop = bus_stops[n_b]
    else:
        print(f"無効なバス停番号です。1から {len(bus_stops)} の整数を入力してください。")
        exit(1)

    n_d = int(input(f"方面を選択し整数で入力してください。\n{directions}\n: ").strip())
    if 1 <= n_d <= len(directions):
        selected_direction = directions[n_d]        
    else:        
        print("無効な方面です。1または2の整数を入力してください。")
        exit(1)

    timetable                       = convert_csv_into_dict(TIMETABLE_PATH, week_or_holiday, directions)
    timetable_for_selected_bus_stop = extract_timetable_for_each_bus_stop(timetable, day, selected_direction, selected_bus_stop)
    next_bus_times                  = find_next_bus_times(current_time, timetable_for_selected_bus_stop)

    selecter = int(input("次の操作を選択し整数で入力してください:\n1. 次のバスの時刻を表示\n2. 現在時刻以降のすべてのバスの時刻を表示 \n: ").strip())

    if selecter == 1:
        print(f"次のバスの時刻: {next_bus_times[0]}")
    elif selecter == 2:
        print("現在時刻以降のすべてのバスの時刻:")
        for bus_time in next_bus_times:
            print(bus_time)
    else:
        print("無効な選択です。プログラムを終了します。")
        exit(1)


if __name__ == "__main__":
    main()