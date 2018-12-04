from GraphAL import GraphAL
from Algorithms import kruskal, topological_sort

graph = GraphAL(initial_num_vertices=4, is_directed=False)

graph.add_edge(0, 1, 6)
graph.add_edge(1, 3, 4)
graph.add_edge(0, 2, 1)

graph.add_edge(0, 3, 3)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 2)

min_spannig_tree = kruskal(graph)
for i in min_spannig_tree:
	print(i)

print('\n')

graph = GraphAL(initial_num_vertices=10, is_directed=False)

graph.add_edge(0,1,4)
graph.add_edge(1,2,4)
graph.add_edge(2,3,8)
graph.add_edge(0,4,3)
graph.add_edge(4,1,2)
graph.add_edge(1,5,5)
graph.add_edge(5,2,6)
graph.add_edge(2,6,9)
graph.add_edge(6,3,13)
graph.add_edge(4,5,12)
graph.add_edge(5,6,17)
graph.add_edge(3,9,20)
graph.add_edge(9,6,15)
graph.add_edge(6,8,10)
graph.add_edge(8,5,11)
graph.add_edge(5,7,21)
graph.add_edge(7,4,1)
graph.add_edge(7,8,14)
graph.add_edge(8,9,16)

min_spannig_tree = kruskal(graph)
for i in min_spannig_tree:
	print(i)

print('\n')

graph = GraphAL(initial_num_vertices=8, is_directed=False)

graph.add_edge(0,1,2)
graph.add_edge(1,2,9)
graph.add_edge(2,3,10)
graph.add_edge(0,4,3)
graph.add_edge(4,1,6)
graph.add_edge(1,5,8)
graph.add_edge(5,2,7)
graph.add_edge(2,6,15)
graph.add_edge(6,3,16)
graph.add_edge(4,5,1)
graph.add_edge(5,6,12)
graph.add_edge(4,7,4)
graph.add_edge(5,7,11)
graph.add_edge(7,6,13)

min_spannig_tree = kruskal(graph)
for i in min_spannig_tree:
	print(i)

print('\n')

graph = GraphAL(initial_num_vertices=7, is_directed=True)

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(0,4)
graph.add_edge(4,1)
graph.add_edge(5,1)
graph.add_edge(4,5)
graph.add_edge(5,3)
graph.add_edge(5,6)
graph.add_edge(3,6)

sorted_vert = topological_sort(graph)
print(sorted_vert)

print('\n')

graph = GraphAL(initial_num_vertices=9, is_directed=True)

graph.add_edge(0,1)
graph.add_edge(2,1)
graph.add_edge(3,2)
graph.add_edge(4,0)
graph.add_edge(4,1)
graph.add_edge(5,1)
graph.add_edge(5,2)
graph.add_edge(6,2)
graph.add_edge(3,6)
graph.add_edge(4,5)
graph.add_edge(6,5)
graph.add_edge(4,7)
graph.add_edge(5,7)
graph.add_edge(8,5)
graph.add_edge(6,8)
graph.add_edge(8,7)

sorted_vert = topological_sort(graph)
print(sorted_vert)