//Jiahao Zhou
//jeiluosmith@gmail.com
//git@github:Jeiluo

#include "Correlation.h"

const double NCC_THRESHOLD = 0.7;
const int WINDOWSIZE = 3;
const int SEARCHSIZE = 520;

cv::Mat CorrelationMatch::matOperator(char op, cv::Mat& img) {
	PointFeature pf;
	switch (op) {
	case 'M':return pf.Moravec_calculate(img);
	case 'H':return pf.Harris_calculate(img);
	case 'S':return pf.SUSAN_calculate(img);
	default: return cv::Mat();
	}
}

void CorrelationMatch::Calculate(cv::Mat& LefImg,cv::Mat& RigImg) {
	Mat LefPoint = matOperator(POINTFEATUREMETHOD, LefImg);

	for (int i = WINDOWSIZE / 2; i < row - WINDOWSIZE / 2; i++) {
		double* rowPtr = LefPoint.ptr<double>(i);
		for (int j = WINDOWSIZE / 2; j < col - WINDOWSIZE / 2; j++)
			if (rowPtr[j]) {
				Rect leftRect(j - WINDOWSIZE / 2, i - WINDOWSIZE / 2, WINDOWSIZE, WINDOWSIZE);
				Mat leftWindow = LefImg(leftRect);
				double meanLeft = mean(leftWindow)[0];
				double NCC = -1.0;
				int count = 0;
				for (int k = j - SEARCHSIZE; k < j - 500; k++) {
					if (j - SEARCHSIZE < 0)
						continue;
					Rect rightRect(k - WINDOWSIZE / 2, i - WINDOWSIZE / 2, WINDOWSIZE, WINDOWSIZE);
					Mat RigWindow = RigImg(rightRect);
					double meanRig = mean(RigWindow)[0];
					double up = 0.0;
					double down = 0.0;
					double downleft = 0.0;
					double downrig = 0.0;

					for (int m = 0; m < WINDOWSIZE; m++)
						for (int n = 0; n < WINDOWSIZE; n++) {
							up += (leftWindow.at<uchar>(m, n) - meanLeft)
								* (RigWindow.at<uchar>(m, n) - meanRig);
							downleft += (leftWindow.at<uchar>(m, n) - meanLeft)
								* (leftWindow.at<uchar>(m, n) - meanLeft);
							downrig += (RigWindow.at<uchar>(m, n) - meanRig)
								* (RigWindow.at<uchar>(m, n) - meanRig);
						}

					down = sqrt(downleft * downrig);
					if (down != 0)
						if (up / down > NCC) {
							NCC = up / down;
							count = k;
						}
				}
				if (NCC > NCC_THRESHOLD) {
					Point pt1(j, i);
					Point pt2(count, i + row);
					Point pt3(count, i);
					LeftSame.push_back(pt1);
					RigSame.push_back(pt3);
				}
			}
	}
}

void CorrelationMatch::saveResult(const std::string& savepath) {
	std::filesystem::path basePath(savepath);

	std::ofstream outfileLeft(basePath / "Left_result.dat", std::ios::app);
	std::ofstream outfileRight(basePath / "Right_result.dat", std::ios::app);

	for (const Point& ptL : LeftSame) {
		outfileLeft << ptL.x << '\t' << ptL.y << std::endl;
	}

	for (const Point& ptR : RigSame) {
		outfileRight << ptR.x << '\t' << ptR.y << std::endl;
	}
}