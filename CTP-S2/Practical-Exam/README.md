Q) A customer-support application needs reusable data structures to manage customer requests. 
Customer requests should be handled using a Queue, while recently processed requests can be maintained using a Stack for undo/review operations. 
Task: Develop a reusable Python package that implements Stack and Queue using type hints and dataclasses. 
The package should: Define a generic Stack class using type hints. 
Define a generic Queue class using type hints. Use dataclass where appropriate for storing request information. Implement push(), pop(), and peek() for Stack. 
Implement enqueue(), dequeue(), and front() for Queue. 
Handle empty Stack/Queue conditions appropriately. 
Organize the implementation as a reusable Python package. 
Create a separate test/demo program to import and use the package.

 ANSWERR:
 ----------
Customer Support - Stack and Queue

(1) aim:
To develop a reusable Python package that implements generic Stack and Queue data structures using type hints and dataclasses for managing customer support requests.

(2) DESCRIPTION:
The Stack follows the LIFO (Last In, First Out) principle and is used to maintain recently processed customer requests for undo or review operations. The Queue follows the FIFO (First In, First Out) principle and is used to handle customer requests in the order they arrive. Type hints provide type safety, while dataclasses are used to store customer request information.

(3) ALGORITHM:
1)Create a reusable Python package named customer_support.
2)Create a dataclass CustomerRequest to store request information.
3)Define a generic Stack class using type hints.
4)Implement push(), pop(), and peek() operations.
5)Handle the empty Stack condition appropriately.
6)Define a generic Queue class using type hints.
7)Implement enqueue(), dequeue(), and front() operations.
8)Handle the empty Queue condition appropriately.
9)Create a separate demo program.
10)Import Stack, Queue, and CustomerRequest from the package.
11)Add customer requests to the Queue.
12)Process requests and store them in the Stack.
13)Display the front request and recently processed request.

(4) SAMPLE OUTPUT:

Front Request: CustomerRequest(request_id=1, customer_name='Vasi', issue='Password Reset')

Recently Processed: CustomerRequest(request_id=2, customer_name='Mahee', issue='Payment Issue')

Undo Request: CustomerRequest(request_id=2, customer_name='Mahee', issue='Payment Issue')

(5) ANALYSIS and INFERENCE:
The project successfully demonstrates generic programming, type hints, dataclasses, Stack, Queue, and reusable Python package organization for a customer-support application.

