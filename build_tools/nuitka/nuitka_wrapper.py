import os
import runpy

if 'BUILD_WORKING_DIRECTORY' in os.environ:
    os.chdir(os.environ['BUILD_WORKING_DIRECTORY'])
    print(f"WORKING directory: {os.environ['BUILD_WORKING_DIRECTORY']}")

import sys

os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin' + os.pathsep + os.getenv('PATH', '')
print('PATH', os.getenv('PATH', ''))
print('sys.prefix:', sys.prefix)

if __name__ == '__main__':
    runpy.run_module('nuitka', run_name='__main__')
