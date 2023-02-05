# 쇠막대기 / 10799.py
# 출처: Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2015 > 중등부 2번
# 알고리즘 분류: 스택, 자료구조

s = input()
st = []
ans = 0

for i in range(len(s)):
    if s[i] == "(":
        st.append(1)
    else:
        if s[i-1] == "(":
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1
print(ans)