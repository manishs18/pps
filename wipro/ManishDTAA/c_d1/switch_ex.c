#include <stdio.h>
int main()
{
	int ch;
	printf("Enter a number in range 1-3-");
	scanf("%d",&ch);
	switch(ch)
	{
		default: printf("\nInvalid choice\n");
			 break;
		case 1:printf("\nMonday\n");
		       break;
		case 2:printf("\nTuesday\n");
		       break;
		case 3:printf("\nWednesday\n");
		       break;
	}
}

