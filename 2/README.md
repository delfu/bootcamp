# Week 2:

## Story

It is now the second week of your internship. Last week, your calculator was well implemented and is now widely used within the project. This week, we'll add a new functionality of linking certain pieces of data together to form a map of knowledge.

## General Terminologies

- `algorithm`: in CS this is the term we use to describe a general approach to a problem. It's used to describe a set of things that needs to happen to solve a problem. It is not a true computer program, only a vague description of it. For example, when you describe to your friend how to get to your house (take the highway, exit at exit 45, turn right) would be an algorithm but instructions like accelerate to 100km/h, slow down before you get to a traffic light, turn the wheel 30 degrees to the right would be omitted. Those instructions would be actual instructions in a program

- `function`: last week we explored some basic concepts of programming. You may have seen functions mentioned online or while you were coding. Let's explain it more formally here. It is a way for us to structure the code in a manageable and modular way. Each function is a reuseable unit, think a mini program, that will perform certain unit of work. It has inputs and outputs. The inputs are called `arguments`. The outputs are called `returns`. Think of the mathematical concept of adding two numbers together. The function name would be something like `add` and the arguments are `number1` and `number2`. Inside the function we'll define all the steps needed to add two numbers together (take the last digit, add it to the other digits,...) and the `return` would be the result of the addition. Not all functions will have inputs or outputs or either.

- `computational complexity`: In CS it is really difficult to evaluate how fast a program runs because it depends on many factors: computer hardware, runtimes, if the CPU is doing something else... The way we gauge if an algorithm is better than another is through computational complexity, a rough sense of how complicated an algorithm is.

- `list`: Last week we learned about the `array` and `dictionary` data structure (recall a data structure is a programming concept of organizing data). This week we'll learn about `list`

## Theory

Last week we used arrays to store some data. Today we'll learn some of its limitations and why we might use other data structure for other things.
Any data structure has a few important computational complexities to analyze:

1. How long does it take to read data?
2. How long does it take to write data?
3. How long does it take to create the data structure?

`Computational Complexity` is not a number or an exact measurement in seconds or milliseconds. But rather it's an order of magnitude. This is better illustrated using an example.
Say you have an array of 100 numbers. How fast can you find the smallest number? The number of seconds it takes you to find the smallest number depends on how fast you read, how good is your eyesight, ... But no matter who you are, you'd have to look at each number at least once, otherwise you might get the wrong number. That's computational complexity. The order of magnitude would be on the order of `N` where `N` is the number of items. This number scales linearly with the number of elements in that array. So an array of 100 or an array of 1000 items, you'd have to look at each number at least once. So for both cases it'd be order of `N`. We use the shorthand `O(N)` to indicate order of N. This short hand is called "big O notation"

This concept of computational complexity is **THE** most crucial concept in CS. If an algorithm A takes `O(N)` but another B takes `O(N^2)`, depending on the what N is, the difference might be negligeable or maybe B might even be faster than A (there's a constant term hidden in there, we'll cover that later). But given a big enough number, a linear algorithm will be faster than an quadratic algorithm.

Similar to the basic graph concept in math `f(x) = 5x + 3`, big O notation also have different graphs. Two `O(N)` might be different because they have different slopes or different constant terms. But their characteristics is that they are both linear and that's really what we care about. So `O(5N)` will always be simplified to `O(N)` because the N term will always dominate. Similarly, we dont put the constant term.

Most often you'd see these types of big O results, in order of "speed":

- `O(some_number)`: constant
- `O(log(N))`: Logarithmic
- `O(N)` : linear
- `O(N ^ some_number)` : polynomial
- `O(some_number ^ N)`: exponential

Don't worry, we'll do many more exercises in the future

## Linked Lists

What an array offers is a way to:

- read data in constant time
- write data in constant time

However, due to its nature, expanding an array is expensive. When first created it is a chunk of memory. But when we run out of space, we need to allocate a bigger chunk of memory and copy over the data. This would be expensive if we do not know ahead of time how big an array we need.

A linked list is a data structure that let's you keep adding items to without incurring that cost. The term "list" is sometimes confused with arrays but in CS terms it is a specific data structure.

The most basic definition of a list item has 2 values inside: a `value` and a `next`. `value` stores the value of the element you want to store. `next` is another list item or `None`

```python
class LinkedListItem:
  def __init__(self, value, next):
    self.value = value
    self.next = next

item3 = LinkedListItem(3, None)
item2 = LinkedListItem(2, item3)
item1 = LinkedListItem(1, item1)

# item1.value == 1
# item1.next.value == 2
# item1.next.next.value == 3
```

The biggest disadvantage over arrays is if you want to access, say the 3th item, you'll have to go through the first two using `next`.

```python
item1.next.next.value
```

So why use a linked list? This seems more cumbersome than an array where you could just do `some_array[2]` to access the 3rd element.

The reason is when we need to add a new item at the end all we have to do is find the last item and `last_item.next = LinkedListItem(1000, None)`

Additionally, with an array, if you need to insert something in the middle of the array, you need to create a new array that's slightly bigger, copy the first part of the old array, add the new item, then copy over the latter part of the old array. With an linked list, all you need to do is to find the splitting point, and

```python
second_part_of_list = splitting_point.next #we temporarily remember where the second half is
splitting_point.next = LinkedListItem(1000, second_part_of_list) # we stitch a new item in
```

In short, linked lists have a linear complexity for read, constant complexity for inserting

Since linked lists are so easy to define, there are many ways to customize this. Adding a `previous` field, you'll be able to create a `two way linked list` that allows you to go forward and back.

You can `next` to be an array of LinkedListItem instead of a single item, we can create a branching list (ie: a tree). We'll discuss this in future weeks.

# Assignment

As part of the enhancement of last week's assignment, we are looking to implement a factorial operator and a fibonacci operator.

Define these two functions:

1. `fib(x)` where `x` is the x-th number in a fibonacci sequence. Refresher, the fibonacci sequence is an operation where each number is the sum of the previous two numbers in the sequence. The starting sequence is `1, 1, 2, 3, 5, 8, 13, ...` the next number in the sequence is 21 because `8 + 13 == 21`. So a formal definition is `fib(x) == fib(x-1) + fib(x-2)` ... but there might be some issue with that approach ...

2. `fact(x)` where we return the factorial of `x`. Refresher, factorial is the mathematical operation where `fact(x) == x * (x - 1) * (x - 2) * (x - 3) * ... * 1`. So formally, `fact(x) == fact(x - 1) * x` There is a mathematical way of solving this, but that's not what we want. Don't google for that method

Use the provided code to run testing. It is setup so that it runs these two functions many many times. Do whatever you can to make the function run fast enough... hint: you might end up running with the same arguments many times ...
