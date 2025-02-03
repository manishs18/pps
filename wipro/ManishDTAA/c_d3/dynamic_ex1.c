#include <stdio.h>
#include <stdlib.h>
int main()
{
	double *p;
	p=(double *) malloc(sizeof(double));
	printf("Enter a double value=");
	scanf("%lf",p);
	printf("The value input is %lf\n",*p);
	return 0;
}
