# What is a dead lock
Consider a case that A and B are shared resources. X and Y are running services that require resource A and B to work.
If X get A, then Y get B.
This time, X need to get B to proceed but not going to release A.
while Y need to get A to proceed but not going to release B.
Then here is a dead lock situation, no one can proceed.

# What to do to solve a deadlock
System to detect the safety of the system to tell if the resources if in a safe condition.
The system can monitor the resources and process to determine if the resource request will put the system into a unsafe condition.
If an unsafe condition can be prevented, a dead lock and be avoided.

# What to do to prevent a deadlock from happening
1. Ask the process to request the resource at once before start. If no enough resource available, put the process on hold until the resource need is met.
2. If the process can't get the resource, put the process on hold and release the resource that's holding by the process. When all the old and new resources are available, continue the process again.
3. Set the priority to all the resources, only allow process to get the resources by order.


# Deadlock prevention and deadlock avoidance
