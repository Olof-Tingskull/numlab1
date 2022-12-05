time_step=0.01
num_cars = 10
total_time = 25
distance = 10
lead_velocity = 25

def euler_iterations(iteration_function):
    total_steps = int(total_time / time_step)

    time_axis = [i * time_step for i in range(total_steps)]
    cars = [[distance * i] for i in range(num_cars)] 

    for step in range(total_steps - 1):
        cars[-1].append(cars[-1][step] + lead_velocity * time_step)

        for car in range(num_cars - 2, -1, -1): 
            cars[car].append(iteration_function(cars[car][step], cars[car + 1][step], cars[car + 1][step + 1]))
    
    return (time_axis, cars)