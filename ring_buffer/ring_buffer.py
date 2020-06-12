class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.position = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            # if buffer below capacity, add new item to tail
            self.storage.add_to_tail(item)
            self.position = self.storage.head
        else:
            if self.position.next is None:
                # update tail value and return position to start
                self.position.value = item
                self.position = self.storage.head
            else: # update position.value and move position
                self.position.value = item
                self.position = self.position.next

    def get(self):
        buffer_list = []
        position = self.storage.head
        # from head, append item values to buffer_list
        while position is not None:
            buffer_list.append(position.value)
            position = position.next

        return buffer_list

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1

        if not self.head: # and not self.tail
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

        else:
            self.head.insert_before(value)
            self.head = self.head.prev


    def remove_from_head(self):
        # if list is empty return None
        if not self.head:
            return None
        # if list has only one entry
        if not self.head.next:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.head.value
            self.head.next.prev = None
            self.length -= 1
            return value

    def add_to_tail(self, value):
        self.length += 1

        if not self.tail:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        # if empty return None
        if not self.tail:
            return None
        # if list has only one entry
        if not self.tail.prev:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.tail.value
            self.tail.prev.next = None
            self.length -= 1
            return value

    def move_to_front(self, node):
        value = node.value

        if not node.next:
            # if tail
            self.tail = node.prev
            node.prev.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.head.insert_before(value)
        self.head = self.head.prev

    def move_to_end(self, node):
        value = node.value

        if not node.prev:
            # if head
            self.head = node.next
            node.next.prev = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.tail.insert_after(value)
        self.tail = self.tail.next

    def delete(self, node):
        if self.length == 1:
            # if sole entry
            self.head = None
            self.tail = None
            self.length = 0
            return

        if not node.prev:
            # if head
            self.head = node.next
            node.next.prev = None
            self.length -= 1
            return

        if not node.next:
            # if tail
            self.tail = node.prev
            node.prev.next = None
            self.length -= 1
            return

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return