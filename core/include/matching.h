#include "opencv2/opencv.hpp"
#include <string>
#include "matrix.h"
#include "tools.h"

class matching
{
    private:
    cv::Mat left_img;
    cv::Mat right_img;
    int window_size = 15;
    cv::Mat left_window;
    cv::Mat right_window;
    cv::Mat left_window_centered;
    int W,H;
    int leftx, lefty, rightx, righty;
    double new_rightx, new_righty;
    Matrix X; //参数值
    Matrix B;
    Matrix L;
    Matrix x; //改正数
    Matrix v; //残差

    cv::Mat g2;
    cv::Mat g2_dx, g2_dy;
    cv::Mat distortion_window;

    double corr;
    double d_corr;
    bool first = 1;
    bool stop = 0;
    double delta0, deltag, deltag_, deltax;
    double SNR;
    double rho;

    double min_x_left;
    double min_y_left;
    double min_x_right;
    double min_y_right;

    public:
    matching(std::string left_path, std::string right_path);
    void set_params(int window_size);
    void set_centers(int left_x, int left_y, int right_x, int right_y); //construct windows
    void disp_windows();
    void params_init();
    void centerize();
    void get_g2(); //right window 重采样
    float sample_img(cv::Mat img, double x, double y);
    void radioCorrection();
    void get_dg(); //对g2求导
    void construct_matrices(); //构造系数矩阵
    void adjustment();
    void update();
    void get_corr();
    void calculate();
    void precision();
    cv::Mat get_left_window();
    cv::Mat get_right_window();
    void get_result();
    void get_matched_points(std::string savepath);
    double get_matched_y();
    double get_matched_x();
};