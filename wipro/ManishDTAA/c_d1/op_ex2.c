#include <stdio.h>
int main()
{
	int x=5,y=6,z=7,r;
	r=(x++,y++,++z)-(z+x,x++,x+y);
	printf("\nz=%d\n",r);
	return 0;
}
