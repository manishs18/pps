#include <stdio.h>
int main()
{
	static int i=3;
	if(--i)
	{
		main();
		printf("\n%d\n",i);
	}
}
