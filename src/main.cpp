#include <torch/extension.h>

#include <iostream>

torch::Tensor d_sigmoid(torch::Tensor z)
{
    auto s = torch::sigmoid(z);
    return s;
}

PYBIND11_MODULE(activations, m)
{
    m.def("sigmoid", &d_sigmoid, "Sigmoid Function");
}