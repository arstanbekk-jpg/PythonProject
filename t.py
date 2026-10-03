n = input().zfill(4)
print(1*(n == n[::-1]) + 37 * (n !=n[::-1]))