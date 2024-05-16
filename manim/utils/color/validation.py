import numpy as np

from ..validation import BaseValidator


class InternalValueValidator(BaseValidator):
    def validate(self, value):
        if not isinstance(value, np.ndarray):
            raise TypeError("value must be a numpy array")
        if value.shape[0] != 4:
            raise TypeError("Array must have 4 values exactly")
