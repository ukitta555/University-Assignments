import random
import numpy as np

def generate_data():
    class_1 = []
    class_2 = []
    for i in range(100):
        x_coord = random.uniform(0, 1)
        class_1.append(
            [
                np.array(
                    [
                        x_coord,
                        random.uniform(x_coord + 0.001, 1),
                        random.uniform(0, 1)
                    ]
                ),
                -1
            ]
        )
        x_coord = random.uniform(0, 0.5)
        class_2.append(
            [
                np.array(
                    [
                            x_coord,
                            random.uniform(0, x_coord - 0.001),
                            random.uniform(0, 1)
                    ]
                ),
                1
            ]
        )
    return class_1 + class_2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alpha = 0.05
    points = generate_data()
    weights = np.array([random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)])
    print(weights)
    bad_counter = 0
    good_counter = 0

    for point, class_marker in points:
        dot_sign = np.sign(np.array(point).dot(weights))
        if dot_sign * class_marker < 0:
            bad_counter += 1
        else:
            good_counter += 1

    print(f"Bad class: {bad_counter}")
    print(f"Correct class: {good_counter}")
    for i in range(1000):
        for point, class_marker in points:
            dot_sign = np.sign(np.array(point).dot(weights))
            if dot_sign * class_marker < 0:
                weights = weights + alpha * class_marker * point

    print(weights)


    bad_counter = 0
    good_counter = 0

    for point, class_marker in points:
        dot_sign = np.sign(np.array(point).dot(weights))
        if dot_sign * class_marker < 0:
            bad_counter += 1
        else:
            good_counter += 1

    print(f"Bad class: {bad_counter}")
    print(f"Correct class: {good_counter}")

