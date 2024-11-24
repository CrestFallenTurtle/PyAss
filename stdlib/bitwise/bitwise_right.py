from backend.log import error
from backend.variables import try_get_variable_value, get_variable_name


class Bitwise_Right:

    def __init__(self) -> None:
        self.function_name = "rshift"

    def start(
        self,
        arguments: list[str],
        var_namespace: dict[str, any],
        method_namespace: dict[str, any],
        lib_namespace: dict[str, any],
    ) -> None:

        if len(arguments) != 3:
            error(
                f"The wrong amount of arguments where sent in, expected three, got {len(arguments)}"
            )

        namespace = {}

        # Probably overkill, but create a namespace
        for arg in arguments:
            var_value = try_get_variable_value(arg, var_namespace)
            arg = get_variable_name(arg)

            namespace[arg] = var_value

        try:
            # This is so fucking stupid
            a = int(namespace[list(namespace.keys())[0]])
            b = int(namespace[list(namespace.keys())[1]])

            resulting_var = list(namespace.keys())[2]
            var_namespace[resulting_var] = a >> b

        except ValueError as err:
            error(
                f"Failed to convert one or more of the provided arguments into an integer\n{err}"
            )
