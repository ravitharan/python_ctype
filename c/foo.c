#include <stdio.h>
#include <stdint.h>

struct parameter_t {
  int count;
  void *input;
  void *output;
};

int foo(struct parameter_t *param)
{
  int32_t *in_ptr = (int32_t *)param->input;
  float *out_ptr = (float *)param->output;
  int i, count = param->count;

  for (i=0; i<count; i++) {
    out_ptr[i] = 0.5 * in_ptr[i];
  }

  return 0;
}
