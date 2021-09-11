def solution(id_list, report, k):
    who = {} # 누구를 누가 신고했는지 ex) "muzi" : ["apeach", "ryan"] --> apeach랑 ryan이 muzi를 신고
    send = {} # 누구에게 메일을 몇 통 보낼지 ex) "muzi": 2 --> muzi에게 2통
    for e in id_list:
        send[e] = 0
        who[e] = set() # muzi에게 apeach가 여러번 신고 넣어도 한번으로 취급. 즉 중복을 피하기 위해 set 사용
    for e in report:
        l = e.split()
        who[l[1]].add(l[0])
    for elem in who:
        if len(who[elem]) >= k:
            for e in who[elem]:
                send[e] += 1
    answer = []
    for e in send:
        answer.append(send[e])
    return answer
