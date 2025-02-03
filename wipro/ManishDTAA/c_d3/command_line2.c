#include <stdio.h>
#include <stdlib.h>
int main(int ac, char *av[])
{
	if(ac<2)
	{
		printf("\nInvalid no, of arguements\n");
		return 1;
	}
	int sum=0;
	for(int i=1;i<ac;i++)
	{
		sum=sum+atoi(av[i]);
	}

	printf("\nResult is %d\n",sum);
	return 0;
}
