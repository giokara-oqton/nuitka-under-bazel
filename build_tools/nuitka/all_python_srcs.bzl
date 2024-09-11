def _all_python_srcs_impl(ctx):
    return DefaultInfo(
        files = ctx.attr.target[PyInfo].transitive_sources,
    )

# Rule definition
all_python_srcs = rule(
    implementation = _all_python_srcs_impl,
    attrs = {
        "target": attr.label(providers = [PyInfo]),
    },
)
