from backend.log import error
from backend.runner import execute_converted_code
from backend.variables import try_get_variable_value


class Judge:
    def __init__(self) -> None:
        self.function_name = "judge"
        self.max_limit = 4  # Sets the max amount of parameters that the user can enter
        self.lower_limit = 4 # Sets the least amount of parameters needed for the function to work

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:
        """main meat method each library"""

        value_a = arguments[0]
        value_b = arguments[1]

        # Obtain the methods to jump to depending if value_a > value_b
        meth_true = arguments[2]
        meth_false = arguments[3]

        # Check that the methods exist
        if meth_true not in method_namespace.keys():
            error(f"Failed to find method {meth_true}, has it been defined?")

        if meth_false not in method_namespace.keys():
            error(f"Failed to find method {meth_false}, has it been defined?")

        # Obtain the meth gut
        meth_true_gut = method_namespace[meth_true]
        meth_false_gut = method_namespace[meth_false]

        # Check if they are variables, and obtain the corresponding value if true
        value_a = try_get_variable_value(value_a, var_namespace)
        value_b = try_get_variable_value(value_b, var_namespace)

        # Since we only can work with integers, we will need to convert them
        try:
            value_a = int(value_a)
            value_b = int(value_b)
        except ValueError as err:
            error(
                f"Failed to convert one or more of the provided arguments into an integer\n{err}"
            )

        finally:

            if value_a > value_b:
                execute_converted_code(
                    meth_true_gut, var_namespace, method_namespace, lib_namespace
                )
            else:
                execute_converted_code(
                    meth_false_gut, var_namespace, method_namespace, lib_namespace
                )
