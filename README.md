PyHeatshrink
===========

Python binding to the [heatshrink library](https://github.com/atomicobject/heatshrink).

*Supported versions:*  
  
Python >= 2.6

Usage
=====

The encoder accepts any object that implements the buffer protocol
and returns a memoryview containing unsigned bytes.
```
>>> import heatshrink
>>> mem = heatshrink.encode('a string')
>>> type(mem)
<type 'memoryview'>
>>> mem.tobytes()
'\xb0\xc8.wK\x95\xa6\xddg'
>> mem.format
'B'
```

The decoder accepts a memoryview and returns a byte representation of
the decoded data.
```
>>> import heatshrink
>>> mem = memoryview(b'\xb0\xc8.wK\x95\xa6\xddg')
>>> heatshrink.decode(mem)
'a string'
```

Testing
=======

CMake + CMocka is used for generating unit tests. To build run:
```
$ mkdir build && cd build
$ cmake ..
$ make
$ make test
```

License
=======

[ISC license](LICENSE)