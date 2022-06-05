# 신고결과 받기
# 출처: 2022 KAKAO BLIND RECRUITMENT
def solution(id_list, report, k):
    
    report=list(set(report))
    answer_dict={}
    report_dict={}
    rans={}
    for i in id_list:
        answer_dict[i]=[]
        report_dict[i]=0
        rans[i]=0
    for x in report:
        a, b= x.split()
        report_dict[b]+=1
        answer_dict[a].append(b)
    for a,b in report_dict.items():
        if report_dict[a]>=k:
            for c in id_list:
                try:
                    if answer_dict[c].index(a)>-1:
                        rans[c]+=1
                except ValueError:
                    continue
    
    answer = list(rans.values())
    return answer