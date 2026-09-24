---
trigger: always_on
description: "Always-on testlib usage policy including the mandatory angle-bracket include form."
---
# OJ Testlib Convention

For direct C++ generator/validator/checker code using testlib, the include MUST be:

```cpp
#include <testlib.h>
```

Never use `#include "testlib.h"`.

Use deterministic seeds/parameters for reproducible generation.
