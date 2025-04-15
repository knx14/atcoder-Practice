#https://atcoder.jp/contests/abc088/tasks/abc088_b
n=int(input())
a=list(map(int,input().split()))
alice_score=0
bob_score=0
a.sort(reverse=True)
for i in range(n):
    if i%2==0:
        alice_score+=a[i]
    else:
        bob_score+=a[i]
print(alice_score-bob_score)