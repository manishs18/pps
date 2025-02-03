#include <stdio.h>
int main()
{
	int a=1,b=0,c=0;
	if(a++ || b++)
		printf("\nHello\n");
	else
		printf("\nHi\n");
	printf("\na=%d b=%d\n",a,b);
}
