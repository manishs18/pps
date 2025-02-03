#include <stdio.h>
int main()
{
	char str[4][10];
	for(int i=0;i<4;i++)
	{
		printf("Enter string %d=",i+1);
		scanf("%s",str[i]);
	}
	for(int i=0;i<4;i++)
	{
		printf("%s\n",str[i]);
	}
	return 0;
}
