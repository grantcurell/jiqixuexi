import numpy as np
import argparse
import matplotlib.pyplot as plt

if __name__ == '__main__':

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
    f_data = [np.random.randint(low=BOUNDARY_SIZE * -1, high=BOUNDARY_SIZE, size=args.num_points),
              np.random.randint(low=BOUNDARY_SIZE * -1, high=BOUNDARY_SIZE, size=args.num_points)]

    # Create the function f
    if BIAS_RANGE != 0:
        true_bias = np.random.randint(low=BIAS_RANGE * -1, high=BIAS_RANGE)
    else:
        true_bias = 0
    true_weights = np.random.rand(1), np.random.rand(1)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    data_tags = []  # list of int used to track the data. Either -1 or 1. This is the same as y

    # Plot the data on the graph
    for x1, x2 in zip(f_data[0], f_data[1]):

        if true_bias + true_weights[0] * x1 + true_weights[1] * x2 < 0:
            ax.scatter(x1, x2, alpha=0.8, c="red", edgecolors='none', s=30)
            data_tags.append(-1)
        else:
            ax.scatter(x1, x2, alpha=0.8, c="green", edgecolors='none', s=30)
            data_tags.append(1)

        fig.canvas.draw()

    f_data.append(data_tags)

    # This function draws 100 points between the two indicated ranges
    x = np.linspace(-1 * BOUNDARY_SIZE, BOUNDARY_SIZE, 100)

    # See this post for how to calculate the line:
    # https://medium.com/@thomascountz/calculate-the-decision-boundary-of-a-single-perceptron-visualizing-linear-separability-c4d77099ef38
    # You first must calculate the x and y intercepts. Do not confuse the nomenclature here. I used y, but x and y here
    # really correspond to x1 and x2 data respectively.
    if true_bias != 0:
        y = (-1 * (true_bias / true_weights[1]) / (true_bias / true_weights[0])) * x \
            + ((-1 * true_bias) / true_weights[1])
    else:
        y = -1 * (true_weights[0] * x) / true_weights[1]

    true_f, = ax.plot(x, y, color="blue", label="f")
    true_f.set_ydata(y)
    plt.xlabel("Weight 1")
    plt.ylabel("Weight 2")
    plt.legend(loc=2)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.title('Perceptron Demonstration')

    # Create and run our perceptron algorithm
    all_point_true = False

    # The first element here is our starting bias. The other two correspond to the two weights
    perceptron_weights = [np.random.randint(low=BIAS_RANGE * -1, high=BIAS_RANGE),
                          np.random.rand(1),
                          np.random.rand(1)]

    iterations = 0

    while not all_point_true:

        bad_point = None

        # Find a point which our algorithm guessed incorrectly
        for x1, x2, y_perceptron in zip(f_data[0], f_data[1], f_data[2]):

            if perceptron_weights[0] + perceptron_weights[1] * x1 + perceptron_weights[2] * x2 < 0:
                if y_perceptron == 1:
                    bad_point = [x1, x2, y_perceptron]
                    break
            else:
                if y_perceptron == -1:
                    bad_point = [x1, x2, y_perceptron]
                    break

        # If no bad point was found exit. This means our algorithm got them all correct!
        if not bad_point:
            print("Learning complete! Iterations required was %s" % iterations)
            break

        iterations = iterations + 1
        print("Bad point found. Iteration is %s" % iterations)
        x_t = bad_point[:2]
        x_t.insert(0, 1)

        y_times_x = np.dot(bad_point[2], x_t)
        perceptron_weights = np.add(y_times_x, perceptron_weights)

        if perceptron_weights[0] == 0:
            y_perceptron = -1 * (perceptron_weights[1] * x) / perceptron_weights[2]
        else:
            y_perceptron = (-1 * (perceptron_weights[0] / perceptron_weights[2]) / (perceptron_weights[0] /
                                                                                    perceptron_weights[1])) * x \
                           + ((-1 * perceptron_weights[0]) / perceptron_weights[2])

        perceptron_line, = ax.plot(x, y_perceptron, color="purple", label="h")
        perceptron_line.set_ydata(y_perceptron)
        plt.pause(1)
        fig.canvas.draw()
