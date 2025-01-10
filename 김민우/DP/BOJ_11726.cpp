#include <bits/stdc++.h>

using namespace std;

int arr[1005];

int main() {
    int n;
    cin >> n;
    
    arr[1] = 1;
    arr[2] = 2;
    
    for(int i=3; i<=n; i++) {
        arr[i] = (arr[i-1] + arr[i-2]) % 10007;
    }
    
    cout << arr[n];
}