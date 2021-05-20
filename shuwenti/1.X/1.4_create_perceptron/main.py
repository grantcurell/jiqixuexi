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
    f_data = (np.random.randint(low=BOUNDARY_SIZE*-1, high=BOUNDARY_SIZE, size=args.num_points),
              np.random.randint(low=BOUNDARY_SIZE*-1, high=BOUNDARY_SIZE, size=args.num_points))

    # Create the function f
    true_bias = np.random.randint(low=BIAS_RANGE*-1, high=BIAS_RANGE)
    true_weights = np.random.rand(1), np.random.rand(1)

    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    # Plot the data on the graph
    for x, y in zip(f_data[0], f_data[1]):

        if true_bias+true_weights[0]*x+true_weights[1]*y < 0:
            ax.scatter(x, y, alpha=0.8, c="red", edgecolors='none', s=30)
        else:
            ax.scatter(x, y, alpha=0.8, c="green", edgecolors='none', s=30)

    plt.plot(true_weights[0], true_weights[1])

    # This function draws 100 points between the two indicated ranges
    x = np.linspace(-1*BOUNDARY_SIZE, BOUNDARY_SIZE, 100)

    # See this post for how to calculate the line:
    # https://medium.com/@thomascountz/calculate-the-decision-boundary-of-a-single-perceptron-visualizing-linear-separability-c4d77099ef38
    # You first must calculate the x and y intercepts
    y = (-1 * (true_bias / true_weights[1]) / (true_bias / true_weights[0]))*x + ((-1*true_bias) / true_weights[1])
    plt.plot(x, y, color="blue", label="f")

    all_point_true = False

    while not all_point_true:
        print("NIL")

    plt.title('Perceptron Demonstration')
    plt.xlabel("Weight 1")
    plt.ylabel("Weight 2")
    plt.legend(loc=2)
    plt.show()
