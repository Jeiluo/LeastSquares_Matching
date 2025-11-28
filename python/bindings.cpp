#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "matching.h"

namespace py = pybind11;

py::array mat_to_numpy(const cv::Mat &mat)
{
    return py::array(
        py::buffer_info(
            mat.data,
            sizeof(float),
            py::format_descriptor<float>::format(),
            2,
            { mat.rows, mat.cols },
            { sizeof(float) * mat.cols, sizeof(float) }
        )
    );
}

PYBIND11_MODULE(lsmatching, m)
{
    py::class_<matching>(m, "Matching")
        .def(py::init<std::string, std::string>())
        .def("set_params", &matching::set_params)
        .def("set_centers", &matching::set_centers)
        .def("calculate", &matching::calculate);
}