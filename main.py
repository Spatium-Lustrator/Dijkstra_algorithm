from create_graph_helper import CreateGraphHelper
from dijkstra_algorithm_class import DijkstraAlgorithm

fill_arrays_helper = CreateGraphHelper()
graph = fill_arrays_helper.fill_graph_hash_table()
weights, parents = fill_arrays_helper.fill_weights_and_parents_hash_tables()

dijkstra_algorithm_executor = DijkstraAlgorithm(graph, weights, parents)
result = dijkstra_algorithm_executor.find_shortest_path()

print("Кратчайший путь составляет:", str(result))