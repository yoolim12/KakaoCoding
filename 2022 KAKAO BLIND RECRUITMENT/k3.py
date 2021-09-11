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
print(cost)