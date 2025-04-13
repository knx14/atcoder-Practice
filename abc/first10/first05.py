#https://atcoder.jp/contests/abc083/tasks/abc083_b
N, A, B = map(int, input().split())
total_sum = 0
for i in range(1,N+1):
    digit_sum = sum(map(int,str(i)))
    if A<=digit_sum<=B:
        total_sum+=i
print(total_sum)