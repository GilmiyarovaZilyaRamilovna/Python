n = int(input())
m = [int(input()) for _ in range(n)]
p = int(input())
q = int(input())
print(sum(m[p-1:q]))