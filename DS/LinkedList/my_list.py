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

	def display(self):
		elems = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elems.append(cur.data)
		print elems

my_list = linked_list()
my_list.display()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
