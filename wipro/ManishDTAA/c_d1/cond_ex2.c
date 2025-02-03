#include <stdio.h>
int main()
{
	int a=5,b=7,c=0,d,e;
	e=d=(c==0)?(a=10):(b=10);
	printf("\na=%d b=%d c=%d d=%d e=%d\n",a,b,c,d,e);
	return 0;
}
