import math as _math
import random as _random
import numpy as np
from typing import  Optional

from neura.utils.types import InputValue, OutputValue

from .base_functions import (
    ParametricFunction,
    ScalarFunction,
    VectorialFunction
)


class Linear(ScalarFunction):
    """
    ## f(x) = x
    """

    def apply_formula(self, x: float) -> float:
        return x
    
    def derivative(self, x: float) -> float:
        return 1
        
class Sigmoid(ScalarFunction):
    """
    ## f(x) = 1 / (1 + e^(-x))
    """

    def apply_formula(self, x: float) -> float:
        return 1 / (1 + _math.exp(-x))

    def derivative(self, x: float) -> float:
        return _math.exp(x) / ((1 + _math.exp(x)) ** 2)
    
class Exponential(ScalarFunction):
    """
    ## f(x) = e^(x)
    """

    def apply_formula(self, x: float) -> float:
        return _math.exp(x)
    
    def derivative(self, x: float) -> float:
        return _math.exp(x)

class ReLu(ScalarFunction):
    """
    ## f(x) = max(0, x)
    """

    def apply_formula(self, x: float) -> float:
        return max(0, x)

    def derivative(self, x: float) -> float:
        return 0 if x <= 0 else 1
    
class LeakyReLu(ScalarFunction):
    """
    ## f(x) = max(x, 0.1x)
    """

    def apply_formula(self, x: float) -> float:
        return max(x, .1 * x)

    def derivative(self, x: float) -> float:
        return 1 if x >= 0 else .1

class Tanh(ScalarFunction):
    """
    ## f(x) = tanh(x)
    """

    def apply_formula(self, x: float) -> float:
        return _math.tanh(x)

    def derivative(self, x: float) -> float:
        return _math.cosh(x) ** -2 
    
class Swish(ScalarFunction):
    """
    ## f(x) = x * sigmoid(x)
    """
    def __init__(self) -> None:
        super().__init__()
        self.sigmoid = Sigmoid()
    
    def apply_formula(self, x: float) -> float:
        return x * self.sigmoid.apply_formula(x)

    def derivative(self, x: float) -> float:
        return self.sigmoid.apply_formula(x) + x * self.sigmoid.derivative(x)
    
class PReLU (ParametricFunction):
    """
    ## f(x) = ax if x < 0 else x
    """
    def __init__(self, a: Optional[float] = None) -> None:
        super().__init__()
        self.a: float = a if a else _random.gauss(0, 1)
        self.params = {"a": self.a}

    def apply_formula(self, x: float) -> float:
        if x < 0:
            return self.a * x
        return x

    def derivative(self, x: float) -> float:
        if x < 0:
            return self.a
        return 1    

class Softmax(VectorialFunction):
    """
    ## Softmax activation function
    """
    def apply_formula(self, x: InputValue) -> OutputValue:
        exp_x = map(lambda i: _math.exp(i), x)
        sum_exp_x = sum(exp_x)
        return np.array([j / sum_exp_x for j in exp_x], dtype=np.float64)

    def derivative(self, x: InputValue) -> OutputValue:
        # Derivative of softmax is a bit more complex, typically used in cross-entropy loss
        raise NotImplementedError("Softmax derivative is usually combined with cross-entropy loss")
    
