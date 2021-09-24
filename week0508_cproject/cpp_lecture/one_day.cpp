#include <iostream>
#include <algorithm>

using namespace std;

int dp[1001][3];
int rgb[1001][3];

int main()
{
    int N;
    cin >> N;
    
    for (int i=1; i<=N; i++)
    {
        for (int j=0; j<3; j++)
        {
            cin >> rgb[i][j];
        }
    }

    int ans = 1000*1000+1;

    for (int i=0; i<=2; i++)
    {
        for (int j=0; j<=2; j++)
        {
            if (i==j)
            {
                dp[1][j] = rgb[1][j];
            }
            else
            {
                dp[1][j] = 1000*1000+1;
            } 
        }

        for (int k=2; k<=N; k++)
        {
            dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + rgb[k][0];
            dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + rgb[k][1];
            dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + rgb[k][2];
        }

        for (int j=0; j<=2; j++) {
            if (i==j)
            {
                continue;
            }
            ans = min(ans, dp[N][j]);
        }
    }

    cout << ans << endl;
    return 0;
}