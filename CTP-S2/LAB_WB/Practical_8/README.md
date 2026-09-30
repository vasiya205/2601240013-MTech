# Producer-Consumer Application using Threading

## Objective
To develop a concurrent Producer-Consumer application in Python using threading modules and thread-safe synchronization primitives.

## Algorithm
1. Initialize a bounded thread-safe queue as a shared buffer.
2. Define producer tasks to generate and enqueue items.
3. Define consumer tasks to dequeue and process items.
4. Start concurrent threads and synchronize completion using `.join()`.

## Input
* Shared buffer size limit (`maxsize=5`) and iteration count (`3` items per thread).

## Output
* Printed production and consumption logs verifying thread-safe item processing.

## Time & Space Complexity
* **Time Complexity**: $O(N)$ where $N$ is the total number of items produced and consumed.
* **Space Complexity**: $O(B)$ where $B$ is the maximum capacity of the queue buffer.
