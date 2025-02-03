#include <stdio.h>
int main()
{
	int a=5;
	printf("%d %d %d %d %d\n",++a,a++,++a,a++,a++);
	a=5;
	printf("%d\n",a++,"%d\n",++a,"%d\n",a++);
	a=5;
	printf("%d %d %d\n",a++,"%d\n",++a,"%d\n",a++);
}

