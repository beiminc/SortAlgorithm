#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

void print_array(auto array)
{
    for(int i : array)
    {
        cout << i << " ";
    }
    cout << endl;
}

void insertion_sort(auto &array)
{
    auto len = array.size();
    int k = 0;
    for (int i = 1; i < len; i++)
    {
        if (array[i] < array[i-1])
        {
            for (int j = i; j > 0; j--)
            {
                if (array[j] < array[j-1])
                {
                    auto temp = array[j-1];
                    array[j-1] = array[j];
                    array[j] = temp;
                }
            }
            cout << "after " << ++k << " change: ";
            print_array(array);
        }
    }
}

int main()
{  
    vector<int> array;
    char ch;
    cout << "please input the array(split by space):";
    while((ch = cin.get()) != '\n')
    {
        if(ch != ' ')
            array.push_back(int(ch - '0'));
    }
    cout << "origin is: " ;
    print_array(array);

    insertion_sort(array);
    cout << "result is: " ;
    print_array(array);

    system("pause");
    return 0;
}