#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main()
{
    //bool flag=1;
    while (1)
    {
        int rollFrequency, a, b;
        cout << "roll frequency?";
        cin >> rollFrequency;
        cout << "[a,b]:";
        cin >> a >> b;
        srand((unsigned)time(NULL));
        for (int i = 0; i < rollFrequency; i++)
        {
            cout << (rand() % (b - a + 1)) + a << endl;
        }
    }
    system("pause");
    return 0;
}