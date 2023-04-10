import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colorbar
from matplotlib import cm
import pandas as pd

viridis = cm.get_cmap('plasma', 8)  # Our color map


def cuboid_data(center, size=(25, 1, 0.01)):
    # code taken from
    # http://stackoverflow.com/questions/30715083/python-plotting-a-wireframe-3d-cuboid?noredirect=1&lq=1
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point
    o = [a - b / 2 for a, b in zip(center, size)]
    # get the length, width, and height
    l, w, h = size
    x = np.array([[o[0], o[0] + l, o[0] + l, o[0], o[0]],      # x coordinate of points in bottom surface
                  # x coordinate of points in upper surface
                  [o[0], o[0] + l, o[0] + l, o[0], o[0]],
                  # x coordinate of points in outside surface
                  [o[0], o[0] + l, o[0] + l, o[0], o[0]],
                  [o[0], o[0] + l, o[0] + l, o[0], o[0]]])               # x coordinate of points in inside surface
    y = np.array([[o[1], o[1], o[1] + w, o[1] + w, o[1]],      # y coordinate of points in bottom surface
                  # y coordinate of points in upper surface
                  [o[1], o[1], o[1] + w, o[1] + w, o[1]],
                  # y coordinate of points in outside surface
                  [o[1], o[1], o[1], o[1], o[1]],
                  [o[1] + w, o[1] + w, o[1] + w, o[1] + w, o[1] + w]])   # y coordinate of points in inside surface
    z = np.array([[o[2], o[2], o[2], o[2], o[2]],              # z coordinate of points in bottom surface
                  # z coordinate of points in upper surface
                  [o[2] + h, o[2] + h, o[2] + h, o[2] + h, o[2] + h],
                  # z coordinate of points in outside surface
                  [o[2], o[2], o[2] + h, o[2] + h, o[2]],
                  [o[2], o[2], o[2] + h, o[2] + h, o[2]]])               # z coordinate of points in inside surface
    return x, y, z


def plotCubeAt(pos=(0, 0, 0), c="b", alpha=0.1, ax=None):
    # Plotting N cube elements at position pos
    if ax != None:
        X, Y, Z = cuboid_data((pos[0], pos[1], pos[2]))
        ax.plot_surface(X, Y, Z, color=c, rstride=1, cstride=1, alpha=0.1)


def plotMatrix(ax, x, y, z, data, cmap=viridis, cax=None, alpha=0.1):
    # plot a Matrix
    norm = matplotlib.colors.Normalize(vmin=data.min(), vmax=data.max())

    def colors(i, j, k): return matplotlib.cm.ScalarMappable(
        norm=norm, cmap=cmap).to_rgba(data[i, j, k])
    for i, xi in enumerate(x):
        for j, yi in enumerate(y):
            for k, zi, in enumerate(z):
                plotCubeAt(pos=(xi, yi, zi), c=colors(
                    i, j, k), alpha=alpha,  ax=ax)

    if cax != None:
        cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap,
                                                norm=norm,
                                                orientation='vertical')
        cbar.set_ticks(np.unique(data))
        # set the colorbar transparent as well
        cbar.solids.set(alpha=alpha)


if __name__ == '__main__':
    x = np.arange(0, 201, 25)
    y = np.array(range(1, 6))
    z = np.arange(0.9, 1.0, 0.01)

    df = pd.read_csv('log.csv')
    # print(df)
    Loss_vals = df.Loss
    # print(Loss_vals[0])

    data_value = np.zeros((len(x), len(y), len(z)))
    print(data_value.size)

    Loss_vals_0 = np.ones(450)
    # for num, item in enumerate(Loss_vals):
    for num in range(0, 11):
        Loss_vals_0[num] = Loss_vals[num * 2]

    # print(Loss_vals_0)

    counter = 0
    for a in range(0, 9):
        for b in range(0, 5):
            for c in range(0, 10):
                data_value[a, b, c] = Loss_vals_0[counter]
                counter += 1
    # print(data_value)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.8], projection='3d')
    ax_cb = fig.add_axes([0.9, 0.3, 0.05, 0.45])
    ax.set_aspect('auto')
    ax.set_xlabel("Max Timeout")
    ax.set_ylabel("Rounds")
    ax.set_zlabel("Termination Accuracy")
    ax.set_zlim(0.9, 1)

    plotMatrix(ax, x, y, z, data_value, cmap=viridis, cax=ax_cb)

    plt.savefig(__file__+".png")
    plt.show()
