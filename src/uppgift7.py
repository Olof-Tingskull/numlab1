import numpy as np
import matplotlib.pyplot as plt

v_max = 25
num_cars = 10
d = 75
total_time = 100
time_step = 0.1
k = time_step * v_max / d



def g(x, v): 
    return v

def f(x): 
    return min(max(x / d, 0), 1) * 25


def fixed_backward_euler(current_pos, front_new_pos, max_iter): 
    iter = 0

    # need to do something about tol when searching for the iteration plot
    tol = 10^-1

    diff = abs(current_pos - (current_pos + time_step * f(front_new_pos - current_pos)))
    x = current_pos

    while diff > tol and iter < max_iter: 
        # funktionen på höger sida kanske ska skrivas som en enskild funktion
        x = current_pos + time_step * f(front_new_pos - x)
        iter += 1

        diff = abs(x - (current_pos + time_step * f(front_new_pos - x)))

    return x 


def explicit_backward_euler(current_pos, front_new_pos):
    return  current_pos + k * min((front_new_pos - current_pos)/(1+k), d)


def calculate_positions(initial_distance, lead_car_velocity, is_explicit = True, max_iter = 100):
    positions = np.arange(num_cars) * float(initial_distance)

    time_axis = []
    graphs = [[] for i in range(num_cars)]  

    for i in range(int(total_time / time_step)):
        time_axis.append(i * time_step)

        graphs[-1].append(positions[-1] + time_step * g(positions[-1], lead_car_velocity))
        positions[-1] = graphs[-1][-1]

        # måste dubbelchecka iterationsgränserna för reverse loopen här känns som att den borde loopa från 2 istället för 1
        for i in range(2, num_cars + 1): 
            if is_explicit: 
                graphs[-i].append(explicit_backward_euler(positions[-i], positions[-i + 1]))
            else: 
                graphs[-i].append(fixed_backward_euler(positions[-i], positions[-i + 1], max_iter))
            positions[-i] = graphs[-i][-1]   # car i (counted backwards) latest updated pos
    
    return (time_axis, graphs)
    


def run(initial_distance, lead_car_velocity):
    (time_axis, graphs) = calculate_positions(initial_distance, lead_car_velocity)

    fig, ax = plt.subplots()

    for i in range(num_cars):
        ax.plot(time_axis, graphs[i], linewidth=2.0)

    ax.set(xlim=(0, total_time),  ylim=(0, np.max(graphs) + d))

    plt.show()





