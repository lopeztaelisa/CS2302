class GraphALNode:
    def __init__(self, item, weight, next):
        self.item = item
        self.weight = weight
        self.next = next


class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        temp = self.adj_list[src]
        while temp != None:
            if temp.item == dest:
                return
            temp = temp.next
        self.adj_list[src] = GraphALNode(dest, weight, self.adj_list[src])

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, weight, self.adj_list[dest])

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    def get_highest_cost_edge(self):
        highest_cost_edge = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.weight > highest_cost_edge:
                    highest_cost_edge = temp.weight
                temp = temp.next

        return highest_cost_edge

    def get_num_edges(self):
        edges = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                edges += 1
                temp = temp.next

        if not self.is_directed:
            return edges//2
        return edges

    def get_edge_weight(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return 0 #edge not valid

        temp = self.adj_list[src]
        while temp != None:
            if temp.item == dest:
                return temp.weight
            temp = temp.next

        return 0 #edge not found

    """def reverse_edges(self):
        if not self.is_directed or len(self.adj_list) == 1:
            return"""

    def get_num_of_self_edges(self):
        self_edges = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp != None:
                if temp.item == i:
                    self_edges += 1
                    break #if self-edge found, continue to next list
                temp = temp.next

        return self_edges

    """def contains_cycle(self):"""

    def is_isolated(self, v):
        if not self.is_valid_vertex(v): #vertex not in the graph
            return None

        if (len(self.get_vertices_reachable_from(v)) == 0) and (len(self.get_vertices_that_point_to(v)) == 0):
            return True

        return False





