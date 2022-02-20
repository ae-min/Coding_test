x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

z1 = y1
z2 = z1-x2+y2
z3 = z2-x3+y3
z4 = z3-x4

print(max(z1,z2,z3,z4))