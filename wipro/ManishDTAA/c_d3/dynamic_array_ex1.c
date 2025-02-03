#include <stdio.h>
#include <stdlib.h>
int main()
{
	int size;
	printf("Enter array size-");
	scanf("%d",&size);
	int *ptr;
	ptr=(int *)malloc(sizeof(int)*size);
	int *ptr1;
	printf("Enter values into array-");
	for(ptr1=ptr;ptr1<ptr+size;ptr1++)
	{
		scanf("%d",ptr1);
	}
	printf("\nDisplay array in reverse\n");
	for(ptr1=ptr+size-1;ptr1>=ptr;ptr1--)
	{
		printf("%3d",*ptr1);
	}
	printf("\n");
	return 0;
}

