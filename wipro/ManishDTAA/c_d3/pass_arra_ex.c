#include <stdio.h>
void check_prime(int *, int);

int main()
{
	int arr[5];
	printf("Enter 5 int values into array-");
	for(int i=0;i<5;i++)
	{
		scanf("%d",&arr[i]);
	}
	//Passing the array at the time of function call as arg
	check_prime(arr,5);
	return 0;
}

void check_prime(int *p, int size)
{
	int newarr[size];
	for(int i=0;i<size;i++)
	{
		int flag=0;
		for(int  j=2;j<=p[i]/2;j++)
		{
			if(p[i]%j==0)
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			newarr[i]=p[i];
		else
			newarr[i]=0;
	}
	printf("\nArray with prime numbers\n");
	for(int i=0;i<size;i++)
	{
		printf("%3d",newarr[i]);
	}
	printf("\n");
}
