import torch
import activations

def test_sigmoid():
    val = torch.Tensor(10, 10)
    assert (torch.sigmoid(val) == activations.sigmoid(val)).all()