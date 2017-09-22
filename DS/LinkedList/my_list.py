class node():
	def __init__(self, data=None):
		self.data = data
		self.next = None	

class linked_list():
	def __init__(self, head=None):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			cur = cur.next
			total += 1	
		return total

	def display(self):
		elems = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elems.append(cur.data)
		print elems

	def delete(self, index):
		idx = 0
		if index >= self.length():
			print "Error: index out of range"
			return False
		cur = self.head
		while True:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = cur.next
				return True
			idx += 1
		return False	
			
my_list = linked_list()
my_list.display()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

my_list.delete(2)

my_list.display()
