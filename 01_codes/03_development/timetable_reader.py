import os
import csv
from datetime import *


def convert_csv_into_dict(csv_path: str, week_or_holiday: str, directions: dict) -> dict:

    with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
        timetable_reader = list(row.strip().split(',') for row in csv_file if row.strip())
    
    timetable   = dict()
    day         = None
    direction   = None
    
    for row in timetable_reader:

        if row[0] == week_or_holiday:
            day = week_or_holiday
            continue
        else:
            pass

        if day and row[0] == directions[1]:     # if day/=None and direction==JAIST発
            direction               = directions[1]
            timetable[direction]    = list()
            continue
        elif day and row[0] == directions[2]:   # if day/=None and direction==鶴来駅発
            direction               = directions[2]
            timetable[direction]    = list()
            continue
        else:
            pass

        if day and direction:   # Check if day/=None and direction/=None
            normalized_row = list(bus_stop.strip() for bus_stop in row)  # Normalize each words in row
            timetable[direction].append(normalized_row)    # timetable = {direction: [時刻1, 時刻2, ...]}
        else:
            pass

    return timetable        


# def extract_timetable_for_each_bus_stop(timetable: dict, selected_direction: str, departure_stop: str, arrival_stop: str = None) -> list:
def extract_timetable_for_each_bus_stop(timetable: dict, selected_direction: str, selected_bus_stop: str) -> list:

    selected_timetable = list()

    if selected_direction in timetable:
        selected_timetable  = timetable[selected_direction]
        bus_stop_index      = find_bus_stop_index(selected_timetable, selected_bus_stop)
        if bus_stop_index == -1:
            print(f"内部処理エラー: '{selected_bus_stop}'バス停は存在しません。csvファイルを確認してください。")
            return list()
        else:
            return list(row[bus_stop_index] for row in selected_timetable[1:])           
    else:
        print(f"内部処理エラー: '{selected_direction}'方面は存在しません。csvファイルを確認してください。")
        return list()


# def find_bus_stop_index(selected_timetable: list, departure_stop: str, arrival_stop: str = None) -> int:
def find_bus_stop_index(selected_timetable: list, selected_bus_stop: str) -> int:

    bus_stop_index = -1

    for n, bus_stop in enumerate(selected_timetable[0]):
        if bus_stop == selected_bus_stop:
            bus_stop_index = n
            break
        else:
            continue

    return bus_stop_index


# def find_next_bus_times(current_datetime: datetime, timetable_for_departure_stop: list, timetable_for_arrival_stop: list = None) -> list:
def find_next_bus_times(current_datetime: datetime, timetable_for_selected_bus_stop: list) -> list:

    next_bus_times = list()

    for i, next_bus_time in enumerate(timetable_for_selected_bus_stop):
        if  i >= len(timetable_for_selected_bus_stop):
            next_bus_times = ["本日の運行は終了しました。"]
            break
        elif next_bus_time == "-":
            continue
        else:
            (hours, minutes)    = next_bus_time.split(':') 
            next_bus_datetime   = datetime(current_datetime.year, current_datetime.month, current_datetime.day, int(hours), int(minutes))
            if next_bus_datetime > current_datetime:
                next_bus_times.append(next_bus_time)
            else:
                continue

    return next_bus_times