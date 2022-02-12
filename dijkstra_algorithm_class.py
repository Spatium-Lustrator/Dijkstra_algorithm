class DijkstraAlgorithm:

    def __init__(self, graph, array_of_weights, array_of_parents):

        self.graph = graph
        self.weights = array_of_weights
        self.parents = array_of_parents

        self.processed = []

    def find_lowest_weight_node(self, array_of_weights):

        lowest_weight = float("inf")
        lowest_weight_node = None
        for node in array_of_weights:

            current_node_weight = array_of_weights[node]
            if current_node_weight < lowest_weight and node not in self.processed:

                lowest_weight = current_node_weight
                lowest_weight_node = node

        return lowest_weight_node

    def find_shortest_path(self):

        node = self.find_lowest_weight_node(self.weights)

        while node is not None:

            weight = self.weights[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():

                new_weight = weight + neighbors[neighbor]
                if self.weights[neighbor] > new_weight:

                    self.weights[neighbor] = new_weight
                    self.parents[neighbor] = node

            self.processed.append(node)
            node = self.find_lowest_weight_node(self.weights)

        return self.weights["finish"]