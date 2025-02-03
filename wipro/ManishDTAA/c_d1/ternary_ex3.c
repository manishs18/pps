#include <stdio.h>
int main()
{
	int a=10,b=12,c,d,e;
	e=d=(c=1)?(a=15):(b=15);
	printf("\na=%d b=%d c=%d d=%d e=%d\n",a,b,c,d,e);
}
