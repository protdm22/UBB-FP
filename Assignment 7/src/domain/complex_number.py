class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.__real_part = real_part
        self.__imaginary_part = imaginary_part

    def get_real_part(self):
        return self.__real_part

    def get_imaginary_part(self):
        return self.__imaginary_part

    def set_real_part(self, new_real_part):
        self.__real_part = new_real_part

    def set_imaginary_part(self, new_imaginary_part):
        self.__imaginary_part = new_imaginary_part

    def __str__(self):
        if self.__real_part == 0:
            str(self.__imaginary_part) + "i"
        elif self.__imaginary_part == 0:
            return str(self.__real_part)
        elif self.__imaginary_part > 0:
            return str(self.__real_part) + "+" + str(self.__imaginary_part) + "i"
        else:
            return str(self.__real_part) + str(self.__imaginary_part) + "i"

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return False
        else:
            return other.__real_part == self.__real_part and other.__imaginary_part == self.__imaginary_part
