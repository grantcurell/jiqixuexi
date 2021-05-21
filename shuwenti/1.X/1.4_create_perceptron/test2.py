import matplotlib.pyplot as plt
import numpy as np
import argparse


if __name__ == '__main__':

    plt.ion()

    BIAS_RANGE = 10  # Magic number for controlling the bias of the true function
    BOUNDARY_SIZE = 20  # Magic number which represents the maximum size of the ints generated

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--num-points", "-n", required=True, type=int, help="The number of points of data you would "
                                                                            "like to generate.")
    parser.add_argument("--start-weights", "-s", required=False, type=tuple, default=(1, 1),
                        help="A tuple containing the starting values for x and y you would like to use. Defaults to "
                             "(1, 1)")
    parser.add_argument("--bias", "-b", required=False, type=int, default=1,
                        help="The bias to use in the equation y=b+w1+w2. Keep in mind w could be negative. "
                             "The bias must be between -%s and %s" % (BIAS_RANGE, BIAS_RANGE))

    args = parser.parse_args()

    # Generate the data set
    f_data = [np.random.randint(low=BOUNDARY_SIZE*-1, high=BOUNDARY_SIZE, size=args.num_points),
              np.random.randint(low=BOUNDARY_SIZE*-1, high=BOUNDARY_SIZE, size=args.num_points)]

    # Create the function f
    if BIAS_RANGE != 0:
        true_bias = np.random.randint(low=BIAS_RANGE*-1, high=BIAS_RANGE)
    else:
        true_bias = 0
    true_weights = np.random.rand(1), np.random.rand(1)

    x = np.linspace(0, 10*np.pi, 100)
    y = np.sin(x)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    data_tags = []  # list of int used to track the data. Either -1 or 1. This is the same as y

    # Plot the data on the graph
    for x1, x2 in zip(f_data[0], f_data[1]):

        if true_bias+true_weights[0]*x1+true_weights[1]*x2 < 0:
            ax.scatter(x1, x2, alpha=0.8, c="red", edgecolors='none', s=30)
            data_tags.append(-1)
        else:
            ax.scatter(x1, x2, alpha=0.8, c="green", edgecolors='none', s=30)
            data_tags.append(1)

        fig.canvas.draw()

    """
    for phase in np.linspace(0, 10*np.pi, 100):
        line1.set_ydata(np.sin(0.5 * x + phase))
        fig.canvas.draw()
    """
