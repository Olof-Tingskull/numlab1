import numpy as np
import matplotlib.pyplot as plt

num_cars = 10
d = 75
total_time = 20
time_step = 0.1

def f(x):    
    return min(max(x / d, 0), 1) * 25

def calculate_positions(initial_distance, lead_car_velocity):
    positions = np.arange(num_cars) * initial_distance

    time_axis = []
    graphs = [[] for i in range(num_cars)] 

    vecf = np.vectorize(f)

    for i in range(int(total_time / time_step)):
        time_axis.append(i * time_step)

        distances = np.diff(positions)
        positions[:-1] = positions[:-1] + vecf(distances) * time_step
        positions[-1] = positions[-1] + lead_car_velocity * time_step

        for j in range(num_cars): 
            graphs[j].append(positions[j])
    
    return (time_axis, graphs)

def run(initial_distance, lead_car_velocity):
    (time_axis, graphs) = calculate_positions(initial_distance, lead_car_velocity)

    fig, ax = plt.subplots()

    for i in range(num_cars):
        ax.plot(time_axis, graphs[i], linewidth=2.0)

    ax.set(xlim=(0, total_time),  ylim=(0, np.max(graphs) + d))

    plt.show()