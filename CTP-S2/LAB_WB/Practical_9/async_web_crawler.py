import asyncio
import time

async def fetch_async(url: str, i: int):
    await asyncio.sleep(0.5)
    return f"Async Data: {url} (ID: {i})"

async def run_async_crawler(urls):
    start = time.time()
    results = await asyncio.gather(*(fetch_async(url, i) for i, url in enumerate(urls)))
    return results, time.time() - start

def run_sequential_crawler(urls):
    start = time.time()
    results = []
    for i, url in enumerate(urls):
        time.sleep(0.5)
        results.append(f"Seq Data: {url} (ID: {i})")
    return results, time.time() - start

if __name__ == "__main__":
    urls = [f"https://example.com/page{i}" for i in range(3)]
    
    async_res, async_time = asyncio.run(run_async_crawler(urls))
    seq_res, seq_time = run_sequential_crawler(urls)
    
    print("Async Output:", async_res, f"| Time: {async_time:.4f}s")
    print("Seq Output:  ", seq_res, f"| Time: {seq_time:.4f}s")
