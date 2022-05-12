def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for a,b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1] #다 돌아도 없을 경우, 마지막주자가 완주하지 못한 선수

