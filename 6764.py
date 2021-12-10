depth = []
for _ in range(4):
    depth.append(int(input()))

if depth[0] < depth[1] < depth[2] < depth[3]:
    print('Fish Rising')
elif depth[0] > depth[1] > depth[2] > depth[3]:
    print('Fish Diving')
elif depth[0] == depth[1] == depth[2] == depth[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')

