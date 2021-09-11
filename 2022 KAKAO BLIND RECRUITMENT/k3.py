from datetime import datetime
import math

car_list = {}
how_long = {}
cost = {}

def cal(time, car, what):
    if what == "IN":
        car_list[int(car)] = time
    else:
        out_time = datetime.strptime(time,"%H:%M")
        in_time = datetime.strptime(car_list[int(car)],"%H:%M")
        minutes = ((out_time - in_time).seconds)/60
        del car_list[int(car)]
        return minutes
        
def solution(fees, records):
    park_min, pay, plus_min, plus_pay = fees
    for e in records:
        time, car, what = e.split()
        if what == "IN":
            if int(car) not in how_long:
                how_long[int(car)] = 0
            cal(time, car, what)
        else:
            minutes = cal(time, car, what)
            how_long[int(car)] += minutes
    
    if car_list != {}:
        for car, v in car_list.items():
            out_time = datetime.strptime("23:59","%H:%M")
            in_time = datetime.strptime(car_list[car],"%H:%M")
            minutes = ((out_time - in_time).seconds)/60
            how_long[int(car)] += minutes
    
    for car, minutes in how_long.items():
        if minutes <= park_min:
            cost[int(car)] = pay
        else:
            payment = pay + math.ceil((minutes - park_min) / plus_min) * plus_pay
            cost[int(car)] = payment
    
    opop = list(cost.keys())
    opop.sort()
    
    answer = []
    for e in opop:
        answer.append(cost[e])
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
### 답 : [14600, 34400, 5000]

print(cost)

### comment : 당시 저 문제 풀때는 str 형태를 datetime으로 바꿔서 푸는 방법 외에는 떠오르지 않았는데, 끝나고 나니 굳이 저렇게까지 import해서 풀 필요가 없는 문제인데 좀 허무(?)했다. 아래와 같이 간단하게 minute 형태로 계산해서 풀수 있다는 점 ~!!

# in_time, out_time 구하는 방식은 00:00 을 기준으로 하여 몇 분이 흘렀는지를 계산한 뒤, 그 둘의 차이를 통해 주차 하고 빠져나가는 데까지 걸린 시간(분)을 구했다.
# 예를 들어, 6:45 ~ 10:30 까지 몇 분이 흘렀는지를 알고 싶다!! 그러면
# --> (00:00 부터 10:30까지 흐른 시간(분)) - (00:00 부터 6:45까지 흐른 시간(분))

# 그래도 이번 기회에 datetime 이란 모듈이 있구나~ 라는 정도 알 수 있게 되었다. 그래도 datetime 덕분에 직접 시간(분)을 계산하는 것보다 코드 짜는데에 좀더 수월하고 쉬웠던 것 같다. 잘 알아두었다가 다음에 필요할 때 또 써보자.

################################################################### 다른 방법으로 푼 코드 ##########################################################################
'''
import math

car_list = {}
how_long = {}
cost = {}

def cal(time, car, what):
    if what == "IN":
        car_list[int(car)] = time
    else:
        in_h, in_m = car_list[int(car)].split(":")
        out_h, out_m = time.split(":")
        
        in_time = int(in_h) * 60 + int(in_m)
        out_time = int(out_h) * 60 + int(out_m)
        
        minutes = out_time - in_time
        del car_list[int(car)]
        
        return minutes
        
def solution(fees, records):
    park_min, pay, plus_min, plus_pay = fees
    for e in records:
        time, car, what = e.split()
        if what == "IN":
            if int(car) not in how_long:
                how_long[int(car)] = 0
            cal(time, car, what)
        else:
            minutes = cal(time, car, what)
            how_long[int(car)] += minutes
    
    if car_list != {}:
        for car, v in car_list.items():
            out_time = 23 * 60 + 59
            in_h, in_m = car_list[int(car)].split(":")
            
            in_time = int(in_h) * 60 + int(in_m)
            minutes = out_time - in_time
            
            how_long[int(car)] += minutes
    
    for car, minutes in how_long.items():
        if minutes <= park_min:
            cost[int(car)] = pay
        else:
            payment = pay + math.ceil((minutes - park_min) / plus_min) * plus_pay
            cost[int(car)] = payment
    
    opop = list(cost.keys())
    opop.sort()
    
    answer = []
    for e in opop:
        answer.append(cost[e])
    return answer
'''
#####################################################################################################################################################
