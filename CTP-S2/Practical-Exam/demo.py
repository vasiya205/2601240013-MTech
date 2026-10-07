from customer_support import Stack, Queue, CustomerRequest

queue: Queue[CustomerRequest] = Queue()
stack: Stack[CustomerRequest] = Stack()

request1 = CustomerRequest(1, "Ravi", "Password Reset")
request2 = CustomerRequest(2, "Anu", "Payment Issue")
request3 = CustomerRequest(3, "Kiran", "Account Locked")

queue.enqueue(request1)
queue.enqueue(request2)
queue.enqueue(request3)

print("Front Request:", queue.front())

processed = queue.dequeue()
stack.push(processed)

processed = queue.dequeue()
stack.push(processed)

print("Recently Processed:", stack.peek())

print("Undo Request:", stack.pop())
