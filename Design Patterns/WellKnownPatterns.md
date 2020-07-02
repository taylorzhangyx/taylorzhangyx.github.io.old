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



- Singleton
- Command
- Command VS Strategy
- Observer
