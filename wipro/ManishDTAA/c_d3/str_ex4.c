#include <stdio.h>
#include <string.h>
int main()
{
	char str1[20],str2[20];
	printf("Enter two strings-");
	scanf("%s %s", str1,str2);
	int n=strcmp(str1,str2);
	printf("\n n is=%d\n",n);
	if(n>0)
		printf("\nFirst string %s is big\n",str1);
	else if(n<0)
		printf("\nSecond string %s is big\n",str2);
	else
		printf("\n %s and %s are equal\n",str1,str2);
	return 0;
}

