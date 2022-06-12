#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
    int rollFrequency,a,b;
    cout << "roll frequency?";
    cin >> rollFrequency;
    cout << "[a,b]";
    cin >> a >> b;
    srand((unsigned)time(NULL));
    for (int i = 0; i < rollFrequency; i++)
    {
        cout << (rand() % (b-a+1))+ a << endl;
    }
    
    return 0;
}