import math

import numpy as np
from scipy import linalg

N = 20
mu_list: list[float] = [5/4, 5/3]
r_list: list[int] = [1, 1]

def get_e_list():
    coefficients = [
        [0.77, -1],
        [1, 0]
    ]
    result = [0, 1]
    return linalg.solve(coefficients, result)

def get_p_i(k, machine_number, e_list):
    machine_number -= 1
    conditional_factor = \
        1 / math.factorial(k) if k <= r_list[machine_number] \
        else 1 / (math.factorial(r_list[machine_number]) * r_list[machine_number] ** (k-r_list[machine_number]))

    return (e_list[machine_number] / mu_list[machine_number]) ** k * conditional_factor


def get_normalizing_factor(e_list):
    result = 0
    for alpha in range(N+1):
        result += get_p_i(k=alpha, machine_number=1, e_list=e_list) * \
                  get_p_i(k=N-alpha, machine_number=2, e_list=e_list)
    return 1 / result


def get_average_queries_in_queue(p_cmo_list):
    average_queries_in_queue = []

    for cmo in range(2):
        result = 0
        for j in range(r_list[cmo] + 1, N + 1):
            result += (j - r_list[cmo]) * p_cmo_list[cmo][j]
        average_queries_in_queue.append(result)
    return average_queries_in_queue


def get_p_cmo_list():
    p_cmo_list = [np.zeros(N + 1), np.zeros(N + 1)]
    for j in range(N + 1):
        p_cmo_list[0][j] = normalizing_factor * \
                           get_p_i(k=j, machine_number=1, e_list=e_list) * \
                           get_p_i(k=N - j, machine_number=2, e_list=e_list)
    for j in range(N + 1):
        p_cmo_list[1][j] = normalizing_factor * \
                           get_p_i(k=N - j, machine_number=1, e_list=e_list) * \
                           get_p_i(k=j, machine_number=2, e_list=e_list)
    return p_cmo_list


def get_average_working_machines(p_cmo_list):
    average_working_machines = []
    for cmo in range(2):
        result = r_list[cmo]
        for j in range(r_list[cmo] + 1):
            result -= (r_list[cmo] - j) * p_cmo_list[cmo][j]
        average_working_machines.append(result)
    return average_working_machines



if __name__ == "__main__":
    e_list: list[float] = get_e_list()
    normalizing_factor = get_normalizing_factor(e_list)
    p_cmo_list = get_p_cmo_list()

    # for list in p_cmo_list:
    #     for el in list:
    #         print(el)
    #     print()
    # print(p_cmo_list)
    # print(sum(p_cmo_list[0]), sum(p_cmo_list[1]))

    average_queries_in_queue = get_average_queries_in_queue(p_cmo_list=p_cmo_list)
    average_working_machines = get_average_working_machines(p_cmo_list=p_cmo_list)
    average_queries = [
        queue_queries + working_machines
        for queue_queries, working_machines in
        zip(average_queries_in_queue, average_working_machines)
    ]

    intensities = [
        mu * working_machines_cmo
        for mu, working_machines_cmo in
        zip(mu_list, average_working_machines)
    ]

    average_cmo_wait_time = [
        average_queries_cmo / intensity
        for intensity, average_queries_cmo in
        zip(intensities, average_queries)
    ]

    average_cmo_queue_wait_time = [
        average_queries_in_queue_cmo / intensity
        for intensity, average_queries_in_queue_cmo in
        zip(intensities, average_queries_in_queue)
    ]


    print(f"e_i coefficients: {e_list}")
    print(f"Normalizing factor: {normalizing_factor}")

    print(f"Average queries in queue per CMO: {average_queries_in_queue}")
    print(f"Average working machines per CMO: {average_working_machines}")
    print(f"Average queries per CMO: {average_queries}")
    print(f"Intensity of output streams: {intensities}")
    print(f"Average query waiting time per CMO : {average_cmo_wait_time}")
    print(f"Average query waiting time in queue per CMO: {average_cmo_queue_wait_time}")