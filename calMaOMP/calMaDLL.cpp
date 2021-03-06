#include <stdio.h>
#include <omp.h>

#ifdef _MSC_VER
#define DLL_EXPORT extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT extern "C" 
#endif

DLL_EXPORT void __stdcall hello(const char* name, int len)
{
	printf("Hello %s\n", name);
}

DLL_EXPORT void __stdcall calMaDLL(const int* in, double* out, int len, int window)
{
	int offset = window / 2;

	if (len <= window) {
		for (int i = 0; i < len; i++) {
			out[i] = 0;
		}
		return ;
	}

	for (int i = 0; i < offset; i++) {
		out[i] = 0;
	}
	for (int i = len - offset + 1; i < len; i++) {
		out[i] = 0;
	}
	int N = 2 * offset;
	long long sum = 0;
#pragma omp parallel for 
	for (int i = offset; i < len - offset + 1; i++) {
		sum = 0;
		for (int m = i - offset; m < i + offset; m++) {
			sum += in[m];
		}
		out[i] = ((double)sum) / N;
	}

    return ;
}

