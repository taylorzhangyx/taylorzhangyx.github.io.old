# Latency

A huge number of factors affect the network latency and the performance of the application. Here we are explaining some terminologies and things to consider when we talk about latency.

## TP99 & SLO

TP99 refers to the latency when the application serves 99% of the requests. So for example, there are 10000 requests a second to the server on average. Then if we sort the requests by the serving time/response time, the time to serve 9900th requests is the value of TP99. It describes the ability the server can serve the requests.

SLO(Serve Level Objective) is more focusing on the performance goal the serve is about to achieve. It has several parts: the latency as the objective, the percentage of user that is experiencing the latency longer than the objective. This could describe the current ability the server can handle.

## User Profile
Not all users have a great computer/phone. And not all users have a great network connectivity. When we design the system, the target user and the user's profile need to be considered to make sure our code/app can run on the client side smoothly.
The followings should be thought about:
- The power of user's machine
- User's network connectivity
- User's location, network restrictions and natural round trip latency
- The RAM and CPU capability of the user's machine
- The system of the user's machine, need to be compatible

## The infrastructure of the system
If the server side is a monolithic system, then it's fine to consider the performance as a whole. However, if the server is a micro-service system and the servers need to work together, the whole system latency need to be considered based on condition of all the micro servers. For instance, if every server has a SLO of 100ms for 1% users and there are 10 servers work together, then the latency for the whole system will be (1-.99**10) = 65%. So based on the system infrastructure, the SLO need to different for different servers.

## Stateless VS Stateful
The communication between the client and the server is better to be stateless especially if the network connectivity is poor since retries and lost connections could cause the stateful server to be confused and cause the system to be more complex. It costs a lot to maintain and recover the state itself.

