from os import stat
from Pyro4 import expose


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        array = self.read_input()
        step = len(array) / len(self.workers)

        mapped = []
        for i in range(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(i * step, min((i + 1) * step, len(array) - 1), array))
        reduced = self.myreduce(mapped)
        self.write_output(reduced)

    # [1, 2, 3, 4, 5 ,6]
    @staticmethod
    @expose
    def mymap(a, b, array):
        max_result = float('-inf')
        for fixed_element_index, fixed_element in enumerate(array[a:b + 1], a):
            if fixed_element_index + 1 < len(array):
                for moving_element in array[fixed_element_index + 1:]:
                    if int(fixed_element) | int(moving_element) > max_result:
                        max_result = int(fixed_element) | int(moving_element)
        return max_result

    @staticmethod
    @expose
    def myreduce(mapped):
        maximum = float('-inf')
        for chunk in mapped:
            if chunk.value > maximum:
                maximum = chunk.value
        return maximum

    def read_input(self):
        f = open(self.input_file_name, 'r')
        array = f.readline().strip().split()
        f.close()
        return array

    def write_output(self, output):
        f = open(self.output_file_name, 'w')

        f.write(str(output))

        f.close()