#https://atcoder.jp/contests/abc081/tasks/abc081_a

#解法1
s = input()
count = s.count("1")
print(count)

#解法2
s = input()
count = 0
if s[0]=="1":
    count +=1
if s[1] == "1":
    count +=1
if s[2] == "1":
    count +=1
print(count)