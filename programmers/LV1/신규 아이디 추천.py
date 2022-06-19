# 신규 아이디 추천
# 출처: 2021 KAKAO BLIND RECRUITMENT

import re

def solution(new_id):
    answer = ''
    # 1단계 & 2단계
    answer = re.sub('[^\w\_\.-]', '', new_id.lower())
    
    # 3단계
    answer = re.sub('\.\.+', '.', answer)
    
    # 4단계
    answer = re.sub('^\.|\.$', '', answer)
    
    # 5단계
    if not answer:
        answer = 'a'
    
    # 6단계
    answer = re.sub('\.$', '', answer[0:15])
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1:]
    
    return answer