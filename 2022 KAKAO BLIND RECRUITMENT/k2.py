from collections import deque
import math

dq = deque()

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        for el in range(2,int(math.sqrt(n))+1):
            if n % el == 0:
                return False
    return True
    

def solution(n, k):
    cnt = 0
    while n != 0:
        dq.appendleft(str(n%k))
        n = n // k
    
    changed = "".join(list(dq))

    for i in range(len(changed)):
        if i != 0 and i != len(changed)-1 and changed[i] == '0':
            changed = changed.replace(changed[i], " ")

    num_list = changed.split()

    for e in num_list:
        if is_prime(int(e)):
            cnt += 1
    
    answer = cnt
    return answer