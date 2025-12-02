//Jiahao Zhou
//jeiluosmith@gmail.com
//git@github:Jeiluo

#pragma once
#include <iostream>
#include <math.h>
#include "opencv2/opencv.hpp"
using namespace cv;

class PointFeature {
private:
	cv::Mat Img;
public:
	void fileRead();
	const cv::Mat& getOrigImg() const { return Img; }

	cv::Mat Moravec_calculate(cv::Mat&);
	cv::Mat Harris_calculate(cv::Mat&);
	cv::Mat SUSAN_calculate(cv::Mat&);
};