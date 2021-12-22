Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
x = max(0, Cr-Ca) + max(0, Br-Ba) + max(0, Pr-Pa)
print(x)