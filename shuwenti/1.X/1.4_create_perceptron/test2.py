import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    plt.ion()

    ########################################
    # Generate some scatterplot and a line #
    ########################################

    # Generate the data set
    f_data = [np.random.randint(low=10*-1, high=10, size=30),
              np.random.randint(low=10*-1, high=10, size=30)]

    x = np.linspace(0, 10*np.pi, 100)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    true_weights = np.random.rand(1), np.random.rand(1)

    # Plot the data on the graph
    for x1, x2 in zip(f_data[0], f_data[1]):

        if 5+true_weights[0]*x1+true_weights[1]*x2 < 0:
            ax.scatter(x1, x2, alpha=0.8, c="red", edgecolors='none', s=30)
        else:
            ax.scatter(x1, x2, alpha=0.8, c="green", edgecolors='none', s=30)

        fig.canvas.draw()

    y = (-1 * (5 / true_weights[1]) / (5 / true_weights[0])) * x \
        + ((-1 * 5) / true_weights[1])

    true_f, = ax.plot(x, y, color="blue", label="f")
    true_f.set_ydata(y)
    plt.xlabel("Weight 1")
    plt.ylabel("Weight 2")
    plt.legend(loc=2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.title('Double Line Problem')
    plt.pause(.05)
    fig.canvas.draw()

    ##########################
    # Generate a second line #
    ##########################

    y2 = x
    second_line, = ax.plot(x, y2, color="purple", label="h")
    second_line.set_ydata(y2)
    plt.pause(1)
    fig.canvas.draw()
