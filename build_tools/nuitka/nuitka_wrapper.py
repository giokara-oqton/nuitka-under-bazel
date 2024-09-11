import os
import runpy

if 'BUILD_WORKING_DIRECTORY' in os.environ:
    os.chdir(os.environ['BUILD_WORKING_DIRECTORY'])
    print(f"WORKING directory: {os.environ['BUILD_WORKING_DIRECTORY']}")

import sys

print('sys.prefix:', sys.prefix)

if __name__ == '__main__':
    runpy.run_module('nuitka', run_name='__main__')
