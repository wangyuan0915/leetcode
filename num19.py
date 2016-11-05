class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def removeNthFromEnd(head, n):

	#get the lenght of list
	count = 1
	tmp = head
	while tmp.next != None:
		count += 1
		tmp = tmp.next

	order = count - n
	if order == 0:
		return head.next
	else:
		ct = 1
		tmp = head
		while ct < order:
			ct += 1
			tmp = tmp.next

		if tmp.next.next == None:
			tmp.next = None
			return head
		else:
			tmp.next = tmp.next.next
			return head







def printListNode(head):
	string = str(head.val) 
	tmp = head
	while(tmp.next != None):
		tmp = tmp.next
		string += str(tmp.val)
	print(string)





if __name__ == "__main__":
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(4)

	a.next = b
	b.next = c
	c.next = d

	printListNode(a)
	printListNode(removeNthFromEnd(a,4))

