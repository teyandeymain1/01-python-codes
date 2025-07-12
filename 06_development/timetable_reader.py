import csv
import datetime
from typing import List, Dict, Optional

class TimetableReader:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file
        self.weekday_jaist_times = []
        self.weekday_tsuruki_times = []
        self.holiday_jaist_times = []
        self.holiday_tsuruki_times = []
        self.load_timetable()
    
    def load_timetable(self):
        """CSVファイルから時刻表を読み込む"""
        with open(self.csv_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        current_section = None
        current_direction = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # セクションの判定
            if line.startswith('平日用'):
                current_section = 'weekday'
                continue
            elif line.startswith('休日用'):
                current_section = 'holiday'
                continue
            
            # 方向の判定
            if 'JAIST発' in line:
                current_direction = 'jaist'
                continue
            elif '鶴来駅発' in line:
                current_direction = 'tsuruki'
                continue
            
            # ヘッダー行はスキップ
            if ('JAIST' in line and 'ハイテクセンター前' in line) or ('鶴来駅' in line and '鶴来本町' in line):
                continue
            
            # 時刻データの処理
            if current_section and current_direction:
                times = [t.strip() for t in line.split(',') if t.strip() and t.strip() != '-']
                if times and ':' in times[0]:  # 時刻データかチェック
                    if current_section == 'weekday':
                        if current_direction == 'jaist':
                            self.weekday_jaist_times.extend(times)
                        else:
                            self.weekday_tsuruki_times.extend(times)
                    else:
                        if current_direction == 'jaist':
                            self.holiday_jaist_times.extend(times)
                        else:
                            self.holiday_tsuruki_times.extend(times)
    
    def parse_time(self, time_str: str) -> Optional[datetime.time]:
        """時刻文字列をdatetime.timeオブジェクトに変換"""
        try:
            hour, minute = map(int, time_str.split(':'))
            return datetime.time(hour, minute)
        except:
            return None
    
    def get_next_buses(self, direction: str = 'both', count: int = 5) -> Dict:
        """直近のバス時刻を取得"""
        now = datetime.datetime.now()
        current_time = now.time()
        is_weekday = now.weekday() < 5  # 月曜日=0, 日曜日=6
        
        # 使用する時刻表を選択
        if is_weekday:
            jaist_times = self.weekday_jaist_times
            tsuruki_times = self.weekday_tsuruki_times
            day_type = "平日"
        else:
            jaist_times = self.holiday_jaist_times
            tsuruki_times = self.holiday_tsuruki_times
            day_type = "休日"
        
        result = {
            'day_type': day_type,
            'current_time': current_time.strftime('%H:%M'),
            'jaist_buses': [],
            'tsuruki_buses': []
        }
        
        # JAIST発の直近バス
        if direction in ['jaist', 'both']:
            upcoming_jaist = []
            for time_str in jaist_times:
                bus_time = self.parse_time(time_str)
                if bus_time and bus_time > current_time:
                    upcoming_jaist.append(time_str)
            result['jaist_buses'] = upcoming_jaist[:count]
        
        # 鶴来駅発の直近バス
        if direction in ['tsuruki', 'both']:
            upcoming_tsuruki = []
            for time_str in tsuruki_times:
                bus_time = self.parse_time(time_str)
                if bus_time and bus_time > current_time:
                    upcoming_tsuruki.append(time_str)
            result['tsuruki_buses'] = upcoming_tsuruki[:count]
        
        return result
    
    def display_next_buses(self, direction: str = 'both', count: int = 5):
        """直近のバス時刻を表示"""
        result = self.get_next_buses(direction, count)
        
        print(f"\n=== {result['day_type']} 時刻表 ===")
        print(f"現在時刻: {result['current_time']}")
        print("-" * 40)
        
        if direction in ['jaist', 'both'] and result['jaist_buses']:
            print(f"\n【JAIST発 → 鶴来駅】")
            print("直近のバス:")
            for i, time in enumerate(result['jaist_buses'], 1):
                print(f"  {i}. {time}")
        
        if direction in ['tsuruki', 'both'] and result['tsuruki_buses']:
            print(f"\n【鶴来駅発 → JAIST】")
            print("直近のバス:")
            for i, time in enumerate(result['tsuruki_buses'], 1):
                print(f"  {i}. {time}")
        
        if not result['jaist_buses'] and not result['tsuruki_buses']:
            print("\n今日はもうバスがありません。")

def main():
    # 時刻表リーダーを初期化
    reader = TimetableReader('time_table.csv')
    
    print("=== バス時刻表システム ===")
    print("1. 全方向の直近バス")
    print("2. JAIST発のみ")
    print("3. 鶴来駅発のみ")
    
    choice = input("\n選択してください (1-3): ").strip()
    
    if choice == '1':
        reader.display_next_buses('both')
    elif choice == '2':
        reader.display_next_buses('jaist')
    elif choice == '3':
        reader.display_next_buses('tsuruki')
    else:
        print("無効な選択です。全方向を表示します。")
        reader.display_next_buses('both')

if __name__ == "__main__":
    main()
