
CFLAGS = -Wall -Werror -fpic
LDFLAGS = -shared 

libfoo.so : foo.o
	$(CC) $(LDFLAGS) -o $@ $<

clean :
	rm -f *.o libfoo.so
