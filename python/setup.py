from skbuild import setup

setup(
    name="lsmatching",
    version="0.0.1",
    cmake_source_dir=".",
    cmake_args=["-G", "MinGW Makefiles"]
)