// 피보나치 수 3 / 2749.py
// 출처: 
// 알고리즘 분류: 수학, 분할 정복을 이용한 거듭제곱

#include <iostream>
using namespace std;
const int mod = 1000000;
const int p = mod/10*15;
int fibo[p] = {0,1};
int main() {
    long long n;
    cin >> n;
    for (int i=2; i<p; i++) {
        fibo[i] = fibo[i-1] + fibo[i-2];
        fibo[i] %= mod;
    }
    cout << fibo[n%p] << '\n';
    return 0;
}