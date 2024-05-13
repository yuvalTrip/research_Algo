import subprocess, sys
import time
import numpy as np
import cvxopt.glpk
from networkx.algorithms.approximation import min_weighted_vertex_cover

subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxopt"], stdout=subprocess.DEVNULL)
import cvxpy as cp


import networkx as nx, cvxpy as cp, numpy as np, matplotlib.pyplot as plt

def mincover(graph: nx.Graph)->int:
    # Create binary variable for each node- this will be the decision variable for the LP
    x = {node: cp.Variable(boolean=True) for node in graph.nodes}

    # Formulate the objective function: minimize the sum of x_i over all nodes
    objective = cp.Minimize(sum(x.values()))

    # Formulate the constraints: for each edge (u, v), x_u + x_v >= 1
    constraints = [x[u] + x[v] >= 1 for u, v in graph.edges]

    # Create the problem instance
    problem = cp.Problem(objective, constraints)

    # Solve the problem
    problem.solve(solver=cp.GLPK_MI)

    # Return the optimal value (minimum number of nodes in the vertex cover)
    return int(problem.value)

def test_mincover():
    for size in [10, 20, 30, 40, 50]:
        # Generate a random Erdos-Renyi graph
        graph_er = nx.erdos_renyi_graph(size, 0.2)
        result_er = mincover(graph_er)
       # result_networkx= min_weighted_vertex_cover(graph_er)
        print(
            f"Erdos-Renyi Graph Size: {size}x{size}, Minimum Vertex Cover: {result_er}")
        assert result_er <= size, f"Test failed for graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        min_vertex_cover = min_weighted_vertex_cover(graph_er)
        # Calculate the size of the minimum vertex cover
        min_vertex_cover_size = len(min_vertex_cover)
        assert result_er <= min_vertex_cover_size, f"Test failed for Erdos-Renyi graph size {size}x{size}: the real VC size is {min_vertex_cover_size}."

        # Generate a random Barabasi-Albert graph
        graph_ba = nx.barabasi_albert_graph(size, 3)
        result_ba = mincover(graph_ba)
        print(
            f"Barabasi-Albert Graph Size: {size}x{size}, Minimum Vertex Cover: {result_ba}")
        assert result_ba <= size, f"Test failed for Barabasi-Albert graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        min_vertex_cover = min_weighted_vertex_cover(graph_er)
        # Calculate the size of the minimum vertex cover
        min_vertex_cover_size = len(min_vertex_cover)
        assert result_ba <= min_vertex_cover_size, f"Test failed for Barabasi-Albert graph size {size}x{size}: the real VC size is {min_vertex_cover_size}."

        # Generate a random Watts-Strogatz graph
        graph_ws = nx.watts_strogatz_graph(size, 4, 0.3)
        result_ws = mincover(graph_ws)
        print(
            f"Watts-Strogatz Graph Size: {size}x{size}, Minimum Vertex Cover: {result_ws}")
        assert result_ws <= size, f"Test failed for Watts-Strogatz graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        min_vertex_cover = min_weighted_vertex_cover(graph_er)
        # Calculate the size of the minimum vertex cover
        min_vertex_cover_size = len(min_vertex_cover)
        assert result_ws <= min_vertex_cover_size, f"Test failed for Watts-Strogatz graph size {size}x{size}: the real VC size is {min_vertex_cover_size}."


if __name__ == '__main__':
#    print(cp.installed_solvers()) #internal checking because bug
   # edges=eval(input())
    #graph = nx.Graph(edges)
    #print(mincover((graph)))
    test_mincover()