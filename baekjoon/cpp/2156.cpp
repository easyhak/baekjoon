// 포도주 시식 / 2156.cpp
// 출처: 
// 알고리즘 분류: 다이나믹 프로그래밍
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    int arr[10001];
    int dp[10001];
    for (int i=1; i<=n; i++){
        cin >> arr[i];
    }
    dp[0]=arr[0];
    dp[1]=arr[1];
    dp[2]=arr[1]+arr[2];
    for (int i=3;i<=n;i++){
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i],max(dp[i-2]+arr[i],dp[i-1]));
    }
    cout << dp[n];
}