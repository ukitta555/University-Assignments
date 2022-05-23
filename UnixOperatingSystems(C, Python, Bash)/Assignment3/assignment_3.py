import json
from operator import attrgetter

import matplotlib.pyplot as plt

if __name__ == '__main__':
    dictionary = dict()
    total = 0
    with open("du.log.txt") as file:
        while True:
            stringified_number = file.readline()
            if stringified_number is None or stringified_number == '':
                break
            else:
                clean_number = str(int(stringified_number))
                if dictionary.get(clean_number):
                    dictionary[clean_number] += 1
                else:
                    dictionary.update({clean_number: 1})
                total += 1

    plt.bar(dictionary.keys(), dictionary.values(), 10, color='g')
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    plt.show()

    eighty_percent = round(total * 0.8)
    current_total = 0
    current_key = None

    for key, val in sorted(list(dictionary.items()), key=lambda x: int(x[0])):
        current_total += val
        current_key = key
        if current_total >= eighty_percent:
            break

    print(int(current_key) * 512)

    print(sorted(list(dictionary.items()), key=lambda x: int(x[0])))

