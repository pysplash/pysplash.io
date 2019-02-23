title: CPython Tests
slug: cpythontests
date: 2019-02-20 12:28:31 UTC-08:00
tags:
category: cpython
link:
description:
type: text

# Tests

## Running

Simplest:

    ./python.exe -m test

Single test file:

    ./python.exe -m test -v test_abc

Single test:

    ./python.exe -m unittest -v test.test_abc.TestABC

### Parallel testing on multi-core/multi-CPU

```bash
./python.exe -m test -j0
```

### Strenuous

Preferred:

```bash
./python.exe -bb -E -Wd -m test -r -w -uall
```

`-R` check for reference leaks (if C code modified) Ex. `-R 3:2`

Alternative:

Run `Tools/scripts/run_tests.py` script.

## Writing

- Tests in `Lib/test` directory
- Files `test_` prefix
