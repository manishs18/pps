#include <stdio.h>
int main()
{
	int a=10,b=20,c=30;
	int d;
	d=(a++,++b,a++)+(++c,c++,c++);
	printf("d is %d\n",d);
}
