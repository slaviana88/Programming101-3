#include "List.h"

#include<iostream>
#include<string>
#include<cstring>

using namespace std;

int main()
{
	List<int> list1;
	list1.push_front(100);
	list1.push_front(200);
	list1.push_front(300);
	list1.push_back(777);
	cout << list1.back() << endl; //777
	list1.pop_back();
	cout << list1.back() << endl; //100
	cout << list1.front() << endl; //300
	list1.pop_front();
	cout << list1.front() << endl; //200

	List<int> list2;
	list2.push_back(616);
	list2.push_front(515);
	list2.push_front(313);
	list2.push_back(777);
	//Извежда 313 515 616 777
	for (List<int>::Iterator it = list2.begin(); it != list2.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
	List<string> list3;
	list3.push_back("vidi");
	list3.push_back("vici");
	List<string>::Iterator iter = list3.begin();
	list3.insert(iter, "Veni");
	//Извежда Veni vidi vici
	for (List<string>::Iterator it = list3.begin(); it != list3.end(); it++)
	{
		cout << *it << " ";
	}
	cout << endl;
	List<string> list4;
	system("pause");
	
	return 0;
}