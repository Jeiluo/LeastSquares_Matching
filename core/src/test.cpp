#include "matching.h"
#include <iostream>

int main()
{
    std::string left_path = "C:/Users/10527/Desktop/shuzisheyingceliang/LeastSquares_Matching/img/uavl_epi.jpg";
    std::string right_path = "C:/Users/10527/Desktop/shuzisheyingceliang/LeastSquares_Matching/img/uavr_epi.jpg";
    matching match(left_path, right_path);
    match.set_params(35);
    match.set_centers(1419,931,902,931);
    match.disp_windows();
    match.calculate();
    match.disp_windows();
    return 0;
}