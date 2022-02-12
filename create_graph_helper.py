class CreateGraphHelper:

    def __init__(self):

        self.graph = {}
        self.weights = {}
        self.parents = {}

    def fill_graph_hash_table(self):

        count_of_nodes = int(input("Кол-во узлов в графе, учитывая стартовый и конечный узлы: "))

        for node in range(count_of_nodes):

            name_of_current_node = input("Введите название текущего узла: ")
            self.graph[name_of_current_node] = {}
            count_of_neighbors = int(input("Кол-во соседних узлов: "))

            for neighbor in range(count_of_neighbors):
                name_of_current_neighbor = input("Введите название текущего узла-соседа: ")
                weight_of_current_neighbor = int(input("Введите вес для достижения узла: "))
                self.graph[name_of_current_node][name_of_current_neighbor] = weight_of_current_neighbor

        return self.graph

    def fill_weights_and_parents_hash_tables(self):

        infinity = float("inf")

        for key in self.graph.keys():

            if key != "start":
                self.weights[key] = infinity
                self.parents[key] = None

        count_of_nodes_able_from_start = int(
            input("Введите кол-во узлов, в которые можно попасть из начального узла: "))

        for key in self.weights.keys():

            if count_of_nodes_able_from_start <= 0:
                break

            current_key_weight = int(input("Введите вес для достижения узла '%s' из начального узла: " % key))

            self.weights[key] = current_key_weight
            self.parents[key] = "start"

            count_of_nodes_able_from_start -= 1

        return self.weights, self.parents
