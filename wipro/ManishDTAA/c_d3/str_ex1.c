#include <stdio.h>
#include <string.h>
int main()
{
	char str[21];
	printf("Enter a string-");
	fgets(str,20,stdin);
	printf("\nString entered is %s\n",str);
	printf("\nprint the string vertically\n");
	for(int i=0;str[i]!='\0';i++)
	{
		printf("\n%c",*(str+i));
	}
	printf("\n");
	return 0;
}
