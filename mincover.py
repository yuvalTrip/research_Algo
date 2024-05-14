import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxopt"], stdout=subprocess.DEVNULL)

import networkx as nx, cvxpy, numpy as np, matplotlib.pyplot as plt

def mincover(graph: nx.Graph)->int:
    # Create binary variable for each node- this will be the decision variable for the LP
    x = {node: cvxpy.Variable(boolean=True) for node in graph.nodes}

    # Formulate the objective function: minimize the sum of x_i over all nodes
    objective = cvxpy.Minimize(sum(x.values()))

    # Formulate the constraints: for each edge (u, v), x_u + x_v >= 1
    constraints = [x[u] + x[v] >= 1 for u, v in graph.edges]

    # Create the problem instance
    problem = cvxpy.Problem(objective, constraints)

    # Solve the problem
    problem.solve(solver=cvxpy.GLPK_MI)

    # Return the optimal value (minimum number of nodes in the vertex cover)
    return int(problem.value)

def test_mincover():
    for size in [10, 20, 30, 40, 50]:
        # Generate a random Erdos-Renyi graph
# Each pair of nodes is connected with a fixed probability, usually denoted as p.
# These graphs are characterized by a Poisson degree distribution, meaning most nodes have a similar number of connections.
        graph_er = nx.erdos_renyi_graph(size, 0.2)
        my_result_er = mincover(graph_er)
        #print(f"Erdos-Renyi Graph Size: {size}x{size}, Minimum Vertex Cover: {my_result_er}")
        assert my_result_er <= size, f"Test failed for graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        nx_result_er = nx.algorithms.approximation.min_weighted_vertex_cover(graph_er)
        # Calculate the size of the minimum vertex cover
        nx_result_er_size = len(nx_result_er)
        assert my_result_er <= nx_result_er_size, f"Test failed for Erdos-Renyi graph size {size}x{size}: the real VC size is {nx_result_er_size}."

        # Generate a random Barabasi-Albert graph
# In this model, nodes are added one at a time, and each new node connects to existing nodes with a probability that is proportional to their degree.
# This results in the formation of hubs, or highly connected nodes.
        graph_ba = nx.barabasi_albert_graph(size, 3)
        my_result_ba = mincover(graph_ba)
        #print(f"Barabasi-Albert Graph Size: {size}x{size}, Minimum Vertex Cover: {my_result_ba}")
        assert my_result_ba <= size, f"Test failed for Barabasi-Albert graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        nx_result_ba = nx.algorithms.approximation.min_weighted_vertex_cover(graph_ba)
        # Calculate the size of the minimum vertex cover
        nx_result_ba_final = len(nx_result_ba)
        assert my_result_ba <= nx_result_ba_final, f"Test failed for Barabasi-Albert graph size {size}x{size}: the real VC size is {nx_result_ba_final}."

        # Generate a random Watts-Strogatz graph
# The model starts with a regular ring lattice where each node is connected to its
# k nearest neighbors. Then, with a probability p, each edge is rewired to a random node, creating shortcuts in the network. This small-world property makes it a useful model for studying real-world networks like social networks and the internet.
        graph_ws = nx.watts_strogatz_graph(size, 4, 0.3)
        my_result_ws = mincover(graph_ws)
        #print(f"Watts-Strogatz Graph Size: {size}x{size}, Minimum Vertex Cover: {my_result_ws}")
        assert my_result_ws <= size, f"Test failed for Watts-Strogatz graph size {size}x{size}: Vertex cover size greater than number of nodes."
        # Find the minimum weighted vertex cover
        nx_result_ws = nx.algorithms.approximation.min_weighted_vertex_cover(graph_ws)
        # Calculate the size of the minimum vertex cover
        nx_result_ws_final = len(nx_result_ws)
        assert my_result_ws <= nx_result_ws_final, f"Test failed for Watts-Strogatz graph size {size}x{size}: the real VC size is {nx_result_ws_final} but you get {my_result_ws}."


if __name__ == '__main__':
   # print(cp.installed_solvers()) #internal checking because bug
    edges = eval(input())
    graph = nx.Graph(edges)
    print(mincover((graph)))
    # test_mincover()