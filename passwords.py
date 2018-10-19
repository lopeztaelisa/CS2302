#Author: Elisabet Lopez
#CS 2302 10:30AM
#Instructor: Diego Aguirre
#T.A.: Manoj Pravaka Saha
#Lab Assignment 2 Option B
#Last modified: October 18, 2018

#Purpose: This program takes a file with a list of usernames followed by their passwords and finds and prints the 20 most used passwords.
#To accomplish this, this program creates a linked list of passwords without duplicates and with the count of the number of times
#each password appears in the file. To create this linked list, this program takes two different approaches: soultion A and
#solution B. This solutions differ in the approach to check for duplicates. To sort the lists, solution A uses bubble sort while solution
#B uses merge sort.

#Node class to create linked list
class Node(object): 
	password = ""
	count = -1
	next = None

	def __init__(self, password, count, next):
		self.password = password
		self.count = count
		self.next = next

#calls create_llist_A to create linked list
#calls bubble_sort to sort linked list
#prints 20 most used passwords along with the number of times they appear in the file
#O(n^2)
def solutionA(filename):
	llist = create_llist_A(filename) #create linked list without duplicates
	sorted_llist = bubble_sort(llist) #sort linked list using bubble sort

	#print 20 most used passwords along with number of times they appear in the file
	temp = sorted_llist
	for i in range(20):
		print(temp.password + " " + str(temp.count))
		temp = temp.next

#calls create_llist_B to create linked list
#calls merge_sort to sort linked list
#prints 20 most used passwords along with the number of times they appear in the file
#O(n)
def solutionB(filename):
	llist = create_llist_B(filename) #create linked list without duplicates
	sorted_llist = merge_sort(llist) #sort linked list using merge sort

	#prints 20 most used passwords along with the number of times they appear in the file
	temp = sorted_llist
	for i in range(20):
		print(temp.password + " " + str(temp.count))
		temp = temp.next

#creates linked list of nodes with unique passwords and count of how many times each password is in the file
#in order to avoid duplicate passwords, this function traverses the linked list to see if the password has been added already
#returns linked list
#O(n^2)
def create_llist_A(filename):
	head = None

	with open(filename, encoding = 'utf8', errors = 'ignore') as file: #open file, ignore encoding errors
		f = file.readlines() #read file line by line
		file.close() #close file

	#gets password
	for line in f:
		password = line.strip().split() #strip the line of whitespace and split into username and password
		if len(password) == 1: #if there is no password
			continue #skip it
		password = password[1] #password is the second element
		
		#creates linked list
		if head == None: #if linked list is empty
			head = Node(password, 1, None) #create head
			continue
		temp = head #begin traversal in search of password
		while temp.next != None and temp.password != password: #while the password has not been seen in the list
			temp = temp.next #traverse linked list
		if temp.password == password: #if password has been seen before
			temp.count += 1 #increase count of times it has been seen
			continue #continue to next password
		if temp.next == None: #if end of list was reached without finding password
			temp.next = Node(password, 1, None) #add node for password with count as 1

	return head

#creates linked list of nodes with unique passwords and count of how many times each password is in the file
#to avoid duplicate passwords,first a dictionary is created with passwords as keys and count of times it has been seen in the file as values
#the dictionary contents are then transferred to a linked list
#returns linked list
#O(n)
def create_llist_B(filename):
	passw_dict = {}

	with open(filename, encoding = 'utf8', errors = 'ignore') as file: #open file, ignore encoding errors
		f = file.readlines() #read file line by line
		file.close() #close file

		for line in f: 
			password = line.strip().split() #strip the line of whitespace and split into username and password
			if len(password) == 1: #if there is no password
				continue #skip it
			password = password[1] #password is the second element
			if password in passw_dict: #if password already in dictionary
				passw_dict[password] += 1 #increase the count by 1
			else: #if password is not in dictionary
				passw_dict[password] = 1 #add password to dictionary and initialize count to 1

	head = None #initialize linked list

	#creates linked list from passw_dict contents
	for password in passw_dict:
		if head == None:
			head = Node(password, passw_dict[password], None)
			temp = head
		else:
			temp.next = Node(password, passw_dict[password], None)
			temp = temp.next

	return head


#sorts a linked list in descending order using bubble sort algorithm
#O(n^2)
def bubble_sort(head):
	if head == None:
		return None

	curr = head
	last = None #keeps track of stopping point in each traversal

	while head != last: #while there are at least 2 elements left to sort
		while curr.next != last: #while curr is an element that has not been sorted
			if curr.count < curr.next.count: #if left element is less than right element
				#swap values
				temp_pass = curr.password #password of left element
				temp_count = curr.count #count of left element
				next_node = curr.next #right element
				curr.password = next_node.password #copy password from right element to left element
				curr.count = next_node.count #copy count from right element to left element
				next_node.password = temp_pass #copy password from left element to right element
				next_node.count = temp_count #copy count from left element to right element
			else: #if left element is greater than right element
				curr = curr.next #don't swap and continue traversal
		last = curr #move stopping point to last sorted element
		curr = head #traversal starts over

	return head

#sorts a linked list in descending order using merge sort algorithm
#O(nlogn)
def merge_sort(head):
	if (head == None) or (head.next == None): #if list is empty or size of list is 1
		return head #list is ordered

	slow = head
	fast = head.next
	
	#gets slow pointer to middle of list
	while (fast.next != None) and (fast.next.next != None):
		fast = fast.next.next
		slow = slow.next

	mid = slow.next
	slow.next = None #splits linked list in half

	sort_left = merge_sort(head) #recursivley split left half
	sort_right = merge_sort(mid) #recursivley split right half

	return merge(sort_left, sort_right) #merge left and right half sorted

#merges left and right halves of linked list
#O(n)
def merge(left, right):
	if left == None:
		return right
	if right == None:
		return left
	if left.count >= right.count:
		temp = left #add first element from left half to linked list
		temp.next = merge(left.next, right) #determine next element by recursively merging remaining elements
	else:
		temp = right #add first element from right half to linked list
		temp.next = merge(left, right.next) #determine next element by recursively merging remaining elements
	return temp




solutionA("test3.txt") #replace input file name
print('\n')
solutionB("test3.txt") #replace input file name
