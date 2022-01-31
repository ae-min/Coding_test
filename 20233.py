a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

aa = (t-30)*x*21
bb = (t-45)*y*21

if t<=30 :
    if t<=45:
        print(a)
        print(b)
    else :
        print(a)
        print(bb+b)
elif t>30 and t<=45:
    print(aa+a)
    print(b)
else :
    print(aa+a)
    print(bb+b)

