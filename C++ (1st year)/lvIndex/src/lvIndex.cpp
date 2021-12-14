//============================================================================
// Name        : lvIndex.cpp
// Author      : Vlad
// Version     :
// Copyright   : A project that is too secret to show to anybody
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;


long long lvIndex (int axes, ...)
{
	int *pijk = &axes;
	for (int i = 0; i <= axes+10; i+=1)
	{
		cout << pijk[i] << ' ';
	}
	axes = 12;
	pijk = &axes;
	cout << endl;
	for (int i = 0; i <= axes+10; i+=1)
	{
		cout << pijk[i] << ' ';
	}
	return 1;
}


int main() {
	lvIndex(2, 125, 3);
	return 0;
}

