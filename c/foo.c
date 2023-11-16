#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

#define FILE_PATH_LEN       256

struct parameter_t {
  char shm_file[FILE_PATH_LEN];
  int count;
  float multiplier;
};


int foo(struct parameter_t *param)
{
  uint8_t *shm_buf;
  int32_t *in_data;
  float *out_data;
  int i, fd, ret = -1;
  size_t pos, in_size, out_size, total_size;
  int count = param->count;
  float multiplier = param->multiplier;

  in_size = count * sizeof(*in_data);
  out_size = count * sizeof(*out_data);
  total_size = in_size + out_size;

  fd = shm_open(param->shm_file, O_RDWR, 0);
  if (fd == -1) {
    perror("shm_open()");
    goto exit;
  }

  /* Map the object into the caller's address space. */
  shm_buf = mmap(NULL, total_size, PROT_READ | PROT_WRITE,
                 MAP_SHARED, fd, 0);
  if (shm_buf == MAP_FAILED) {
    perror("mmap");
    goto exit;
  }

  pos = 0;
  in_data = (typeof(in_data))&shm_buf[pos];

  pos += in_size;
  out_data = (typeof(out_data))&shm_buf[pos];

  for (i=0; i<count; i++) {
    out_data[i] = multiplier * in_data[i];
  }

  munmap(shm_buf, total_size);

  ret = 0;

exit:
  close(fd);

  return ret;
}

