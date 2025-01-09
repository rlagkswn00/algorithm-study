#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

int N, M;
int arr[1001][1001];
int visited[1001][1001][2] = {0};
int x[4] = {0, 0, -1, 1};
int y[4] = {-1, 1, 0, 0};
queue<int> que1;
queue<int> que2;
queue<int> que3;
queue<int> que4;

int bfs() {
    que1.push(1);
    que2.push(1);
    que3.push(1);
    que4.push(0);
    int result=-1;
    while (!que1.empty()) {
        int row = que1.front();
        que1.pop();
        int col = que2.front();
        que2.pop();
        int day = que3.front();
        que3.pop();
        int indent = que4.front();
        que4.pop();
        if (visited[row][col][indent] != 0||result>=0)
            continue;
        visited[row][col][indent] = 1;
        if(row==N&&col==M){
            result=day;
            continue;
        }
        for (int i = 0; i < 4; i++) {
            int new_row = row + x[i];
            int new_col = col + y[i];
            if (new_row <= 0 || new_row > N)
                continue;
            if (new_col <= 0 || new_col > M)
                continue;
            if (arr[new_row][new_col] == 1 && indent == 1)
                continue;
            que1.push(new_row);
            que2.push(new_col);
            que3.push(day+1);
            que4.push(indent+arr[new_row][new_col]);
        }

    }
    return result;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        string str;
        cin>>str;
        for (int j = 1; j <= M; j++) {
            arr[i][j]=str[j-1]-'0';
        }
    }
    cout << bfs();


    return 0;
}

