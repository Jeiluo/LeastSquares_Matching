#include "tools.h"

double dabs(double a)
{
    if(a>0)
        return a;
    else
        return -a;
}

double dms2rad(double dms)
{
    double deg=(int)dms;
    double min=(int)((dms-deg)*100);
    double sec=((dms-deg)*100-min)*100;
    double degree=deg+min/60+sec/3600;
    return degree*pi/180;
}

double rad_abs(double rad)
{
    while(rad<0||rad>=2*pi)
    {
        if(rad<0)
            rad+=2*pi;
        else
            rad-=2*pi;
    }
    return rad;
}

double cot(double rad)
{
    return 1/tan(rad);
}

double sec_abs(double sec)
{
    //先将秒值化归至0-2pi之间
    while(sec<0||sec>2*pi*rou)
    {
        if(sec<0)
            sec+=2*pi*rou;
        else
            sec-=2*pi*rou;
    }

    //将接近2pi的秒减至0附近
    if((sec-2*pi*rou<100)&&(sec-2*pi*rou>-100))
        sec-=2*pi*rou;
    return sec;
}

double rad2dms(double rad)
{
    double degree=rad*180/pi;
    double deg=(int)degree;
    double min=(int)((degree-deg)*60);
    double sec=((degree-deg)*60-min)*60;
    return deg+min/100+sec/10000;
}