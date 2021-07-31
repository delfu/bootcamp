# Week 1: The Beginning

## Story

Intern, your first task is to implement our math equation evaluator feature in our Project DoubleZero. Let's start with a simple design and reiterate. It will serve as the basis of the rest of the project so we'll need to get this done this week

## General Terminologies

- `computer instructions/machine code`: computers work one instruction at a time. Each instruction is a very basic operation like `store this number here`, `load that number from over there`, `if this number is 0, go here`, `add this number and this number and store it here`. These are called `instructions`. Each type of CPU has a list of these instructions that it understands and that's why a program made for Mac doesnt work for Windows machines for example; they have different `CPU architecture`.

- `assembly`: this is a type of programming language that's closest to raw computer instructions. Each CPU architecture has its own assembly language. When computer programming was first invented, this was the first of telling computers what to do. However, it is very cumbersome to use. That's why we invented higher level programming languages.

- `compiled language`: a compiled programming language is a language that's much closer to english and much easier to use. It gets passed to a `compiler` that turns it into raw computer instructions (technically to assembly first). Languages like C and C++ are classic examples of this kind of language. However, because of the `compiler` step, working with these languages are still a bit cumbersome.

- `interpreted language`: an interpreted language, like Javascript, Python, ... are among some of the most modern languages. They do not require a compiler to turn the instructions into machine code first. The downside is that they run slower than a compile language. But they are the easiest to program for and can be modified quickly

## Theory

### Type

Every piece of data in a computer program is represented in `binary` of 32 bits. Each bit is either a 0 or a 1. That gives a possibilty of around 4 billion values. For example, `00000000000000000000000000000010` represents the digit `2`. So how do we represent something that's not a number? That where `types` come in. We can tell the computer what kind of data to expect so we can represent numbers, letters, ... re-interpreting the bits as such.

Some basic types are:

- `string`: a sequence of letters. It's what we use to represent text
- `boolean`: a true or false value
- `integer`: a whole number, negative or positive
- `float`: a number with decimals, negative or positive

### Data structures

A major part of programming is to deal with `data structures`. A data structure is a way to store data in a much more structured way.

Some basic data structures are:

- `array`: a sequence of data of any type, can be access randomly. For example, we have an array of numbers `1, 2, 30, 55` and we can get the second element (`2`) out of it. This is one of the most basic data structures, usually used to represent anything similar to a list. And in a way, a `string` is essentially an array of individual characters
- `dictionary`: similar to a regular dictionary, each entry has a `key` (in the case of English, it's the word you're looking up) and a `value` (in the case of English, it's the definition of the word). This is a very useful data structure. It allows us to store things we want to look up later. Instead of creating multiple variables and assigned them values, we use a dictionary to group them all in one place. For example, we can use this to store settings so when the program needs to lookup a setting, it can do so really quickly.

There are tons more data structures out there. We'll cover more in the future

### Control flow

In order for a program to do anything, it needs to be able to react to inputs and logic. That's where `control flow` comes in. You may have heard of `if/else`, it's the most well known and basic control flow. It allows a program to do different things based on different values.

- `if/else`: it's best to illustrate this by example:

```python
if someVariable == 5:
	print("the value is 5")
elif someVariable > 10:
	print("the value is too big")
else:
	print("i'm not sure what the value means")
```

in this code (python) has a variable called someVariable of type `integer` that if it's 5 then the program outputs `the value is 5`, if the value is larger than 10 outputs `the value is too big`, and if the value is anything else, we say we dont know how to handle the value.

The `:` at the end of each line here is essential to tell python that the condition has ended.

`==` means equality. In python a single `=` is to assign a value to a variable like `someVariable = 9` means assign the value of 9 to someVariable

The extra spacing in front of `print` is essential. As a rule in python, lines after a `:` will be indented. Because it's inside the conditional. Some languages use `{}`, some languages use indentation

`print` just means output some text

- `for`: is what we call a loop. It contains some condition that while not met, we'll keep running the inner code. This is very similar to `while` loop.

```python
for character in someString:
	if character == "a":
		print(character)
```

This code snippet has a variable called `someString` of type string (just text). for every single letter of that string, we'll print it out if it's `a`. So for an input of `hello my name is Alan`, the output would be `aa`, from n`a`me and Al`a`n . The capital A from Alan did not match because the comparison is case sensitive.

## Assignment Instructions:

The goal of this week's assignment is to create a program that, given a mathematical expression, will return the result. We will do this in two parts

### Part 1

First we'll handle simple input. we will only have expressions with a single operation `+-*/`

And for some ease (reason is not immediately evident) we put the operation at the end and not in between the two numbers

Example input and output:

- `1 2 +` means 1+2 and the output would be `3`
- `25 4 *` outputs `100`

a few useful tips:

- use the `split` function on a string, it will allow you to "split" a string into pieces based on a character you provide, in this case " "
- use the starter code. It will let you run a bunch of tests. To run it, do `python part1.py` in the commandline

### Part 2

Second we'll enhance our solution by supporting multiple operations per line.
`2 4 + 5 *` should output 30. We will not support operation priority, it will only be evaluated left to right
