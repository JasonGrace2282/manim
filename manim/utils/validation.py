from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence, Callable
from typing import Generic, TypeVar
import operator as op

T = TypeVar("T")
U = TypeVar("U")


class BaseValidator(ABC, Generic[T, U]):
    """
    Abstract descriptor class for validators.

    https://docs.python.org/3/howto/descriptor.html#validator-class
    """
    def __set_name__(self, owner: object, name: str):
        self.private_name = '_' + name

    def __get__(self, obj: T, objtype: type[object] | None = None) -> U:
        return getattr(obj, self.private_name)

    def __set__(self, obj: T, value: U):
        if (new_value := self.validate(value)) is not None:
            value = new_value
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value: U) -> U | None:
        """Used to validate/mutate an attribute.

        To simply use it for validation, don't return anything from 
        this method. Otherwise, the return value from this function will
        be used as the modified value

        """


class Validator(BaseValidator):
    """A BaseValidator with some useful arguments
    """
    def __init__(
        self,
        format_str: str | Callable,
        *,
        exception_on_failure: bool = True,
        exception: type[Exception] = ValueError,
        iterate: bool = False,
    ) -> None:
        super().__init__()
        self.format_str = format_str
        self.exception_on_failure = exception_on_failure
        self.iterate = iterate
        self.exception_type = exception

    def raise_error(self, **kwargs):
        from manim._config import logger
        if callable(self.format_str):
            error = self.format_str(**kwargs)
        else:
            error = self.format_str.format(**kwargs)

        if self.exception_on_failure:
            raise self.exception_type(error)
        else:
            logger.warning(error)



class SubclassOf(Validator):
    """
    Validator that anything set to this value MUST be an
    instance of a subclass of the assigned class.

    Examples
    --------
    
    .. code-block:: pycon

        >>> from manim import VMobject, Mobject
        >>> class MyMobject:
        ...     submobject = SubclassOf(
        ...         VMobject,
        ...         "Expected instance of {expected.__name__}, got {invalid} instead"
        ...     )
        >>> v = VGroup()
        >>> v.submobject = VMobject()
        >>> try:
        ...     v.submobject = Mobject()
        ... except ValueError as e:
        ...     print(e)
        Expected instance of VMobject, got Mobject instead


    Parameters
    ----------
        __cls
            The class any attribute must be a subclass of

        format_str
            A formatting string for the error message.
            An example 

    """
    def __init__(
        self,
        __cls: type[T],
        /,
        format_str: str | Callable = "Expected instance of {expected.__name__}, got {invalid} instead",
        forbidden: Sequence[type[T]] = (),
        **kwargs
    ) -> None:
        super().__init__(format_str=format_str, **kwargs)
        self.class_ = __cls
        # forbidden is for Mobjects without points
        self.forbidden = forbidden

    def validate(self, value):
        if not self.iterate:
            value = (value,)
        elif (
            not isinstance(value, Iterable)
            or any(isinstance(value, bad) for bad in self.forbidden)
        ):
            self.raise_error(
                expected=self.class_,
                invalid=value
            )
        for val in value:
            if not isinstance(val, self.class_):
                self.raise_error(
                    expected=self.class_,
                    invalid=val
                )

class OneOf(Validator, Generic[T]):
    """Can be one of a given set of values.
    """
    def __init__(self, *options: T, format_str: str | Callable = "Expected value in {options}, got {invalid}", **kwargs) -> None:
        super().__init__(format_str=format_str, **kwargs)
        self.options: set[T] = set(options)

    def validate(self, value: T):
        if value not in self.options:
            self.raise_error(options=self.options, invalid=value)


def _number_error(
    invalid: float,
    min: float,
    max: float,
    min_inclusive: bool,
    max_inclusive: bool,
) -> str:
    base = "Expected value "
    if min > float("-inf") and max < float("inf"):
        # format using interval notation
        base += f"in range {'[' if min_inclusive else '('}{min}, {max}{']' if max_inclusive else ')'}"
    elif min > float("inf"):
        base += f"less than {min}{' (inclusive)' if min_inclusive else ''}"
    elif max < float("inf"):
        base += f"greater than {max}{' (inclusive)' if max_inclusive else ''}"
    else:
        # base case, no bounds added. In this case input
        # was not int | float
        base = "Expected number"

    return f"{base}, got {invalid} instead"

class Number(Validator):
    """A number in a given range.
    """
    def __init__(
        self,
        min: float = float("-inf"),
        max: float = float("inf"),
        format_str: str | Callable = _number_error,
        *,
        min_inclusive: bool = True,
        max_inclusive: bool = False,
        **kwargs
    ):
        super().__init__(format_str, **kwargs)
        self.min = min
        self.max = max
        self.incl_min = min_inclusive,
        self.incl_max = max_inclusive

    def _check_range(self, value: float) -> bool:
        return (
            (
                op.ge(value, self.min)
                if self.incl_min
                else op.gt(value, self.min)
            ) and (
                op.le(value, self.max)
                if self.incl_max
                else op.lt(value, self.max)
            )
        )

    def validate(self, value):
        if not (
            isinstance(value, (int, float))
            and self._check_range(value)
        ):
            self.raise_error(
                invalid=value,
                min=self.min,
                max=self.max,
                min_inclusive=self.incl_min,
                max_inclusive=self.incl_max,
            )
