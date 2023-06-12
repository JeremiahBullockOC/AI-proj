import sklearn
from sklearn.linear_model import LinearRegression
from random_obstacles import *
from asp import *
import numpy as np


def predictObstacles(maze, destination):
    holdingSet = []
    originalSet = []
    for n in range(100):
        originalSet.append(np.array(maze))
        tempMaze = maze.copy()
        tempMaze = handle_pit_creation(tempMaze, destination)
        tempMaze = create_oil_slick(tempMaze, destination, 0.05)
        tempMaze, junk = create_teleporter(tempMaze, (len(maze) / 5))
        holdingSet.append(np.array(tempMaze))

    originalSet = np.array(originalSet)
    nsamples, nx, ny = originalSet.shape
    d2_train_dataset = originalSet.reshape((nsamples, nx * ny))
    data = d2_train_dataset[:-1]
    holdingSet = np.array(holdingSet)
    nsamples, nx, ny = holdingSet.shape
    d2_target_dataset = holdingSet.reshape((nsamples, nx * ny))
    target = d2_target_dataset[:-1]
    model = LinearRegression()
    model.fit(data, target)
    new_data = [d2_target_dataset[-1]]
    prediction = model.predict(new_data)
    # print(len(prediction[0].tolist()))
    return prediction[0].tolist()