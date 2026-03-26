// Includes the Python.h header file, which provides the Python C API.
#include <Python.h>

// Includes the standard input/output library for C.
#include <stdio.h>

// Defining C function that will be accessible from Python with 'self' and 'args' from Python.
static PyObject* py_hello(PyObject *self, PyObject *args) {

	// Print a message:
    printf("Hola Mundo desde el lenguaje C!\n");

    // No value to be returned. Returns a 'None' object.
    Py_RETURN_NONE;
}

// Method table for the module, mapping Python function to C functions.
static PyMethodDef HolaMetodos[] = {
	// py_hello -> A pointer to the C function that implements this Python function.
    {"hola",  py_hello, METH_NOARGS, "Print 'Hola Mundo desde el lenguaje C!."},
    // METH_NOARGS -> the function takes no arguments from Python.
    // Marking the end of the array of method definitions.
    {NULL, NULL, 0, NULL}
};

// Module structure: provides metadata about the Python module.
static struct PyModuleDef hola_modulo = {
	// Internal members of the module definition structure.
    PyModuleDef_HEAD_INIT,
    
    // Name of module
    "hola_modulo",
    
    // Module documentation, in this case NULL/  
    NULL,
    // -1 so the module keeps state in global variables
    -1,
    // Pointer to PyMethodDef structures defined earlier
    HolaMetodos
};

// Module initialization function, void for call from Python.
PyMODINIT_FUNC PyInit_hola_modulo(void) {
	// Creates and returns the Python module object based on the definition in 'hola_modulo'.
    return PyModule_Create(&hola_modulo);
}
