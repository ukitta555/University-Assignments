//============================================================================
// Name        : testStructcpp.cpp
// Author      : Vlad
// Version     :
// Copyright   : A project that is too secret to show to anybody
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

struct x
{
public:
	int i;
	int f()
	{
		return c4[0];
	};
private:
	char c4[4];
};

int main() {
	string s = "s0";
	cout << (int)s[-3000];
	return 0;
}
