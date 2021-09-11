dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}

def solution(s):
    num_letter = '' # "o" + "n" + "e" 과 같이 문자 하나하나 붙여서 숫자를 의미하는 단어 만들기
    ans_str = '' # 정답을 우선 str 형태로 받기(숫자 하나하나 뒤에 붙이기 쉽게)

    for letters in s: # 숫자 형태의 str
        if letters in "0123456789":
            ans_str += letters
        else: # 문자 형태의 str
            num_letter += letters

            if num_letter in dict:
                ans_str += dict[num_letter]
                num_letter = ''

    answer = int(ans_str)
    return answer


###################################### 마음에 들었던 다른 분의 풀이 1 ###########################################
'''
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''
# comment : 이 분은 이렇게 replace 함수를 통해 코드를 간결하게 하여 답을 구했다. 나처럼 하나하나 글자를 비교하면서 붙이고 비교하는 작업을 거치는 것보다 훨씬 구하는 과정도 간결해보여 마음에 들었다. replace 함수를 많이 애용하도록 하자.
#################################################################################################################



###################################### 마음에 들었던 다른 분의 풀이 2 ###########################################
'''
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
'''
# comment : 위 분과 크게 다를 바는 없는 것 같다. 나는 이 풀이를 풀 때 딕셔너리만 떠올랐는데 이렇게 리스트로도 구현할 수 있다는 점.
#################################################################################################################
