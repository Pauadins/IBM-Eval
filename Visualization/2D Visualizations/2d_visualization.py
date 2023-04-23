import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colorbar
from matplotlib import cm
import pandas as pd

viridis = cm.get_cmap('cool', 8)  # Our color map

if __name__ == '__main__':
    max_timeout = np.arange(0, 201, 2)
    termination_accuracy = np.arange(0.9, 0.999, 0.001)

    df = pd.read_csv('log.csv')

    data_value = np.zeros((len(max_timeout), len(termination_accuracy)))

    data_loss_vals = df.Loss
    loss_vals = np.ones((175, 2))
    for num, item in enumerate(loss_vals):
        loss_vals[num][0] = data_loss_vals[num * 2]
        loss_vals[num][1] = data_loss_vals[num * 2 + 1]

    data_accuracy_vals = df.Accuracy
    accuracy_vals = np.ones((175, 2))
    for num, item in enumerate(accuracy_vals):
        accuracy_vals[num][0] = data_accuracy_vals[num * 2]
        accuracy_vals[num][1] = data_accuracy_vals[num * 2 + 1]

    data_precision_vals = df.Precision
    precision_vals = np.ones((175, 2))
    for num, item in enumerate(precision_vals):
        precision_vals[num][0] = data_precision_vals[num * 2]
        precision_vals[num][1] = data_precision_vals[num * 2 + 1]

    # Clean up data
    for num, itrem in emumerate(precision_vals)

    # counter = 0
    # for a in range(0, 5):
    #     for b in range(0, 3):
    #         for c in range(0, 5):
    #             data_value[a, b, c] = Loss_vals_0[counter]
    #             counter += 1
    # print(data_value)

    # fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_axes([0.1, 0.1, 0.7, 0.8], projection='3d')
    # ax_cb = fig.add_axes([0.85, 0.25, 0.05, 0.5])
    # ax.set_aspect('auto')
    # ax.set_xlabel("Max Timeout")
    # ax.set_ylabel("Rounds")
    # ax.set_zlabel("Termination Accuracy")
    # ax.set_zlim(0.95, 1)
    # ax.set_title("Federated Learning Party 1 Precision Heatmap")

    # plotMatrix(ax, x, y, z, data_value, cmap=viridis, cax=ax_cb)

    plt.savefig("test.png")
    plt.show()
