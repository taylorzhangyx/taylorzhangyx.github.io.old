# Message Queue

### What is Message Queue
Message queue is a queue that holds the message between client and server. This queue works as a buffer to hold the message for the server before the server is actually able to process it. By adding a message queue, the client can proceed without waiting for the server to finish process the request which speeded up the response time.

## What doest message queue solve
In the cases that the server is busy or not available, the requests from client need to be waited to be precessed by the server to get a 200 OK. Everything after getting the acknowledgement will be blocked if the server is too slow to consume the request, even if it is a drop and go request. By adding a message queue, the queue can buffer the messages for the server before it is processed. The client can send the request to the MQ and move on immediately after getting the OK from MQ instead of the server. Message queue will handle the consumption of the messages by server. It can solve that the message is not lost before the server consumes it. And it will hold the information about where this message is coming from in order to get the result back to the client after the server processes the message asynchronously.

## What UI approach can be taken when designing the work flow when MQ is involved
The true question is that do we want to pause the UI when the client try to post message to the MQ?
1. If we want to pause, then the UI will be hold and show up some spinner when the post is in progress. And only hide the spinner after the post is succeeded - acknowledgement is posted back to the client from MQ. The user will know that when the message is in the air and when the save is completed. Usually, only one message is designed to be posted at the same time in this case.
2. If we don't want the user to worry about the success of the post at all, we can hide the post notification. The client still need to post the message to the MQ but this case, since the user doesn't know the success of the post, they can post more than one messages at the same time. Thus the client need to build something extra to buffer the message or send multiple message at the same time to prevent failure.

## What performance problem could cause when using message queue?
Since an new layer is introduced between the client and the server, the actual response time is highly impacted.
1. Even the client can proceed without the server actually processes the message, but if the client cares about the result, the gap between sending the request and get the actual result of that request could be long.
2. This may varies depending on the actual implementation of the MQ, but the response time could be not consistent. Depending on the status of the actual server, some message may be routed to the faster and less busy server but some could be routed to a slow one. Then some client may complain that the server is slow.
3. The message queue could experience the back pressure. And if the back pressure is not handled well, there will be some data loss due to the queue is overwhelmed.
4. By introducing the MQ, one point of failure is introduced and once the MQ is failed, the data could be lost and hard  to recover.


## What is back pressure?
Back Pressure refers to the situation that the incoming data traffic is larger than the ability to process the data. For example, a server can only handle 5M requests per second, and there are 10M requests coming every second for 1 hour. We could use a message queue to buffer them but if the message queue is smaller than the data that's need to be buffered, some data could be overflow out of the queue and get lost.

## Kafka
[Kafka](https://www.youtube.com/watch?v=JalUUBKdcA0) is a data streaming system that could work as a message queue to handle the messages from client. Use pulling to handle messages. Run on top of ZooKeeper instance to achieve the high availability and stability.

### Basic Architecture
producer -> broker -> consumer

### Producer
Emits the message to broker.

### Consumer
PULL data from the data partition and consumes the message.

### Broker
Save the messages into different partitions and break the messages into chunks if needed.

## RabbitMQ
A simple queue implementation on the server side. Uses Pub/Sub to achieve high performance.

### Basic architecture
Publisher -> Exchange -> Consumer

### Publisher
Sends the messages to the exchange.

### Consumer
Read from the queue when a message push is received.

### Exchange
Takes the messages and PUSH them to different queues in a round robbin fashion.


## RabbitMQ vs Kafka
### Features
Apache Kafka — It is distributed. The data is shared and replicated with assured durability and availability.
RabbitMQ — It offers comparatively less support for these features.
### Performance rate
Apache Kafka — Its performance rate is high, up to 100,000 messages/second.
RabbitMQ — Whereas, the performance rate of RabbitMQ is around 20,000 messages/second.
### Processing
Apache Kafka — It allows reliable log distributed processing. Also, there exist stream processing semantics built into the Kafka Streams.
RabbitMQ — The consumer is just FIFO based, reading from the HEAD and processing sequentially.
