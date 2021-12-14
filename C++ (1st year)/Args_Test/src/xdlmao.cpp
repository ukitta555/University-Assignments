//============================================================================
// Name        : xdlmao.cpp
// Author      : Vlad
// Version     :
// Copyright   : A project that is too secret to show to anybody
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main(int argc, char **argv, char **envp) {
	cout << " ' " << argv[1] << " ' "<< endl;
	int *pc = &argc;
	void *pv= &argv;
	void *pv1 = &envp;
	cout << pc << ' ' << pv << ' ' << pv1 << " " << endl;
}
