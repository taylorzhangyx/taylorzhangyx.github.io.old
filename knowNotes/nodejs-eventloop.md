event loop

message queue

command orders

worker thread

stack

fork process


https://blog.logrocket.com/node-js-multithreading-what-are-worker-threads-and-why-do-they-matter-48ab102f8b10/
https://nodejs.org/docs/latest-v10.x/api/worker_threads.html
https://flaviocopes.com/node-event-loop/#the-call-stack
https://nodesource.com/blog/worker-threads-nodejs/
https://stackoverflow.com/questions/56656498/how-is-cluster-and-worker-threads-work-in-node-js


https://blog.insiderattack.net/deep-dive-into-worker-threads-in-node-js-e75e10546b11

Why do we want thread pooling when using worker thread?

One process which have multiple threads can run on multiple cores at the same time.


In Node.js, each worker will have its own instance of V8 and Event Loop. However, unlike child processes, Workers can share memory.
