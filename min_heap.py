#Author: Elisabet Lopez
#CS 2302 10:30AM
#Instructor: Diego Aguirre
#T.A.: Manoj Pravaka Saha
#Lab Assignment 5 Option A
#Last modified: November 27, 2018

#Purpose: This program is an implementation of a min-heap. It contains methods
#to insert an element, extract the minimum element, and check if heap is empty.
#This program also uses the min-heap implementation to implement heapsort.

#heap implementation
class Heap:
	def __init__(self):
		self.heap_array = []

	#inserts element and percolates up to maintain min-heap property
	#O(logn)
	def insert(self, k):
		self.heap_array.append(k) #insert at end/leftmost leaf

		#percolate up
		i = len(self.heap_array)-1 #index of k
		parent = (i-1)//2
		#while the root is not reached and min-heap property is violated
		while (i > 0) and (self.heap_array[parent] > self.heap_array[i]): 
			temp = self.heap_array[parent]
			self.heap_array[parent] = self.heap_array[i]
			self.heap_array[i] = temp

			i = parent #repeat percolate up from new position (parent index)
			parent = (i-1)//2 #update parent index

	#extracts minimum value (root), replaces it with last element, 
	#and percolates down to maintain min-heap property
	#O(logn)
	def extract_min(self):
		if self.is_empty():
			return None

		if len(self.heap_array) == 1: #if min-heap has only 1 element
			return self.heap_array.pop() #remove and return root

		min_elem = self.heap_array[0] #get root
		self.heap_array[0] = self.heap_array.pop() #removes and returns last element

		curr_i = 0 #current index
		child = (2*curr_i) + 1 #left child of current index
		value = self.heap_array[curr_i] #value of current node

		#percolate down
		while child < len(self.heap_array): #while current node has left child
			min_val = value #minimum value so far
			min_i = -1 #index of minimum value
			
			i=0
			while i < 2 and child+i < len(self.heap_array): #while current node has children
				if self.heap_array[child+i] < min_val: #if child is less than minimum value so far
					min_val = self.heap_array[child+i] #update minimum value
					min_i = child + i #update index of minimum value
				i = i + 1 #check next child

			if min_val == value: #min-heap property is not violated
				break
			else: #swap
				temp = self.heap_array[curr_i]
				self.heap_array[curr_i] = self.heap_array[min_i]
				self.heap_array[min_i] = temp

				curr_i = min_i #repeat from new position
				child = (2*curr_i) + 1 #update left child

		return min_elem

	#determines whether heap is empty or not
	#O(1)
	def is_empty(self):
		return len(self.heap_array) == 0

#sorts a list from a CSV file using heapsort
#O(nlogn)
def heapsort(filename):
	#reads file
	with open(filename) as file:
		lst = file.read().split(',')#splits elements at commas
		file.close()

	heap = Heap() #initialize heap
	result = [] #sorted result

	#populate heap
	for num in lst:
		heap.insert(int(num))

	#sort in ascending order
	while not heap.is_empty():
		result.append(heap.extract_min())

	return result

sorted_list = heapsort("heapsort_test.txt") #replace with CSV filename
for i in sorted_list:
	print(i,end=" ")
