import matplotlib.pyplot as plt 
import numpy as np 
import src.uppgift7 as u7 




def run(initial_distance, lead_car_velocity, min_iter, max_iter): 
    (t, explicit_graph) = u7.calculate_positions(initial_distance, lead_car_velocity)

    last_car_last_pos = np.empty(max_iter - min_iter)

    for i in range(min_iter, max_iter): 
        (t, graph) = u7.calculate_positions(initial_distance, lead_car_velocity, is_explicit = False, max_iter = i, want_tolerans = False)

        # dubbelchecka så att indexeringen är korrekt
        last_car_last_pos[i - min_iter] = graph[0][-1]

    
    fig, ax = plt.subplots()

    # tror man måste ha asarray här då grpahs i u7 filen verkar vara en vanlig array 
    log_errors = np.log(np.absolute(last_car_last_pos - np.asarray(explicit_graph[0][-1])))

    ax.plot(np.arange(min_iter, max_iter), log_errors, linewidth=2.0)

   # ax.set(xlim=(0, max_iter),  ylim=(0, np.max(log_errors) + 1))

    plt.show()




















































