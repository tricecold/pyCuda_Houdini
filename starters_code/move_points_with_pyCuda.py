node = hou.pwd()
geo = node.geometry()

import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy

string_buffer = geo.pointFloatAttribValuesAsString("P", float_type=hou.numericData.Float32)

a_gpu = gpuarray.to_gpu(numpy.fromstring(string_buffer, dtype='float32' ).reshape(-1, 3).astype(numpy.float32))
a_doubled = (1.2*a_gpu).get()
##print a_doubled
geo.setPointFloatAttribValuesFromString("P", numpy.getbuffer(a_doubled), float_type=hou.numericData.Float32)

