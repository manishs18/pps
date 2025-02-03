#include <stdio.h>
int main()
{
	int num=10;
	void *ptr;
	ptr=&num;
	printf("\nnum is %d\n",num);
	* (int *)ptr=* (int *)ptr+5;
	printf("\nnum is %d\n",num);
}

