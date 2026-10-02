n = int(input())

t = 45*n + 5*(n//2) + 15*((n-1)//2)

hours = 9 + t // 60
minutes = t % 60

print(hours, minutes)