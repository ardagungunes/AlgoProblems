#include <iostream>
#include <vector>
#include <cmath>
#include <bits/stdc++.h>

using namespace std;



int main() {

    int n;

    cin>>n;
    cin.ignore();


    for(int i = 0; i < (int) pow(2,n); i++){

        int num = i;
        string binary;


            while (num != 0) {
                //cout << num << endl;

                binary += to_string(num % 2);

                num = num / 2;

            }

            while(binary.size() != n){

                binary+='0';


            }

            reverse(binary.begin(), binary.end());

        cout << binary << endl;

        }


    return 0;
}

