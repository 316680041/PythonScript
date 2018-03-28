#include <iostream>  
using namespace std;

class Test
{
	public :int add_int(int num1, int num2) {
		return num1 + num2;
	}

	public :float add_float(float num1, float num2) {
		return num1 + num2;
	}

};

extern "C" {
	Test testObj;
	void add_int(int num1,int num2) {
		testObj.add_int(num1, num2);
	}
	void add_float(float num1, float num2) {
		testObj.add_float(num1, num2);
	}
}
