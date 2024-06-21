class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DLLStack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def pop(self):
        if not self.tail:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value
    
    def peek(self):
        return self.tail.value if self.tail else None
    
    def is_empty(self):
        return self.head is None

s = input()
st = DLLStack()
positions = DLLStack()

for index, char in enumerate(s):
    if char in "{[(":
        st.push(char)
        positions.push(index + 1)  # Store position (1-based index)
    elif char in "}])":
        if st.is_empty():
            print(f"False at position {index + 1}")
            break
        elif (char == ')' and st.peek() == '(') or \
             (char == ']' and st.peek() == '[') or \
             (char == '}' and st.peek() == '{'):
            st.pop()
            positions.pop()
        else:
            print(f"False at position {index + 1}")
            break
else:
    if st.is_empty():
        print(-1)  # Balanced
    else:
        print(f"False at position {positions.peek()}")
