#include <stdio.h>
int main()
{
	char ch;
	printf("\nsize of char vriable- %lu\n",sizeof(ch));
	printf("\nsize of char const- %lu\n",sizeof('a'));
	printf("\nsize of int const- %lu\n",sizeof(100));
	printf("\nsize of long int  const- %lu\n",sizeof(10l));
	printf("\nsize of float const- %lu\n",sizeof(2.4f));
	printf("\nsize of double  const- %lu\n",sizeof(2.4));
	printf("\nsize of long double  const- %lu\n",sizeof(2.41234567123456789l));
	printf("\nsize of double  const- %lu\n",sizeof(2.4));
}
