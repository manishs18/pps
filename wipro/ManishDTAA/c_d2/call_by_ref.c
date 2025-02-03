#include <stdio.h>
void change(int *,int *);

int main()
{
	int v1=10,v2=20;
	printf("\nBefoe function call v1=%d v2=%d\n",v1,v2);
	change(&v1,&v2); // call by value
	printf("\nAfter function call v1=%d v2=%d\n",v1,v2);
	return 0;
}

void change(int *v1, int *v2)
{
	*v1+=5;
	*v2+=5;
	printf("\nInside change function  v1=%d v2=%d\n",*v1,*v2);
}
