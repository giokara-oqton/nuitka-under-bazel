# Minimal example of running Nuitka under Bazel

This repo is inspired on the nice work already done [here](https://github.com/chaosct/bazel_nuitka_test). In this repo, we try to make nuitka binaries further available as dependencies for subsequent Bazel targets.
The goal of this repository is to compile Python targets created with [Bazel buildsystem](https://github.com/bazelbuild/bazel) into binary executables through the use of Nuitka.
This repo expects Bazel to be available, either through [Bazelisk](https://github.com/bazelbuild/bazelisk) or with [Bazel version 6.5.0](https://github.com/bazelbuild/bazel/releases/tag/6.5.0) installed.
It has been tested on Ubuntu 24.04.

## Testing the example

To run the `py_binary` target without Nuitka in order to check expected result, run

```bash
bazel run //src/test1:test1_main
```

To build a Nuitka binary, run

```bash
bazel build //src/test1:test1_nuitka_bin
```

The binary will be located under `bazel-bin/src/test1/test1_nuitka_bin` subdirectory.
In order to run it, please adjust the `LD_LIBRARY_PATH` to point to the Python libraries used by bazel, e.g.

```bash
export LD_LIBRARY_PATH="$HOME/.cache/bazel/_bazel_$USER/<hash of cache dir>/execroot/nuitka_under_bazel/external/python_3_10_x86_64-unknown-linux-gnu/lib:$LD_LIBRARY_PATH"
```

and then finally run the Nuitka-generated binary

```bash
./bazel-bin/src/test1/test1_nuitka_bin
```
