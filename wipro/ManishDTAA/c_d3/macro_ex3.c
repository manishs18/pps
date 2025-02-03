#include <stdio.h>
#define CALC(a,b,c) a+b-c
int main()
	{
		int x=5,y=6,z=7;
		printf("\n%d\n", CALC(x,y,z)*CALC(z,x,y));
	}
