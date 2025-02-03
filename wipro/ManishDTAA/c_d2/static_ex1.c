#include <stdio.h>
void show();//prototype

int main()
{
	show();
	show();
	show();
}

void show()
{
	static int num=10;
	num++;
	printf("\nNum is %d\n",num);
}
