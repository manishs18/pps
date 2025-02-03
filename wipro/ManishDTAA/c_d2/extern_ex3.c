#include <stdio.h>
void show();// prototype of show function
int main()
{
	extern int var;  //extern declaration
	printf("\nIn main var is %d\n",var);
	show(); // function call
}
int var=10;

void show()
{
	printf("\nIn show var is %d\n",var);
}

