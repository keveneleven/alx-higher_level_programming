#include <Python.h>
/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	const char *str;

	if (PyUnicode_Check(p))
	{
		str = PyUnicode_AsUTF8(p);
		if (str != NULL)
		{
			printf("'%s'\n", str);
		}
		else
		{
			PyErr_Print();
		}
	}
	else
	{
		PyErr_Print();
	}
}

