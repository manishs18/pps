#include <stdio.h>
int main()
{
	int *ptr;
	{
		int var=100;
		ptr=&var;
	}
		printf("\nvar=%d\n",*ptr);
	return 0;
}
