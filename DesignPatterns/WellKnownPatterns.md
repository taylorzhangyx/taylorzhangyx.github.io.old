# 1st Tier - Well Known and Most Used
The following patterns are well known and really effective to be used in the code base to make it more readable and easy to manage.

## Composed Method
Encapsulate calls of a small number of coherent elements into a method.

### When to use
This is most used when you want to make the code more readable. Sometimes the code shows a manipulation in such a low level that is hard to understand. For instance, `cur[i] = temp[l-1] + k[m]', which is so hard to follow the meaning if you lose the context. Composed Method can make the code more readable and scannable by either adding the documentation or abstracting the logical related code into a composed method.

### Benefits
1. Make the code more readable and scannable.
2. Easy to follow the logic and algorithms.
3. Make it possible to refactor the code into a package or class in the future.
4. Save the space for adding the documentation.

## Creation Method
Use method instead of Constructors to produce new object.
Also known as **Factory Method** or **Static Factory Method**.

### When to use
When the creation of an object is often get used and the object need a little bit tweak that the plain constructor is hard to reflect the intention. For instance,
```
car = Car('blue', 2, 40, 2010)
--->

car = Create2WDBestSellCar()

def Create2WDBestSellCar():
    return Car('blue', 2, 40, 2010)
```

### Benefits
1. Make the creation call easy to understand.
2. Encapsulate the creation into a method to be reusable.
3. In the future, if this create is changed, one edit instead of modifying everywhere the object is created to apply the change.

## Factory Method
This is more on the class level that the interface defines a factory method that the subclasses that implement this interface will use the same factory method to instantiate the object.

### When to use
When you have manager level object that need to manipulate/create the objects A that's of the same interface, then a factory method for the interface of object A is useful to defer the creation details to the implementations of the interface. And the manager can just call the creation method to create a bunch of objects which is different but share the same interface.
```
FurniturePipeLine.Create(12,44)

class FurniturePipeLine:
    def Produce(self, nChair, nTable):
        for i in range(nChair):
            res.append(Create(chairProducer))
        for i in range(nTable):
            res.append(Create(tableProducer))
        return res

    def Create(self, producer):
        return producer.make()

class Producer:
    def make(self):
        return 'original producer'

class ChairProducer(Producer):
    def make(self):
        return 'Chair'

class TableProducer(Producer):
    def make(self):
        return 'Table'
```

This allows the high level manipulation/creation of the same interface possible by just calling the factory method in a iteration since they have the same signature.

### Benefits
1. Simplify the signature of creating the object.
2. Use polymorphism to delegate the creation of the same series of object to be one repeated call.
3. Hide the details of the creation away from the high level.


## Abstract Factory
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

Abstract Factory is a higher level abstraction of the factory pattern.

### When to use
If you have a family of objects and the objects can be grouped under certain types, then the abstract factory can be used to produce the same type of object of that family.
For example, a car abstract factory can be implemented by different brands to produce the car parts, engine, wheel, body, of certain brand.

## Factory Method VS Abstract Factory VS Creation Method

### In terms of the level of abstraction

Abstract Factory _HIGHER THAN_ Factory Method _HIGHER THAN_ Creation Method

### In terms of the scope

Abstract Factory COULD INCLUDE Factory Method COULD INCLUDE Creation Method

### How to differentiate them
Creation Method refers to a **method** that could handle creation of a object.

Factory Method refers to a **abstract method** that could be implemented by subclasses to handle the creation of a series objects.

Abstract Factory refers to a series **factory** that handles the creation objects that belongs to different families but of the same kind.


## Strategy
Modularize different strategies into one common type/interface so that the higher level can call solve the same kind of problem using same signature but different strategies. More explicitly, modularize a family of algorithm which achieve the same thing to be interchangeable.

### When to use them
On a higher level abstraction, the logic sometime only cares about solving the problem itself as oppose to the details of how to solve the problem. Then, the strategy can play a role here to offer the same signature to solve one kind of problem but defer the question of which strategy to use to somewhere else.
Thus the focus can be divided. The higher level method will focus on which problem to solve. The lower level one will focus on which strategy to solve it. The strategy class is responsible for how to solve it.

### Benefits
1. The strategy can be interchangeable so no matter what strategy to choose, the problem can be solve.
2. The framework can stay untouched if new strategies are added or the old strategies are out-dated and deleted.

## Singleton
Ensure the class has only one instance and give it a global entrance to access it.

### When to use
Don't use it unless you absolutely 100% sure that the class is 100% isolated from other code and no need to change in the future.

### Why it's bad
1. The global access of the singleton makes it play a role of global variable. It's hard to tell the state of the instance and also it's easy to encounter the race condition since it's used in different places at the same time.
2. It's hard to mock or stub the class for tests since the initialization of the class is somehow out of your control.
3. It's a big blocker for refactoring. Singleton offered a global access to the class itself which means the classes that depend on the singleton is directly accessing the singleton class which makes the two tightly coupled and hard to decouple.


## Command
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

### When to use
This patten is more focused on encapsulating the operations in a object. The object representing a request for a certain operation. By checking the command object, the goal of the command and parameters are shown. A good example of this is the network layer. Networks can handle multiple requests from one app to another. Each request is a command to tell the app on the other side to do some kind of work.

### Benefit
1. By logging the command object, the history of the requests will be recorded. This exposing the information of how the system works.
2. By recording the commands and parameters, the system can support the undo operation to recover the system back to the original state.

## Command VS Strategy

Just brief, a command has different purpose. For example: CutCommand, DeleteCommand, CopyCommand, SortCommand,.... A strategy has same purpose but different approach. In sorting algorithm, we have: BubbleSort, SelectionSort, ...

Typically the Command pattern is used to make an object out of what needs to be done -- to take an operation and its arguments and wrap them up in an object to be logged, held for undo, sent to a remote site, etc. There will tend to be a large number of distinct Command objects that pass through a given point in a system over time, and the Command objects will hold varying parameters describing the operation requested.

The Strategy pattern, on the other hand, is used to specify how something should be done, and plugs into a larger object or method to provide a specific algorithm. A Strategy for sorting might be a merge sort, might be an insertion sort, or perhaps something more complex like only using merge sort if the list is larger than some minimum size. Strategy objects are rarely subjected to the sort of mass shuffling about that Command objects are, instead often being used for configuration or tuning purposes.

Both patterns involve factoring the code and possibly parameters for individual operations out of the original class that contained them into another object to provide for independent variability. The differences are in the use cases encountered in practice and the intent behind each pattern.

## Observer
Define a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.

### When to use
If you find the change of a class A is always triggers an operation to another class B or many other classes C,D,..., then now class A,B,C,D are coupled. Using the Observer/observable pattern is a good option to decouple the 2 sides of classes.
Since now the observer is responsible for exchange data between 2 classes, the classes does not know each other. They are decoupled and and do further refactoring.

### Benefit
1. Decouple the classes to remove the knowledge of other classes.
2. Open for further refactoring since the dependency is less.
