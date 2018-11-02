#Author: Elisabet Lopez
#CS 2302 10:30AM
#Instructor: Diego Aguirre
#T.A.: Manoj Pravaka Saha
#Lab Assignment 3 Option A
#Last modified: November 1, 2018

#Purpose: This program is a simple version of a Natural Language Processing (NLP) system.
#This program reads a file that contains words and their vector description (embedding) to
#construct either an AVL tree or a Red-Black Tree (the user is prompted to choose). This
#program uses the implementation provided in zyBooks for these two types of trees, but it
#adapts the code to include the word and its embedding. This program also reads a file 
#with pairs of words and computes their similarity using the cosine distance. This program
#includes methods to compute the number of nodes and the height of the tree,to generate a 
#file containing all the words stored in the tree in ascending order, and given a desired 
#depth, to generate a file with all the keys that have that depth in ascending order.

#from numpy import dot #dot product to calculate similiarity
#from numpy.linalg import norm #magnitude to calculate similarity
import AVLNode as AVL #class to create AVL nodes
import AVLTree as AVLTree #class for AVL tree
import RBTNode as RBT #class to create RBT nodes
import RBTree as RBTree #class for Red-Black tree
from math import sqrt
from time import clock #to calculate runtimes

#constructs AVL tree with words as keys
#O(nlogn)
def create_AVLtree(filename):
	with open(filename) as file:
		f = file.readlines()
		file.close()

	tree = AVLTree.AVLTree() #initialize tree

	for line in f:
		if line[0].isalpha() == False: #if word does not start with alphabetic character
			continue #ignore

		line = line.strip().split() #remove whitespace and separate each word
		word = line.pop(0) #word is first item in each line
		embedding = line #list of numbers

		node = AVL.AVLNode(word, embedding) #create node with word as key
		tree.insert(node) #use AVLTree class to insert node into AVL tree

	return tree

#constructs Red-Black tree with words as keys
#O(nlogn)
def create_RBtree(filename):
	with open(filename) as file:
		f = file.readlines()
		file.close()

	tree = RBTree.RedBlackTree() #initialize tree

	for line in f:
		if line[0].isalpha() == False: #if word does not start with alphabetic character
			continue #ignore

		line = line.strip().split() #remove whitespace and separate each word
		word = line.pop(0) #word is first item in each line
		embedding = line #list of numbers

		node = RBT.RBTNode(word, embedding, None) #create node with word as key
		tree.insert_node(node) #use AVLTree class to insert node into AVL tree

	return tree

#computes similarity of pairs of words from a file
#O(n^2)
def similarity(filename, tree):
	with open(filename) as file:
		f = file.readlines()
		file.close()

	for line in f:
		line = line.strip().split()
		w0 = line[0] #first word
		w1 = line[1] #second word

		e0 = tree.search(w0).embedding #embedding of first word
		e1 = tree.search(w1).embedding #embedding of second word

		dotproduct = dot_product(e0,e1)
		magnitude = get_magnitude(e0)*get_magnitude(e1) #product of magnitudes of both words

		sim = float(dotproduct)/float(magnitude)
		
		#a = [float(i) for i in e0] #to use with numpy; cast each number in embedding to float
		#b = [float(i) for i in e1] #to use with numpy; cast each number in embedding to float

		#sim = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)) #similarity using numpy

		print(w0 + " " + w1 + " " + str(sim)) #display similarity

#computes dot product of 2 vectors
#O(n)
def dot_product(a, b):
	dotproduct = 0
	for i in range(len(a)):
		dotproduct += float(a[i])*float(b[i])

	return dotproduct

#computes magnitude of a vector
#O(n)
def get_magnitude(x):
	sum_of_sqrs = 0
	for i in range(len(x)):
		sum_of_sqrs += float(x[i])**2 #square each number and add

	mag = sqrt(sum_of_sqrs) #take square root of sum

	return mag

#computes number of nodes in a tree
#O(n)
def num_nodes(root):
	if root == None:
		return 0
	return 1 + num_nodes(root.left) + num_nodes(root.right)

#computes height of tree
#O(n)
def height(x):
	if x == None:
		return -1
	return 1 + max(height(x.left), height(x.right))

#generates a file containing all words stored in the tree, in ascending order, one per line
#O(n)
def print_ascending(x):
	if x == None:
		return
	print_ascending(x.left)
	with open("words_in_ascending.txt", "a+") as outfile:
		outfile.write(x.word + "\n")
	print_ascending(x.right)

#given a desired depth, generates a file with all the keys that have that depth in ascending order
#O(n)
def ascending_at_depth(x, d):
	if x == None:
		return
	if d == 0: 
		with open("ascending_at_depth.txt", "a+") as outfile:
			outfile.write(x.word + "\n")
	#traverses depth level from left to right (ascending order)
	ascending_at_depth(x.left, d-1)
	ascending_at_depth(x.right, d-1)


def main():
	valid_input = False
	while valid_input == False: #while user does not enter AVL tree or Red-Black Tree
		tree = input("What type of tree would you like to use? AVL or Red-Black? ")
		if "avl" in tree.lower():
			valid_input = True
			tree = create_AVLtree("glove.6B.50d.txt")
		elif "red" in tree.lower():
			valid_input = True
			tree = create_RBtree("glove.6B.50d.txt")
		else:
			print("Please type either AVL or Red-Black. ")

	similarity("pairs_of_words.txt", tree) #replace with file name of file with pairs of words
	nodes = num_nodes(tree.root)
	h = height(tree.root)
	print_ascending(tree.root)
	ascending_at_depth(tree.root, 12)

main()
