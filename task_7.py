class Complex:
    def __init__(self, a):
        self.a = a

    def op_data(self):
        if str(self.a)[1] == '-':
            if "+" in str(self.a):
                b = str(self.a)[2:-2].split('+')
                b = [("-" + b[0]), b[1]]
            else:
                b = str(self.a)[2:-2].split('-')
                b = [("-" + b[0]), ("-" + b[1])]
        else:
            if "+" in str(self.a):
                b = str(self.a)[1:-2].split('+')
            else:
                b = str(self.a)[1:-2].split('-')
                b = [b[0], ("-" + b[1])]
        return b

    def __add__(self, other):
        real = int(self.op_data()[0]) + int(other.op_data()[0])
        img = int(self.op_data()[1]) + int(other.op_data()[1])
        if img < 0:
            return f"({real}{img}j)"
        else:
            return f"({real}+{img}j)"

    def __mul__(self, other):
        real = int(self.op_data()[0]) * int(other.op_data()[0]) - int(self.op_data()[1]) * int(other.op_data()[1])
        img = int(self.op_data()[0]) * int(other.op_data()[1]) + int(self.op_data()[1]) * int(other.op_data()[0])
        if img < 0:
            return f"({real}{img}j)"
        else:
            return f"({real}+{img}j)"

c_1 = Complex(-5+2j)
c_2 = Complex(-2-3j)
c_3 = Complex(1-2j)
print(c_1 + c_3)
print(c_1 * c_2)


