#include <stdio.h>
int main()
{
	int arr[3][4];
	for(int r=0;r<3;r++)
	{
		for(int c=0;c<4;c++)
		{
			printf("\nEnter value for row %d and col %d-",r+1,c+1);
			scanf("%d",*(arr+r)+c);
		}
	}
	for(int r=0;r<3;r++)
	{
		for(int c=0;c<4;c++)
		{
			printf("%3d",*(*(arr+r)+c));
		}
		printf("\n");
	}
}
