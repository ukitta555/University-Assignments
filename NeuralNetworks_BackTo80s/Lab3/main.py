import math
import random
from pprint import pprint
from typing import List
import numpy as np


data = [
    [5.4, 4020, 2060, 57, 37],
    [8.9, 4810, 2223, 140, 40],
    [19.5, 5380, 2910, 285, 60],
    [25, 5890, 2880, 300, 40],
    [44.8, 6870, 3270, 700, 55],
    [56, 6316, 3705, 700, 44],
    [68, 7380, 3755, 700, 38],
    [13.8, 5200, 2470, 300, 60],
    [9.2, 4285, 2348, 140, 42],
    [30, 5920, 3000, 500, 54],
    [31.8, 6070, 3180, 500, 60],
    [47.5, 6675, 3320, 600, 34],
    [44.2, 6770, 3070, 520, 37]
]

predict_data = [
    [46, 6770, 3070, 520, 37],
    [49, 6900, 3150, 520, 40]
]

def normalize(data: List[List[float]]):
    for column_index in range(len(data[0])):
        max_value = float("-inf")
        min_value = float("inf")
        for data_point in data:
            if data_point[column_index] > max_value:
                max_value = data_point[column_index]
            if data_point[column_index] < min_value:
                min_value = data_point[column_index]
        a_n = 1 / (max_value - min_value)
        b_n = - min_value / (max_value - min_value)
        for data_point in data:
            data_point[column_index] = a_n * data_point[column_index] + b_n

    return data

def calc_eucledean_distance(vector_one: List[float], vector_two: np.ndarray[float]):
    return math.sqrt(
        sum(
            [(value - weight) ** 2 for value, weight in zip(vector_one, vector_two)]
        )
    )



def find_closest_weight_vector(data_point: List[float], W: np.ndarray[np.ndarray[float]]):
    minimum_distance = float("inf")
    min_weight_vector_index = -1
    for index, weight_vector in enumerate(W):
        distance = calc_eucledean_distance(data_point, weight_vector)
        if distance < minimum_distance:
            minimum_distance = distance
            min_weight_vector_index = index
    return min_weight_vector_index


def train(data, W):
    learning_rate = 0.3
    learning_rate_delta = 0.05
    while learning_rate > 0:
        for _ in range(10):
            for data_point in data:
                closest_weight_vector_index = find_closest_weight_vector(data_point, W)
                for weight_index in range(len(W[closest_weight_vector_index])):
                    W[closest_weight_vector_index][weight_index] += \
                        learning_rate * (data_point[weight_index] - W[closest_weight_vector_index][weight_index])
            learning_rate -= learning_rate_delta
    pprint(W)


def generate_random_weights():
    W = np.random.uniform(
        low=0.1,
        high=0.3,
        size=[
            2,
            len(data[0])
        ]
    )
    return W

mu_0 = 0.5
sigma_0 = 3
a = 2
b = 2

def learning_rate_decay(time):
    return mu_0 * np.exp(-a*time)

def sigma(time):
    return sigma_0 * np.exp(-b * time)

def neighbourhood_function(time, distance):
    return np.exp(-(distance ** 2) / (2 * sigma(time)))



if __name__ == '__main__':
    result = normalize(data)
    W = generate_random_weights()
    pprint(result)

    time = 1

    while time < 200:
        random_data_point = random.choice(data)
        closest_weight_vector_index = find_closest_weight_vector(random_data_point, W)
        for vector_index, weight_vector in enumerate(W):
            if vector_index != closest_weight_vector_index:
                distance_between_closest_and_this_weight_vectors = calc_eucledean_distance(
                    W[closest_weight_vector_index],
                    weight_vector
                )
                for column_index in range(len(weight_vector)):
                    weight_vector[column_index] += \
                        learning_rate_decay(time) * \
                        neighbourhood_function(time, distance_between_closest_and_this_weight_vectors) * \
                        (random_data_point[column_index] - weight_vector[column_index])
        time += 1

    # train(result, W)
    print("Train data verification:")
    for data_point in data:
        closest_weight_vector_index = find_closest_weight_vector(data_point, W)
        print(closest_weight_vector_index)
    print("Predictions:")
    for data_point in predict_data:
        closest_weight_vector_index = find_closest_weight_vector(data_point, W)
        print(closest_weight_vector_index)
