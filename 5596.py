a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) != sum(b):
    print(max(sum(a),sum(b)))
else: 
    print(sum(a))