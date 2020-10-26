import numpy as np

mList = [1, 2, 3]
array = np.array(mList)
print(type(array))
print(np.arange(0, 10, 2))
print(np.zeros(shape=(5, 5)))
print(np.ones(shape=(2, 5)))

np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print(arr)
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())
print(arr.mean())
print(arr.shape)
print(arr.reshape(2, 5))
