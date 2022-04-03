import matplotlib.pyplot as plt

time_plot_length = 20

tasks_deadlines = [3, 4, 5]
tasks_y_axis = [1, 2, 3]
num_of_tasks = len(tasks_y_axis)
task_deadline = [3, 4, 5]
plt.subplots(figsize=(10, 7))
[plt.axhline(y=i, linestyle='solid') for i in tasks_y_axis]

# mark(tick) exec time for each task axis
list_of_x = []
list_of_y = []
for i in range(1, time_plot_length):
    for t in tasks_y_axis:
        list_of_x.append(i)
        list_of_y.append(t)
plt.plot(list_of_x, list_of_y, 'r|')

# mark(tick) deadline time for each task axis
for t_i in range(len(tasks_y_axis)):
    for i in range(time_plot_length // tasks_deadlines[t_i]):
        plt.plot(task_deadline[t_i]*(i+1), tasks_y_axis[t_i], 'bd')


plt.ylim([0, 10])
plt.xlim([0, time_plot_length],)
plt.xticks([i for i in range(time_plot_length)])
plt.ylabel('tasks')
plt.show()
