"""Defines rule to convert py_binary targets to nuitka binaries.
"""

load("@bazel_skylib//rules:run_binary.bzl", "run_binary")
load("//build_tools/nuitka:all_python_srcs.bzl", "all_python_srcs")

NUITKA_TOOL = "//build_tools/nuitka:nuitka"

def nuitka_binary(name, target, main):
    all_python_srcs(
        name = "{}_all_deps".format(name),
        target = target,
    )
    run_binary(
        name = "nuitka_{}".format(name),
        srcs = [":{}_all_deps".format(name)],
        outs = [
            name,
        ],
        args = [
            "--onefile",
            main,
            "--disable-ccache",
            "--show-modules",
            "--output-filename={}".format(name),
            "--output-dir=bazel-out/k8-fastbuild/bin/{}".format(main[0:main.rindex("/")]),
        ],
        tool = NUITKA_TOOL,
    )
