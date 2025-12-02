#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "matching.h"

namespace py = pybind11;

py::array mat_to_numpy(const cv::Mat &mat)
{
    if (mat.empty())
        throw std::runtime_error("mat_to_numpy: empty cv::Mat");

    int type = mat.type();
    int depth = CV_MAT_DEPTH(type);

    if (depth == CV_8U)
    {
        return py::array(
            py::buffer_info(
                mat.data,
                sizeof(uint8_t),
                py::format_descriptor<uint8_t>::format(),
                2,
                { mat.rows, mat.cols },
                { (size_t)mat.step, sizeof(uint8_t) }
            )
        );
    }
    else if (depth == CV_32F)
    {
        return py::array(
            py::buffer_info(
                mat.data,
                sizeof(float),
                py::format_descriptor<float>::format(),
                2,
                { mat.rows, mat.cols },
                { (size_t)mat.step, sizeof(float) }
            )
        );
    }
    else
    {
        throw std::runtime_error("mat_to_numpy: unsupported cv::Mat type (only CV_8U & CV_32F)");
    }
}

PYBIND11_MODULE(_lsmatching, m)
{
    m.doc() = "Least squares matching module";
    py::class_<matching>(m, "Matching")
        .def(py::init<std::string, std::string>())
        .def("set_params", &matching::set_params)
        .def("set_centers", &matching::set_centers)
        .def("calculate", &matching::calculate)
        .def("get_left_window", [](matching &self) {
            return mat_to_numpy(self.get_left_window());
        })
        .def("get_right_window", [](matching &self) {
            return mat_to_numpy(self.get_right_window());
            })
        .def("get_matched_points", &matching::get_matched_points);
        ;
}