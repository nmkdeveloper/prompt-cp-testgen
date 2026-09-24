# testlib dependency

This bundle requires `testlib.h` for applicable C++ generators, validators and checkers but intentionally does not vendor a frozen arbitrary upstream snapshot.

Use the official testlib project/source approved by your environment, place `testlib.h` in a known include directory, and set `TESTLIB_INCLUDE_DIR`.

Official project: https://github.com/MikeMirzayanov/testlib

The OJ Test Engineering rules require the generated source code to include the header as:

```cpp
#include <testlib.h>
```

not with quoted includes.
