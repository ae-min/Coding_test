for i in range(3):
    fh, fm, fs, lh, lm, ls = map(int, input().split())
    first = (fm * 60) + (fh * 3600) + fs
    last = (lm * 60) + (lh * 3600) + ls
    time = last - first
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    print("%d %d %d" %(h, m, s))
    
'''
퇴근시간을 입력받아서 근무한 시간을 출력하는 알고리즘이다.
간단하게 초단위로 시간을 계산했다.
시간은 초에 3600을 나눈 몫이고,
분은 초에 3600을 나눈 나머지에 60을 나눈 몫이다.
초는 초에 3600을 나눈 나머지에 60을 나눈 나머지이므로 계산해주어 출력해준다.
'''