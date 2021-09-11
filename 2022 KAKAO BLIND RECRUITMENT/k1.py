def solution(id_list, report, k):
    who = {}
    send = {}
    for e in id_list:
        send[e] = 0
        who[e] = set()
    for e in report:
        l = e.split()
        who[l[1]].add(l[0])
        #count[l[1]] += 1
    for elem in who:
        if len(who[elem]) >= k:
            for e in who[elem]:
                send[e] += 1
    answer = []
    for e in send:
        answer.append(send[e])
    return answer