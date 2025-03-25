INITIAL_INDEX = -1


class FunctionCall:
    def __init__(self, function_name, *function_parameters):
        self.__function_name = function_name
        self.__function_parameters = function_parameters

    def call(self):
        self.__function_name(*self.__function_parameters)

    def __call__(self, *arguments, **keyword_arguments):
        return self.call()


class Operation:
    def __init__(self, undo_function, redo_function):
        self.__undo_function = undo_function
        self.__redo_function = redo_function

    def undo(self):
        self.__undo_function()

    def redo(self):
        self.__redo_function()


class CascadedOperation:
    def __init__(self, *operations):
        self.__operations = operations

    def undo(self):
        for operation in self.__operations:
            operation.undo()

    def redo(self):
        for operation in self.__operations:
            operation.redo()


class UndoError(Exception):
    def __init__(self):
        self.__error_message = "UNDO ERROR! No more undoes available"

    def __str__(self):
        return self.__error_message


class RedoError(Exception):
    def __init__(self):
        self.__error_message = "REDO ERROR! No more redoes available"

    def __str__(self):
        return self.__error_message


class UndoRedoService:
    def __init__(self):
        self.__history = []
        self.__history_index = INITIAL_INDEX

    def record_undo(self, operation: Operation):
        self.__history.append(operation)
        self.__history_index = len(self.__history) - 1

    def undo(self):
        if self.__history_index == INITIAL_INDEX:
            raise UndoError()

        self.__history[self.__history_index].undo()
        self.__history_index -= 1

    def redo(self):
        if self.__history_index == len(self.__history) - 1:
            raise RedoError()

        self.__history_index += 1
        self.__history[self.__history_index].redo()
