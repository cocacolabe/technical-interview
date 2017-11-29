#!/usr/bin/env python


"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s.For example: if s = "udacity"
and t = "ad", then the
function returns True.Your
function definition should look like: question1(s, t) and
return a boolean True or False.
"""

def question1(s, t):
  l = len(t)
  dictT = {}
    for chr in t:
      if chr not in dictT.keys():
        dictT[chr] = 1
      else:
        dictT[chr] += 1
        
    for i in range(0, len(s)-l+1):
      subStr = s[i:i+l]
      subDic = {}
        for chr not in dictT.keys():
          break
        else:
          if chr not in subDic.keys():
            subDic[chr] = 1
          else:
            subDic[chr] += 1
      if subDic == dictT: return True
     return False

 print question1('','Empty')
 print question1('aa','aaccccc')
 print question1('Udacity','')

"""

Question 2
Given a string a, find the longest palindromic substring contained in a.Your
function definition should look like question2(a), and
return a string.

"""

def question2(a):

	def palindrome(s, p1, p2):
		l = p1
		r = p2
		n = len(s)
		while ((r <= n-1) & (l >= 0)):
			if (s[l] == s[r]):
				l-=1
				r+=1
			else:
				break
		return s[l+1:r]

	n = len(a)
	if (n==0): return ""
	longest = a[0]
	for i in range(0, n-1):
		pOne = palindrome(a, i, i)
		if (len(pOne) > len(longest)):
			longest = pOne
		pTwo = palindrome(a, i, i+1)
		if (len(pTwo) > len(longest)):
			longest = pTwo
	return longest

a = 'fdafjkdkjfdvbn'

print question2('abccbadef')
print question2(' ')
print question2('USDHSBufdsufhsudhsckasduhurqohcbsaqo')


"""

Question 3
Given an undirected graph G, find the minimum spanning tree within G.A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.Your
function should take in and
return an adjacency list structured like this:

  {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]
  }

Vertices are represented as unique strings.The
function definition should be question3(G)
"""


def question3(G):
    # G is dictionary
    if type(G) != dict:
        return "Error: G is not dictionary!"
    if len(G) < 2:
        return "Error: G has not enough vertices to form edges!"
    vertices = G.keys()
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    edges = sorted(list(edges))

    # loop through edges
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j

        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)

        if len(vertices) == 1:
            break
            
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph
            
    test = {'A': [('B', 2)],
            'B': [('A', 2), ('C', 5)],
            'C': [('B', 5)]}

print question3(test)
print question3('')

	
"""

Question 4
Find the least common ancestor between two nodes on a binary search tree.The least common ancestor is the farthest node from the root that is an ancestor of both nodes.For example, the root is a common ancestor of all nodes on the tree, but
if both nodes are descendents of the root 's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
  ],
  3,
  1,
  4)
and the answer would be 3.

 """

def question4(T, r, n1, n2):
    
    space = []
    while n1 != r:
        n1 = parent(T, n1)
        space.append(n1)
    if len(space) == 0:
        return -1
    while n2 != r:
        n2 = parent(T, n2)
        if n2 in space:
            return n2
    return -1
    
def parent(T, n):
	#return parent of n if it exists, otherwise return -1
    numrows = len(T)
    for i in range(numrows):
        if T[i][n] == 1:
            return i
    return -1


print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4)


"""

Question 5
Find the element in a singly linked list that 's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
  self.data = data
self.next = None

 """

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None 

def question5(ll, m):

	n1 = ll
	n2 = ll
	for i in range(0, m):
		if (n1 == None): 
			return None
		n1 = n1.next
	while (n1 != None):
		n1 = n1.next
		n2 = n2.next
	return n2.data

A = Node(2)
B = Node(3)
C = Node(8)
D = Node(1)
E = Node(6)

A.next = B 
B.next = C
C.next = D 
D.next = E

print question5(A, 3)
print question5(B, 1)
print question5(C, 2)

