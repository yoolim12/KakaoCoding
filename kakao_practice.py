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

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))