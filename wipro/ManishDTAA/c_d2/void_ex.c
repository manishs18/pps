#include <stdio.h>
int main()
{
	int num=10;
	int *ptr;
	ptr=&num;
	printf("\nnum is %d\n",num);
	*ptr=*ptr+5;
	printf("\nnum is %d\n",num);
}

