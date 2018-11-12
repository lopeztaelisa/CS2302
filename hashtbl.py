#Author: Elisabet Lopez
#CS 2302 10:30AM
#Instructor: Diego Aguirre
#T.A.: Manoj Pravaka Saha
#Lab Assignment 4 Option A
#Last modified: November 11, 2018

#Purpose: This program creates a hash table to store words and their vector description (embedding).
#The hash table solves collisions by chaining. This program includes multiple hash functions. This
#program also computes the load factor of a hash table.

#class to create hash table node
class HTNode:
    def __init__(self, word, embedding, next):
        self.word = word
        self.embedding = embedding
        self.next = next

#class to create hash table; includes hash functions
class HashTable:

	def __init__(self, table_size):
		self.table = [None] * table_size


	def hash1(self, k):
		word_int = 0
		for char in k:
			word_int += ord(char) #adds up ASCII values of each character

		return word_int % len(self.table)

	def hash2(self, k):
		word_base_26 = 0
		for i in range(len(k)-1, -1, -1):
			char_base_26 = ord(k[i].lower())-97 #converts character base 26 to base 10
			char_base_26 = abs(char_base_26) #handles special characters that end up as negative numbers
			word_base_26 += char_base_26 * (26 ** len(k)-1-i) #converts entire word base 26 to base 10
			if word_base_26 >= len(self.table):
				word_base_26 = 0

		return word_base_26

	#better hash function
	def hash3(self, k):
		word_base_26 = 0
		for i in range(len(k)-1, -1, -1):
			char_base_26 = ord(k[i].lower())-97 #converts character base 26 to base 10
			char_base_26 = abs(char_base_26) #handles special characters that end up as negative numbers
			word_base_26 += char_base_26 * (26 ** len(k)-1-i) #converts entire word base 26 to base 10

		return word_base_26 % len(self.table)


#creates and populates hash table
def create_HT(filename):
	with open(filename) as file:
		f = file.readlines()
		file.close()

	size = (400000//10)+1
	H = HashTable(size) #initializes hash table

	for line in f:
		if line[0].isalpha() == False: #if word does not start with alphabetic character
			continue #ignore

		line = line.strip().split() #remove whitespace and separate each word
		word = line.pop(0) #word is first item in each line
		embedding = line #list of numbers

		insert(H, word, embedding) #insert word in hash table

	return H

#inserts a word into hash table
def insert(H, word, embedding):
	loc = H.hash3(word) #get corresponding bucket
	H.table[loc] = HTNode(word, embedding, H.table[loc]) #create node and insert in table

#computes load factor (average list size) of a hash table
def load_factor(h):
	elem = 0

	#traverses buckets
	for i in range(len(h.table)):
		temp = h.table[i]
		while temp != None: #traverses linked list in bucket
			elem += 1
			temp = temp.next

	return elem/len(h.table)

#prints all buckets and their contents from hash table
def print_HT(H):
	for bucket in range(len(H.table)):
		print(str(bucket) + ": ", end=" ")
		temp = H.table[bucket]
		while temp != None:
			print(temp.word, end=" ")
			temp = temp.next
		print('\n')

#counts how many empty buckets there are in hash table
def empty_buckets(H):
	empty = 0
	for i in range(len(H.table)):
		if H.table[i] == None:
			empty += 1

	return empty

H = create_HT("glove.6B.50d.txt") #creates hash table
print_HT(H) #prints hash table contents
print(empty_buckets(H)) #prints number of empty buckets
print(load_factor(H)) #prints load factor of hash table
