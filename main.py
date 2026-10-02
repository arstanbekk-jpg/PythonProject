x1,y1,x2,y2 = map(int,input().split())
if abs(x2-x1)== 1 or abs(y2-y1)== 1:
    print("YES")
else:
    print("NO")