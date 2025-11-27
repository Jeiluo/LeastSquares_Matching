#define pi 3.1415926
#define rou 206265
#include <cmath>

//度分秒转换为弧度
double dms2rad(double dms);

//double类型取绝对值
double dabs(double a);

//将弧度置为0-2pi之间
double rad_abs(double rad);

//取cot值
double cot(double rad);

//将秒置为0附近
double sec_abs(double sec);

//弧度转换为度分秒
double rad2dms(double rad);

template<typename T>
T clamp(T val, T lo, T hi)
{
    if(val < lo) return lo;
    if(val > hi) return hi;
    return val;
}