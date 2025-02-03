#include <stdio.h>
int main()
{
	register int num1=5;
	{
		int num=10;
		printf("\nnum1=%d\n",num1);
		printf("\nnum=%d\n",num);

	}
	num1=num1+10;
	printf("\nnum1=%d\n",num1);
	return 0;
}
