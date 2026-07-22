# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
22-07-2026

## 📚 Topics Covered

## Iterable

## Iterator

## iter()

## next()

## StopIteration

## __iter__()

## __next__()

## Custom Iterator

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run


## Official Python Documentation

- Iterator Types ✅
- Iterator Protocol ✅
- iter() ✅
- next() ✅
- StopIteration ✅

---

## 💻 Programs

- literator_basics.py
- iter_list.py
- iter_tuple.py
- iter_string.py
- custom_counter.py
- custom_iterator.py
- hospital_patient_iterator.py
- employee_iterator.py

- program01.py
- program02.py
...
- program15.py




---

## 🏥 Mini Project

Hospital Patient Iterator



## 🎯 Bonus Project

Employee Record Iterator



---

## 15 Practice Programs
- List Iterator
- Tuple Iterator
- String Iterator
- Set Iterator
- Dictionary Iterator
- iter() practice
- next() practice
- Handle StopIteration
- Custom Counter Iterator
- Custom Number Iterator
- Reverse Iterator
- Even Number Iterator
- Hospital Patient Iterator
- Employee Iterator
- Custom Range Iterator

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Iterators / Generators) ✅


---


## 💡 What I Learned Today

 
✅ Iterable kya hota hai?
✅ Iterator kya hota hai?
✅ iter()
✅ next()
✅ Iterable vs Iterator
✅ __iter__()
✅ __next__()
✅ for loop internally kaise kaam karta hai
✅ Custom Iterator
✅ Mini Project
✅ Bonus Project


---

## 📂 GitHub

Day17 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1.  What is an Iterable?

An Iterable is any Python object that can return its elements one at a time, allowing it to be iterated over in a loop (like a for loop).Key characteristic: It implements the __iter__() method.Examples: list, tuple, string, dictionary, set.

### 2. What is an Iterator?

An Iterator is an object that represents a stream of data. It remembers its current state during iteration and produces the next value each time next() is called on it.Key characteristic: It implements both __iter__() and __next__() methods.

### 3. Difference between Iterable and Iterator?

FeatureIterableIteratorDefinitionObject that can be looped over.Object that performs the actual iteration step-by-step.StateDoes not keep track of current state/position.Keeps track of its current position.Methods RequiredMust implement __iter__().Must implement both __iter__() and __next__().MemoryStores all elements in memory at once.Generates/fetches elements on demand (memory efficient).Example[1, 2, 3] (List)iter([1, 2, 3]) (List Iterator)

### 4. What does iter() do?

The iter() built-in function takes an Iterable as an argument and returns its corresponding Iterator object.Pythonnumbers = [1, 2, 3]          # Iterable
nums_iter = iter(numbers)    # Iterator

### 5. What does next() do?

The next() built-in function fetches the next item from an Iterator. Each time you call next(), it advances the iterator by one step.Pythonprint(next(nums_iter))  # Output: 1
print(next(nums_iter))  # Output: 2

### 6. What is StopIteration?

StopIteration is a built-in exception raised automatically by an iterator's __next__() method when there are no more items left to iterate over.

### 7. What is the Iterator Protocol?

The Iterator Protocol in Python is a standard agreement consisting of two methods:__iter__(): Returns the iterator object itself.__next__(): Returns the next item or raises StopIteration when finished.Any object that implements both of these methods adheres to the Iterator Protocol.

### 8. What is __iter__()?

It is a special (dunder) method.When called on an Iterable, it creates and returns a new Iterator.When called on an Iterator, it returns self (the iterator itself).

### 9. What is __next__()?

It is a special (dunder) method implemented in an Iterator.It returns the next value from the container.If no more items are available, it raises the StopIteration exception.

### 10. How does a for loop work internally?When you write:Pythonfor item in [10, 20]:
    print(item)
Internally, Python performs the following steps under the hood:Calls iter([10, 20]) to get an iterator.Runs an infinite loop where it repeatedly calls next() on that iterator.Catches the StopIteration exception automatically to exit the loop gracefully without crashing.Python# Internal equivalent:
iterator = iter([10, 20])
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
### 11. Can a List be an Iterator?

No. A list is an Iterable, but not an Iterator.A list does not have a __next__() method.Calling next([1, 2, 3]) will raise a TypeError. You must convert it first using iter([1, 2, 3]).

### 12. How do you create a Custom Iterator?

You create a custom iterator by defining a class that implements __iter__() and __next__().Pythonclass Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self  # Returns itself as an iterator

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

# Usage
count = Counter(3)
for num in count:
    print(num)  # Prints 1, 2, 3
### 13. Why are Iterators useful?

Memory Efficiency: They compute elements on-the-fly (lazy evaluation) rather than storing the entire sequence in memory.Infinite Sequences: They allow processing datasets that are potentially infinite (e.g., reading a stream of sensor data).Large File Processing: Allows reading huge files line-by-line without loading the whole file into RAM.14. What is the difference between Iterator and Generator?FeatureIteratorGeneratorCreationCreated using custom class with __iter__() & __next__().Created using a function with the yield keyword.Code ComplexityRequires more boilerplate code.Extremely concise and readable.State TrackingYou manually manage variables and state.Python automatically saves state when yield is hit.ProtocolExplicitly implements the Iterator Protocol.Automatically implements the Iterator Protocol.15. What happens when an Iterator reaches the end?Once an iterator reaches the end:Calling next() on it raises a StopIteration exception.The iterator is exhausted. It cannot be reset or reused; if you need to iterate again, you must create a new iterator object using iter().