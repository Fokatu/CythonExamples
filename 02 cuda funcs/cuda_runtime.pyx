cdef extern from "<stdint.h>" nogil:
    ctypedef ssize_t intptr_t
    ctypedef  size_t uintptr_t

cdef extern from "cuda_runtime.h":
    int cudaMalloc(void** devPtr, size_t size)
    int cudaMemcpy(void* dst, const void* src, size_t count,
                   int kind)

cpdef intptr_t malloc(size_t size):
    cdef void* ptr
    status = cudaMalloc(&ptr, size)
    return <intptr_t>ptr

cpdef memcpy(intptr_t dst, intptr_t src, size_t size, int kind):
    status = cudaMemcpy(<void*>dst, <void*>src, size, kind)