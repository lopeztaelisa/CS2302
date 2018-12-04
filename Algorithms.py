#Author: Elisabet Lopez
#CS 2302 10:30AM
#Instructor: Diego Aguirre
#T.A.: Manoj Pravaka Saha
#Lab Assignment 5 Option A
#Last modified: December 4, 2018

#Purpose: This program is an implementation of Kruskal's algorithm to find a minimum spanning tree and of
#Topological sort to sort the edges of a graph.

from GraphAL import GraphAL #adjacency list
from DSF import DisjointSetForest #disjoint set forest
from queue import *

#returns minimum spanning tree using Kruskal's algorithm
#assumes graph is undirected and represented with an adjacency list
def kruskal(graph):
	edges = get_edges(graph)
	edges = sorted(edges, key=lambda edge: edge[2]) #sorts edges by weight in ascending order
	T=[] #minimum spanning tree edges

	dsf = DisjointSetForest(graph.get_num_vertices())

	#checks for cycles using disjoint set forest data structure
	for edge in edges:
		if dsf.find(edge[0]) != dsf.find(edge[1]): #if edge does not make a cycles
			dsf.union(edge[0], edge[1]) #add to set
			T.append(edge) #add to minimum spanning tree

	return T

#returns list of edges of graph in the form of [source, destination, weight]
def get_edges(graph):
	edges = []

	for src in range(len(graph.adj_list)):
		temp = graph.adj_list[src]

		while temp != None:
			if [temp.item, src, temp.weight] not in edges: #graph is undirected and we only need an edge once
				edges.append([src, temp.item, temp.weight])
			temp = temp.next

	return edges

#returns an ordering of the vertices such that if there is a path from u to v, u is before v in the ordering
#assumes graph is directed
def topological_sort(graph):
	in_degrees = get_indegree_of_each_vertex(graph)
	sorted_result = []

	q = [] #queue

	for i in range(len(in_degrees)):
		if in_degrees[i] == 0:
			q.append(i) #enqueue

	while len(q) > 0:
		u = q.pop(0) #dequeue

		sorted_result.append(u)

		for adj_vertex in graph.get_vertices_reachable_from(u):
			in_degrees[adj_vertex] -= 1

			if in_degrees[adj_vertex] == 0:
				q.append(adj_vertex)

	if len(sorted_result) != graph.get_num_vertices(): #cycle was found
		return None #invalid because graph must be acylic

	return sorted_result

#returns a dictionary with all vertices and their in degree
def get_indegree_of_each_vertex(graph):
	in_degrees = []

	for v in range(graph.get_num_vertices()):
		in_degrees.append(len(graph.get_vertices_that_point_to(v)))

	return in_degrees


