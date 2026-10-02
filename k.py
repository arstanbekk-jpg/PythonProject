n = int(input())
g = n % 1440
h = (g//60)% 24
m = g % 60
print(h,m)