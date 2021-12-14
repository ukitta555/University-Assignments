#include <iostream>
using namespace std;

int sizeOfInt () 
{
	int i = 1;
	int counter = 1;
	while (i > 0)
	{
		i <<= 1 ;
		counter++;
	}
	return counter;
}

int main ()  
{
	return sizeOfInt();
}