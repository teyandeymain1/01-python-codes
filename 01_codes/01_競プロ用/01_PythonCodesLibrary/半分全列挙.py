import sys
from itertools import combinations

# 半分全列挙による解法
def solve_problem(N, inTuple):
    # タプルを2つに分割
    first_half = inTuple[:N // 2]
    second_half = inTuple[N // 2:]

    # 各半分の部分集合の和を列挙
    def subset_sums(nums):
        sums = set()
        for r in range(len(nums) + 1):
            for combo in combinations(nums, r):
                sums.add(sum(combo))
        return sums

    # それぞれの部分集合の和を計算
    first_sums = subset_sums(first_half)
    second_sums = subset_sums(second_half)

    # 目標値は全体の半分
    total_sum = sum(inTuple)
    half = total_sum // 2

    # second_sums をソートして二分探索できるようにする
    second_sums = sorted(second_sums)

    # 最小の答えを見つける
    ans = 10**10

    for f in first_sums:
        # second_sums の中から half - f 以上の最小値を探す
        lo, hi = 0, len(second_sums)
        while lo < hi:
            mid = (lo + hi) // 2
            if second_sums[mid] + f >= half:
                hi = mid
            else:
                lo = mid + 1
        if lo < len(second_sums):
            ans = min(ans, second_sums[lo] + f)

    return ans

#======================================main==============================================
def main():
    # 標準入力を読み取る
    readline = sys.stdin.read
    input_data = readline().splitlines()  # 複数行の入力を扱うためにsplitlinesを使う
    
    # 1行目：Nの値を取得
    N = int(input_data[0])
    
    # 2行目：タプルに変換
    inTuple1 = tuple(map(int, input_data[1].split()))
    
    # 解を出力
    print(solve_problem(N, inTuple1))

if __name__ == "__main__": 
    main()

"""
このコードの目的は、リスト内の要素からなる部分集合のうち、
指定された半分以上の和を持つ最小の和を見つけることです。
具体的には、solve_problem 関数内でべき集合（すべての部分集合）を作成し、
部分集合の和が半分以上の中で最小のものを見つけて返しています。
半分全列挙 (meet-in-the-middle) というアルゴリズムを使うことで、
べき集合を作らずに効率的に解を求めることができます。これにより計算量が大幅に改善され、
O(2^(N/2)) になります。
inTuple を2つに分割し、それぞれの部分集合の和を subset_sums 関数で計算します。
その後、1つ目の部分集合の和に対して、2つ目の部分集合の和から half に近いものを二分探索で探します。
"""