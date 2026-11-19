## 1. For CPU bound work, synchronous processes are suitable because it uses threadpool
## 2. For I/O bound work, asynchronous processes are suitable because it uses an even loop (`one main thread` handles all the requests)
## 3. In python GIL is enforced 
    - GIL (Global Interpreter Lock) means that an instance of python code cannot be run by more than one thread simultaniously 
    - To achieve parallelism the python code should be run as multiple processes 
## 4. In FastAPI we use `await` which tells the os to pause the current request and execute some other ready request, in linux there is `epoll` which monitors the waiting request, if the data arrived to socket, `epoll` tells the os the request is ready to be executed.
## 5. In FastAPI for asynchronous calls it is mandatory to use functions/tools that are specifically defined like asyncio.time, httpx ect..
