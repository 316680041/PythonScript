//sample C file to add 2 numbers - int and floats

#include <stdio.h>

int test()  
{  
    int a = 10, b = 5;  
    return a+b;  
} 

int main()
{
	printf("---start---\n");
	int num = test();
	printf("num=%d\n",num);
	printf("---end---");
}