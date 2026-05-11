import numpy as np
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
print(calorie_stats)
average_calories = np.mean(calorie_stats) - 60
print(average_calories)