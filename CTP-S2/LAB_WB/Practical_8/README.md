# Asynchronous Web Crawler vs Sequential Implementation

## Objective
To develop an asynchronous web crawler using `asyncio` and `aiohttp` to perform non-blocking concurrent network requests and compare its execution performance against a sequential implementation[cite: 3, 33].

## Algorithm
1. Import `asyncio`, `aiohttp`, and `time` modules.
2. Define a sequential crawler function for blocking requests.
3. Define an asynchronous crawler function using `asyncio.gather` for concurrent fetching[cite: 3, 33].
4. Implement retry mechanisms and exception handling for network requests.
5. Run both implementations and compare total execution times.

## Input
* A list of target URLs (`https://example.com/page0` to `page2`).

## Output
* Crawled data results and execution runtime durations for both asynchronous and sequential approaches.

## Time & Space Complexity
* **Time Complexity**: 
  * *Sequential*: $O(N \times T)$ where $N$ is URLs and $T$ is request delay.
  * *Asynchronous*: O(T) bounded by the longest individual request.
* **Space Complexity**: O(N) to store the result collection list.
