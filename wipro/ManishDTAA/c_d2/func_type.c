#include <stdio.h>
void first();//without arg and without ret value
void second(int,int);// with aarg without ret value
int  third();// without  arg with ret value
int  fourth(int,int);// with  arg with ret value
int main()
{
	first();// caall to first()
	second(10,20); //call to second()
	int var=third();//call to third() 
	printf("\n var is - %d\n",var);
	var=fourth(fourth(100,200),fourth(10,20)); // call to fourth function
	printf("\n var is - %d\n",var);
	return 0;
}
void first()  //function definition
{
	printf("\nI am a function without arg or ret val\n");
}
void second(int n1, int n2)
{
	printf("\nResult of multiplication is %d\n",n1*n2);
}

int third()
{
	int n1=40,n2=50;
	return n1+n2;
}

int fourth(int n1, int n2)
{
	return n1-n2;
}
