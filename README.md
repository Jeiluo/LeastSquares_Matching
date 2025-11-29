# Least-Square Matching for Image Pairs

## Core Algorithm tested in C++
### Windows
**1. Download Release for MinGW-w64**
Click [here](https://github.com/niXman/mingw-builds-binaries/releases/download/15.2.0-rt_v13-rev0/x86_64-15.2.0-release-win32-seh-ucrt-rt_v13-rev0.7z) to download the release of `MinGW-W64 v13`.<br>
**2. Install Cmake for Windows**

mkdir build<br>
cd build<br>
cmake .. -G "MinGW Makefiles"<br>
mingw32-make -j8<br>
.\leastsquares_matching.exe<br>

## Image Matching Application Deployment
### Windows
python setup.py bdist_wheel<br>
pip install dist\lsmatching-0.0.1-cp311-cp311-win_amd64.whl