#include "matching.h"
#include <iostream>

int main()
{
    std::string left_path = "F:/Users/21910/Desktop/github/LeastSquares_Matching/img/uavl_epi.jpg";
    std::string right_path = "F:/Users/21910/Desktop/github/LeastSquares_Matching/img/uavr_epi.jpg";
    matching match(left_path, right_path);
    match.set_params(45);
    match.set_centers(2061,1408,1547,1408);
    match.calculate();
    match.get_result();
    return 0;
}