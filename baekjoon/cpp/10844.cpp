// 쉬운 계단 수 / 10844.py
// 출처: 
// 알고리즘 분류: 다이나믹 프로그래밍

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    long long dp[1001][10];
    dp[0][0]=0;
    for (int i=1; i<10;i++)
        dp[0][i]=1;
    for (int i=1; i<1000;i++){
        for (int j=0;j<10;j++){
            if (j==0) dp[i][j]=dp[i-1][j+1]% 1000000000;
            else if (j==9) dp[i][j]=dp[i-1][j-1]% 1000000000;
            else dp[i][j]=(dp[i-1][j+1]+dp[i-1][j-1])% 1000000000;
        }
    }
    long long ans=0;
    for(int i=0; i<10;i++) ans+=dp[n-1][i];
    cout << ans%1000000000;
}