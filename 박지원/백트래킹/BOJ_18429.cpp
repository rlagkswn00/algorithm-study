#include <bits/stdc++.h>
using namespace std;

int N, K;
int arr[9];
int result = `0;
void cal2(vector<int> vec)
{
    int hp = 500;
    for (int i=0;i<vec.size();i++){
        hp=hp-K+arr[vec[i]];
        if(hp<500)
            return;
    }
    result++;
    return;
}
void cal(vector<int> vec, int visited[9])
{
    if (vec.size() == N)
    {
        cal2(vec);
        return;
    }
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] != 0)
            continue;

        vector<int> new_vec;
        for (int j = 0; j < vec.size(); j++)
        {
            new_vec.push_back(vec[j]);
        }
        new_vec.push_back(i);

        int new_visited[9] = {0};
        for (int j = 0; j <= 8; j++)
        {
            new_visited[j] = visited[j];
        }
        new_visited[i]=1;

        cal(new_vec, new_visited);
    }
}

int main()
{

    cin >> N >> K;
    for (int i = 1; i <= N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 1; i <= N; i++)
    {
        int visited[9] = {0};
        visited[i] = 1;
        vector<int> vec;
        vec.push_back(i);
        cal(vec, visited);
    }
    cout<<result;
    return 0;
}
