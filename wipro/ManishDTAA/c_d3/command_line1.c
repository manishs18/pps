#include <stdio.h>
#include <stdlib.h>
int main(int ac, char *av[])
{
	if(ac!=4)
	{
		printf("\nInvalid no, of arguements\n");
		return 1;
	}

	printf("\nResult is %d\n",atoi(av[1])+atoi(av[2])+atoi(av[3]));
	return 0;
}
