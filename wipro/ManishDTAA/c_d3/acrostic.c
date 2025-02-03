#include <stdio.h>
int main()
{
	char str[5][6];
	for(int i=0;i<5;i++)
	{
		printf("Enter string %d=",i+1);
		scanf("%s",str[i]);
	}
	int flag=0;
	for(int r=0;r<5;r++)
	{
		for(int c=0;c<5;c++)
		{
			if(str[r][c]!=str[c][r])
				flag=1;
		}
	}
	if(flag==0)
		printf("\nIts an acrostic\n");
	else
		printf("\nIts not an acrostic\n");

	return 0;
}
