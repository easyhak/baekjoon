// 연속합 / 1912.cpp
// 출처: 
// 알고리즘 분류: 다이나믹 프로그래밍
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    int arr[100001];
    int dp[100001];
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    int ans=arr[0];
    dp[0]=arr[0];
    for (int i=1;i<n;i++){
        dp[i]=max(dp[i-1]+arr[i],arr[i]);
        ans=max(dp[i],ans);
    }
    cout << ans;
    
}