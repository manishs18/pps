#include <stdio.h>
int main()
{
	int arr[5];
	int *ptr;
	printf("Enter values into array");
	for(ptr=arr;ptr<arr+5;ptr++)
	{
		scanf("%d",ptr);
	}

	printf("\nContents of array-\n");
	for(ptr=arr;ptr<arr+5;ptr++)
	{
		printf("%3d",*ptr);
	}
	printf("\n");
	return 0;
}

