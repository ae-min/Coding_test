br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

x = max(abs(jr-br), abs(jc-bc))
y = abs(jr-dr)+abs(jc-dc)

if x>y :
    print('daisy')
elif x<y :
    print('bessie')
else : 
    print("tie")