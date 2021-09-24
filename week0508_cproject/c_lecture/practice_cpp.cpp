#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int findIndex(const vector< vector <int> > &arr, vector<int> item) {

    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == item)
            return i;
    }

    return -1;
}

int main() {
    int m = 4;
    int n = 3;

    vector<int> puddle;
    puddle.push_back(2);
    puddle.push_back(2);
    vector< vector <int> > puddles;
    puddles.push_back(puddle);

    // 방문 체크 생성
    vector< vector <int> > visited;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            visited[j][i] = 0; 
        }
    }

    // 이동 가능 경로 생성
    int dx[2], dy[2];
    for (int i=0; i<=1; i++) {
        dx[i] = i;
        dy[i] = i;
    }

    vector<int> init;
    init.push_back(1);
    init.push_back(1);
    vector< vector<int> > queue;
    queue.push_back(init);

    while (queue.size() != 0) {
        vector<int> temp;
        temp = queue.back();
        queue.pop_back();

        if (visited[temp[0]][temp[1]] != 0 && temp[0] != m && temp[1] != n) {
            continue;
        }

        visited[temp[0]][temp[1]] += 1;

        
        vector<int> index1;
        index1.push_back(temp[1]+1);
        index1.push_back(temp[0]);

        if (findIndex(puddles, index1) != 0) {
            queue.push_back(index1);
        }

        vector<int> index2;
        index2.push_back(temp[1]+1);
        index2.push_back(temp[0]);

        if (findIndex(puddles, index2) != 0) {
            queue.push_back(index2);
        }


    }

    
    cout << visited[m][n] << endl;
    
    return 0;
}







// int u, v, n;
// double cnt, w;
// int a[500001];
 
// int main() {
//     cin >> n >> w;
//     for(int i = 1 ; i<=n-1; i++)
//     {
//         cin >> u >> v;
//         a[u]++;
//         a[v]++;
//     }
//     for (int i = 2; i <= n; i++)
//     {
//         if (a[i] == 1)
//         {
//             cnt++;
//         }
//         //cout << a[i] << ' ';
//     }
//     printf("%.10f", w / cnt);
    
// }


// int n, k;
// string a;
// vector<char> result;

// int main() {

//     cin >> n >> k >> a;

//     int i = 0;
//     while (i != a.size()) {
//         while (k != 0 && !result.empty() && result.back() < a[i]) {
//             result.pop_back();
//             k--;
//         }
//         result.push_back(a[i]);
//         i++;
//     }

//     while (k--) {
//         result.pop_back();
//     }

//     for (int i=0; i<result.size(); i++) {
//         cout << result[i];
//     }

 
//     return 0;
// }














// long long dp[91];

// int main() {

//     int n;
//     cin >> n;

//     dp[0] = 1;
//     dp[1] = 1;
//     dp[2] = 1;
//     dp[3] = 2;

//     for (int i=4; i<=90; i++) {
//         int temp = 0;
//         for (int j=0; j<=i-2; j++) {
//             temp += dp[j];
//         }
//         dp[i] = temp;
//     }

//     cout << dp[n] << endl;

//     return 0;
// }











// long long dist[100000];
// long long oil_price[100000];

// int main() {
//     int n;

//     cin >> n;
//     for (int i=0; i<n-1; i++) {
//         cin >> dist[i];
//     }
//     for (int i=0; i<n; i++) {
//         cin >> oil_price[i];
//     }

//     long long price = oil_price[0];
//     long long expense = 0;

//     for (int i=0; i<n-1; i++) {
//         expense += dist[i] * price;

//         if (oil_price[i+1] < price) {
//             price = oil_price[i+1];
//         }
//     }
    
//     cout << expense << endl;
//     return 0;
// }




// long long input_lst[1000];

// int main() {
//     int n, m;
//     long long temp;
//     long long sum = 0;
//     cin >> n >> m;

//     for (int i=0; i<n; i++) {
//         cin >> input_lst[i];
//     }
    
//     for (int i=0; i<m; i++) {
//         sort(input_lst, input_lst+n);
//         temp = input_lst[0] + input_lst[1];
//         input_lst[0] = temp;
//         input_lst[1] = temp;
//     }

//     for (int i=0; i<n; i++) {
//         sum += input_lst[i];
//     }

//     cout << sum << endl;
//     return 0;
// }