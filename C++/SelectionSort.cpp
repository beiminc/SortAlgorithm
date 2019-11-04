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

void selection_sort(auto &array)
{
    auto len = array.size();
    for (int i = 0; i < len; i++)
    {
        int key = i;
        for(int j = i+1; j < len; j++)
        {
            if(array[j] < array[key])
            {
                key = j;
            }
        }
        if(key != i)
        {
            int temp = array[i];
            array[i] = array[key];
            array[key] = temp;
        }

        cout << "after " << i + 1 << " change: ";
        print_array(array);
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

    selection_sort(array);
    cout << "result is: " ;
    print_array(array);

    system("pause");
    return 0;
}