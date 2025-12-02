from skbuild import setup
import os
import shutil

dll_names = [
    "python311.dll",
    "libstdc++-6.dll",
    "libgcc_s_seh-1.dll",
    "libwinpthread-1.dll",
]

def find_mingw_bin():
    paths = os.environ.get("PATH", "").split(os.pathsep)
    
    # 遍历每一个路径，直到找到有效的 MinGW bin 路径
    for path in paths:
        # 判断路径是否存在
        if os.path.exists(path):
            # 如果路径存在，检查路径是否包含 mingw 和 bin
            if "mingw" in path.lower() and "bin" in path.lower():
                return path  # 返回有效的 MinGW bin 路径
        else:
            # 打印无效路径（可选）
            print(f"Invalid path: {path}")
    
    # 如果没有找到有效的 MinGW bin 路径，打印提示并返回 None
    print("No valid MinGW bin directory found in PATH.")
    return None

def find_dll(name):
    # 1. 当前 Python/Conda 环境下
    import sys
    candidate = os.path.join(sys.prefix, name)
    if os.path.exists(candidate):
        return candidate

    # 2. MinGW bin 目录（你可以根据实际路径修改）
    mingw_bin = find_mingw_bin()
    if mingw_bin:
        candidate = os.path.join(mingw_bin, name)
        if os.path.exists(candidate):
            return candidate

target_dir = os.path.join("_skbuild\\win-amd64-3.11\\cmake-install\\lsmatching")
os.makedirs(target_dir, exist_ok=True)

# 拷贝所有 DLL 到 lsmatching 包目录
copied_dlls = []
for dll in dll_names:
    dll_path = find_dll(dll)
    if dll_path is None:
        raise RuntimeError(f"Cannot find {dll} on this system")
    shutil.copy(dll_path, os.path.join("_skbuild\\win-amd64-3.11\\cmake-install\\lsmatching", dll))
    copied_dlls.append(dll)

setup(
    name="lsmatching",
    version="0.0.1",
    cmake_source_dir=".",
    cmake_args=["-G", "MinGW Makefiles"],
    packages=["lsmatching"],
    package_dir={"lsmatching": "lsmatching"},
    package_data={"lsmatching": ["_lsmatching*.pyd", "__init__.py", "*.dll"] + copied_dlls},
    include_package_data=True,
)