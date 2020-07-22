class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
            output = "\n". join(map(str, self.list))
            return (((output.replace("[", "")).replace("]", "")).replace(",", "")).replace(" ", "\t") + f"\n{'*' * 10}"

    def __add__(self, other):
        new_list = []
        for i in range(len(self.list)):
            new_list.append([])
            for k in range(len(self.list[i])):
                new_list[i].append(self.list[i][k] + other.list[i][k])
        output = "\n".join(map(str, new_list))
        return (((output.replace("[", "")).replace("]", "")).replace(",", "")).replace(" ", "\t")



matrix_1 = Matrix([[1, 2, 23, 45, 67], [3, 4, 5, 7, 20], [5, 6, 34, -9, 19]])
matrix_2 = Matrix([[1, 2, -56, 34, 67], [3, 4, 58, 35, 29], [5, 6, 45, 91, -80]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
