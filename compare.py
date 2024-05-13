import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
import time
import matplotlib
matplotlib.use('TkAgg')  # or any other suitable backend


def solve_with_root(a: np.ndarray, b: np.ndarray):
    """
    Solves the linear equation Ax = b using scipy.optimize.root.

    Parameters:
    a (np.ndarray): Coefficient matrix.
    b (np.ndarray): Right-hand side vector.

    Returns:
    np.ndarray: Solution vector x.


     >>> a = np.array([[1, 2], [3, 4]])
    >>> b = np.array([5, 6])
    >>> solve_with_root(a, b)
    array([-4. ,  4.5])

     >>> a = np.array([[1]])
    >>> b = np.array([1])
    >>> solve_with_root(a, b)
    array([1.])

    >>> a = np.array([[0]])
    >>> b = np.array([0])
    >>> solve_with_root(a, b)
    array([0.])

    >>> a = np.array([[0, 0], [0, 0]])
    >>> b = np.array([0, 0])
    >>> solve_with_root(a, b)
    array([0., 0.])
    """

    # Define the equation to be solved by scipy.optimize.root
    def equation(x):
        return np.dot(a, x) - b
    # Use scipy.optimize.root to solve the equation
    sol = root(equation, np.zeros_like(b))
    return sol.x# Return the solution vector


def test_solve_with_root():
    """
    Test the solve_with_root function by comparing its result with numpy.linalg.solve.
    """
    # Perform the test 10 times
    for _ in range(10):
        size = np.random.randint(1, 10)# Generate a random size for the coefficient matrix
        a = np.random.rand(size, size)# Generate a random coefficient matrix
        b = np.random.rand(size)# Generate a random right-hand side vector

        # Solve the equation using scipy.optimize.root
        x_root = solve_with_root(a, b)

        # Solve the equation using numpy.linalg.solve
        x_numpy = np.linalg.solve(a, b)

        # Check if the solutions are close
        assert np.allclose(x_root, x_numpy)


def compare_solution_methods():
    """
    Compare the performance of solve_with_root and numpy.linalg.solve on random inputs of different sizes.

    This function generates random inputs of varying sizes, solves the linear equations using both
    solve_with_root and numpy.linalg.solve, and measures the running time for each method. It then
    plots the average running time as a function of the input size.
    """
    # Generate input sizes from 1 to 1000 with a step size of 50
    sizes = np.arange(1, 1001, 50)
    # List to store running times for solve_with_root
    root_times = []
    # List to store running times for numpy.linalg.solve
    numpy_times = []

    # Loop through different input sizes
    for size in sizes:
        a = np.random.rand(size, size) # Generate a random coefficient matrix of size 'size x size'
        b = np.random.rand(size) # Generate a random right-hand side vector of length 'size'

        # Measure the running time for solve_with_root
        start_time = time.time()
        solve_with_root(a, b)
        root_times.append(time.time() - start_time)

        # Measure the running time for numpy.linalg.solve
        start_time = time.time()
        np.linalg.solve(a, b)
        numpy_times.append(time.time() - start_time)

    # Plot the running times for both methods
    plt.plot(sizes, root_times, label='solve_with_root')
    plt.plot(sizes, numpy_times, label='numpy.linalg.solve')
    plt.xlabel('Input Size') # Set label for x-axis
    plt.ylabel('Running Time (s)') # Set label for y-axis
    plt.title('Comparison of Solution Methods')
    plt.legend()
    plt.savefig("comparison.png")  # after you plot the graphs, save them to a file and upload it separately.
    plt.show() # this should show the plot on your screen


if __name__ == '__main__':
    test_solve_with_root()
    compare_solution_methods()