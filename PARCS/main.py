from os import stat
from Pyro4 import expose


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        array, target = self.read_input()
        step = len(array) / len(self.workers)

        mapped = []
        for i in range(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(i * step, min((i + 1) * step, len(array) - 1), array, target))
        reduced = self.myreduce(mapped)
        self.write_output(reduced)

    @staticmethod
    @expose
    def mymap(a, b, array, target):
        res = []
        for fixed_element_index, fixed_element in enumerate(array[a:b + 1], a):
            if fixed_element_index + 1 < len(array):
                for moving_element in array[fixed_element_index + 1:]:
                    if int(fixed_element)+ int(moving_element) == int(target):
                        res.append([fixed_element, moving_element])
        return res

    @staticmethod
    @expose
    def myreduce(mapped):
        res = []
        for chunk in mapped:
            for s in chunk.value:
                res.append(s)
        return res

    def read_input(self):
        f = open(self.input_file_name, 'r')
        array, target = [line.strip() for line in f.readlines()]
        array = array.split()
        f.close()
        return array, target

    def write_output(self, output):
        f = open(self.output_file_name, 'w')

        for result in output:
            f.write(str(result[0]) + " ")
            f.write(str(result[1]))
            f.write("\n")

        f.close()