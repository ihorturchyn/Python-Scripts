#!/usr/bin/env python
import platform

profile = [
    platform.architecture(),
    platform.dist(),
    platform.libc_ver(),
    platform.platform(),
    platform.processor(),
    platform.python_build(),
    platform.python_compiler(),
    platform.python_version(),
    platform.system(),
    platform.uname(),
    platform.version(),
]

for line in profile:
    print(line)