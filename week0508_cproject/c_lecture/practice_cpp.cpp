#include <iostream>
#include <algorithm>

using namespace std;
long long dp[91];

int main() {

    int n;
    cin >> n;

    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;

    for (int i=4; i<=90; i++) {
        int temp = 0;
        for (int j=0; j<=i-2; j++) {
            temp += dp[j];
        }
        dp[i] = temp;
    }

    cout << dp[n] << endl;

    return 0;
}











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