import pandas as pd
import numpy as np

'''data = {
    1:{1:'one', 2:"two", 3:"three", 4:"four"}
    2:{}
    3:{}
    4:{}
    5:{}
    6:{}
}'''
#my first attempt before i saw solution


'''df = pd.DataFrame(np.random.randint(1, 100, size = (6, 4)), columns=['A', 'B', 'C', 'D'])
print(df)

df.set_index('A', inplace=True)
print(df)'''

'''df = pd.DataFrame(np.random.randint(1, 100, size = (3, 3)), columns=['A', 'B', 'C'], index=['X','Y','Z'])
print(df)

element = df.at['Y', 'B']
print(element)'''

"""df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)))
print(df)

df[4] = df[0] * df[1]
print("procut of colomns")
print(df[4])

print("set as new columns")
print(df)"""

df = pd.read_csv('data.csv')
print(df.describe())

import matplotlib.pyplot as plt

x = [1, 3, 5,6, 7, 9, 12]
y = [1, 4, 7, 8 ,9 , 13, 23]

plt.plot(x, y, color='red', linestyle='--', marker = 'o')
plt.show()

x = [1, 3, 9, 10, 18 ,23]
y1 = [2, 4, 5, 6, 78, 9]
y2 = [2, 4, 5, 78, 8, 9]

plt.figure(figsize=(9,5))

plt.subplot(2, 2, 1)
plt.plot(x,y1)
plt.title('plot1')

plt.subplot(2, 2, 2)
plt.plot(x, y2, color = 'red')

plt.subplot(2, 2, 3)
plt.plot(y1, x, color = 'yellow')

plt.subplot(2, 2, 4)
plt.plot(y2, x, color = 'green')

plt.show()