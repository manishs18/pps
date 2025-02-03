#include <stdio.h>
//#define X
int main()
{
#ifdef X
	printf("\nHello\n");
	printf("\nStudents\n");
#else
	printf("\nWipro\n");
	printf("\nClasses\n");
#endif
}

