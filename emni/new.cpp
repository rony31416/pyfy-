#include<bits/stdc++.h>
using namespace std;

int main()
{

    vector<int> v;

    for (int i = 1000; i <= 99999; i++)
    {
        string s = to_string(i);
        set<char> digits(s.begin(), s.end());

        // for(auto u : digits){
        //     cout<<u<<" ";
        // }
        if (i <= 9999)
        {
            if (digits.size() == 4)
            {
                v.push_back(i);
            }
        }
        else
        {
            if (digits.size() == 5)
            {
                v.push_back(i);
            }
        }
    }
        // cout<<"hello";

        // for(int i = 0 ; i < v.size() ; i++){
        //     cout<<v[i] << "\n";
        // }

        cout<<v.size() << "\n";

        return 0;
    }

