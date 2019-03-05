import matplotlib.pyplot as plt
"""values in X axis"""
x_values = [1, 2, 3, 4, 5]
"""values in Y axis"""
y_values = [1, 4, 9, 16, 25]
"""in parameter c we set the dot's color"""
"""figsize is in inches"""
plt.figure(dpi=128, figsize=(10, 6))
#plt.scatter(x_values, y_values, s=100, c="red")
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
edgecolor='none', s=40)
"""first pair is the scale of Y axis, second is X axis"""
plt.axis([0, 50, 0, 10])

plt.show()