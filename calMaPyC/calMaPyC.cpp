
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <stdio.h>
#include <numpy/arrayobject.h>

//#define DEBUG

void hello(const char* name)
{
	printf("Hello %s !\n", name);
}

static PyObject* py_hello(PyObject* self, PyObject* args)
{
	const char* name;
	if (!PyArg_ParseTuple(args, "s", &name))
		return NULL;
	hello(name);

	Py_INCREF(Py_None);
	return Py_None;
}

// calMaPyC(data,100)
// calMaPyC(np.array,int)
static PyObject* py_calMaPyC(PyObject* self, PyObject* args) {
#ifdef DEBUG	
	printf("enter py_calMaPyC\n");
#endif
	PyArrayObject* inputArray = NULL;
	PyObject* outputArray = NULL;
	int window;

	if (!PyArg_ParseTuple(args, "O!i", &PyArray_Type, &inputArray, &window))
		return NULL;
#ifdef DEBUG
	printf("Parse args succeed.\n");
#endif
	if (inputArray == NULL)
		return NULL;

	int nd = PyArray_NDIM(inputArray);
	npy_intp* dims = PyArray_DIMS(inputArray);
	outputArray = PyArray_SimpleNew(nd, dims, NPY_FLOAT64);
	if (outputArray == NULL)
		return NULL;

	int* pInput = (int*)PyArray_DATA(inputArray);
	double* pOutput = (double*)PyArray_DATA((PyArrayObject*)outputArray);

	int offset = window / 2;
	int len = (int)dims[0];

	if (len <= window) {
		for (int i = 0; i < len; i++) {
			pOutput[i] = 0;
		}
		Py_INCREF(outputArray);
		return outputArray;
	}

	for (int i = 0; i < offset; i++) {
		pOutput[i] = 0;
	}
	for (int i = len - offset + 1; i < len; i++) {
		pOutput[i] = 0;
	}
	int N = 2 * offset;
	long long sum = 0;
	for (int i = offset; i < len - offset + 1; i++) {
		sum = 0;
		for (int m = i - offset; m < i + offset; m++) {
			sum += pInput[m];
		}
		pOutput[i] = ((double)sum) / N;
	}

	Py_INCREF(outputArray);
	return outputArray;
}

static PyMethodDef calMaPyC_methods[] = {
	{ "hello", py_hello, METH_VARARGS, "Hello" },
	{ "calMaPyC", py_calMaPyC, METH_VARARGS, "calMaPyC" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef calMaPyC_module = {
	PyModuleDef_HEAD_INIT,
	"calMaPyC",
	NULL,
	-1,
	calMaPyC_methods
};

PyMODINIT_FUNC PyInit_calMaPyC(void)
{
	import_array();
	return PyModule_Create(&calMaPyC_module);
}

PyMODINIT_FUNC PyInit_calMaPyCG(void)
{
	import_array();
	return PyModule_Create(&calMaPyC_module);
}
