import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colorbar
from matplotlib import cm
import pandas as pd

viridis = cm.get_cmap('cool', 8)  # Our color map

if __name__ == '__main__':
    x = np.arange(0, 201, 50)
    y = np.array(range(2, 5))
    z = np.arange(0.95, 0.99, 0.01)

    df = pd.read_csv('log.csv')
    # print(df)
    Loss_vals = df.Precision
    # print(Loss_vals[0])

    data_value = np.zeros((len(x), len(y), len(z)))
    print(data_value.size)

    Loss_vals_0 = np.ones(75)
    # for num in range(0, 11):
    for num, item in enumerate(Loss_vals_0):
        Loss_vals_0[num] = Loss_vals[num * 2]

    # print(Loss_vals_0)

    counter = 0
    for a in range(0, 5):
        for b in range(0, 3):
            for c in range(0, 5):
                data_value[a, b, c] = Loss_vals_0[counter]
                counter += 1
    print(data_value)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.8], projection='3d')
    ax_cb = fig.add_axes([0.85, 0.25, 0.05, 0.5])
    ax.set_aspect('auto')
    ax.set_xlabel("Max Timeout")
    ax.set_ylabel("Rounds")
    ax.set_zlabel("Termination Accuracy")
    ax.set_zlim(0.95, 1)
    # ax.set_title("Federated Learning Party 1 Precision Heatmap")

    # plotMatrix(ax, x, y, z, data_value, cmap=viridis, cax=ax_cb)

    plt.savefig("test.png")
    plt.show()
