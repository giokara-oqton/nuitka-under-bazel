import argparse
import contextlib
import io
import os
import sys

import piptools.scripts.compile  # pylint: disable=import-error # type: ignore

def generate_requirements_lock(requirements_file: str, requirements_raw_lock_file: str):
    stderr = io.StringIO()
    with contextlib.redirect_stderr(stderr):
        try:
            piptools.scripts.compile.cli.main(args=[
                '--allow-unsafe',
                '--generate-hashes',
                f'--output-file={requirements_raw_lock_file}',
                requirements_file,
            ],
                                              prog_name='root')
        except SystemExit as ex:
            exit_code = ex.code
            if not isinstance(exit_code, int) or exit_code != 0:
                if stderr.getvalue():
                    print(stderr.getvalue())
                raise RuntimeError(f'Failed to generate requirements lock! Reason: {ex}.') from ex


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--requirements_file', type=str, required=True)
    parser.add_argument('--requirements_lock_file', type=str, required=True)
    args = parser.parse_args()

    if 'BUILD_WORKSPACE_DIRECTORY' not in os.environ:
        sys.exit("""
Please run this app as a Bazel target:

bazel run //build_tools:python_requirements
        """)

    if not os.path.exists(args.requirements_file):
        sys.exit('The input requirements file does not exist!')

    workspace_dir = os.environ['BUILD_WORKSPACE_DIRECTORY']
    requirements_raw_lock_file = os.path.join(workspace_dir, 'requirements_raw_lock.txt')
    if os.path.exists(requirements_raw_lock_file):
        os.remove(requirements_raw_lock_file)

    requirements_lock_file = os.path.join(workspace_dir, args.requirements_lock_file)
    if not os.path.exists(requirements_lock_file):
        sys.exit('The requirements lock file does not exist!')

    generate_requirements_lock(args.requirements_file, requirements_raw_lock_file)
    os.remove(requirements_raw_lock_file)


if __name__ == '__main__':
    main()
