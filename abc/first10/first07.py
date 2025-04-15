#https://atcoder.jp/contests/abc085/tasks/abc085_b
n=int(input())
d = [input() for i in range(n)]
d_only=set(d)
print(len(d_only))