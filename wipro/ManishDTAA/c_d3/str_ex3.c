#include <stdio.h>
#include <string.h>
int main()
{
	char str1[20]="HELLO there ", str2[20]="ALL",str3[20]="WIPRO";
	printf("\nfor string1 strlen=%lu  sizeof=%lu\n",strlen(str1),sizeof("hello"));
	printf("\nstr1=%s  str2=%s   str3=%s\n",str1,str2,str3);
	strcpy(str2,str1);
	printf("\nstr1=%s  str2=%s   str3=%s\n",str1,str2,str3);
	strcat(str2,str3);
	printf("\nstr1=%s  str2=%s   str3=%s\n",str1,str2,str3);
	return 0;
}
