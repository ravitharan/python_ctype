#include <math.h>

int foo(double *angle,
        int count,
        double *dst_sin,
        double *dst_cos)
{
    int i;

    for (i=0; i<count; i++) {
        dst_sin[i] = sin(angle[i]);
        dst_cos[i] = cos(angle[i]);
    }
    return 0;
}

