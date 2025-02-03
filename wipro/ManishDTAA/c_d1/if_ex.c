#include <stdio.h>
int main()
{
	int num1,num2;
	printf("Enter 2 numbers-");
	scanf("%d %d",&num1,&num2);
	if(num1>num2)
		printf("\n%d is big\n",num1);
	else if(num2>num1)
		printf("\n%d is big\n",num2);
	else
	{
		printf("\n%d %d\n",num1,num2);
		printf("\nBoth are equal\n");
	}
}

