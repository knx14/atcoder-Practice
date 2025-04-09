#https://atcoder.jp/contests/abc081/tasks/abc081_b
#for分を利用した全探索
n = int(input())
a = list(map(int,input().split))
count = 0
while True:
 for i in range(n):
   if a[i] % 2 != 0:
     print(count)
     exit()
   a[i] //=2
 count +=1

#関数を使用した解き方
def max_divide_operations(n,a):
  min_operations = float('inf')
  for num in a:
    count = 0
    while num % 2 ==0:
      num //= 2
      count +=1
    min_operations = min(min_operations,count)
  return min_operations

n = int(input())
a = list(map(int,input().split()))
print(max_divide_operations(n,a))
