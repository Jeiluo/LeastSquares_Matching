mkdir build<br>
cd build<br>
cmake .. -G "MinGW Makefiles"<br>
mingw32-make -j8<br>
.\leastsquares_matching.exe


python setup.py bdist_wheel
pip install dist\lsmatching-0.0.1-cp311-cp311-win_amd64.whl