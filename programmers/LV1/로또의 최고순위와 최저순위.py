# 로또의 최고순위와 최저순위
# 출처: 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
def solution(lottos, win_nums):
    result_dict={"0":6,"1":6,"2":5,"3":4,"4":3,"5":2,"6":1}
    w_cnt,z_count=0,0
    for i in lottos:
        try:
            if i==0:
                z_count+=1
            if win_nums.index(i)>-1:
                w_cnt+=1
        except ValueError:
            continue
    return [result_dict[str(w_cnt+z_count)], result_dict[str(w_cnt)]]