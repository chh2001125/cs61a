# CS61a:Structure and Interpretation of Computer Programs	2021 Spring



这是我自己对cs61a所有lab、hw、project的实现，也算是记录自己的学习过程，代码仅供参考。

课程地址：https://inst.eecs.berkeley.edu/~cs61a/sp21/



# 完成度：

耗时：24h

Lab（6/13）

HW（4/10）

Project（2/3）

# Lab:

## [Lab 00: Getting Started](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab00/)


## [Lab 01: Variables & Functions, Control](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab01/)


## [Lab 02: Higher-Order Functions, Lambda Expressions](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab02/)


## [Lab 03: Recursion, Tree Recursion](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab03/)


## [Lab 04: Midterm Review](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab04/)


## [Lab 05: Python Lists, Data Abstraction, Trees](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab05/)


## [Lab 06: Nonlocal, Mutability, Iterators and Generators](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab06/)	


## [Lab 07: Object-Oriented Programming, Linked Lists, Mutable Trees](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab07/)	未完成


## [ Lab 08: Midterm Review](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab08/)	未完成


## Lab 09：缺失

## [ Lab 10: Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab10/)	未完成


## [Lab 11: Interpreters](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab11/)	未完成


## [ Lab 12: Tail Recursion, Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab12/)	未完成


## [Lab 13: Regular Expressions, BNF](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab13/)	未完成


## [Lab 14: Final Review](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab14/)	未完成

# HW:

## [HW 01: Variables & Functions, Control](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw01/)


## [HW 02: Higher-Order Functions](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw02/) 


## [HW 03: Recursion](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw03/)	
### Q2:pingpong值得回顾

pingpong（n）
要求给出n处的值

1. 这道题要求使用递归完成并且不能使用赋值语句，助教的提示是通过迭代的方式实现逻辑然后再将迭代转换成递归。
2. 由于不能使用赋值语句，在转换的过程中，发现并不能保存当前的状态是该加还是减。于是助教提示使用helper()函数帮助我们转递参数并且保存状态
3. helper(index，pingpongvalue，direction)函数不仅可以访问pingpong的n，还可以通过传参的形式保存状态
4. 如果直接使用pingpong进行递归的话，我们需要**反向**访问之前的值，但是pingpong函数不能使用赋值语句并且只能传入一个参数，无法保存状态
5. 使用helper(index，pingpongvalue，direction)相当于**正向**前进，知道当前状态就可以推断出下一状态，直到index等于n

对问题的分析也很重要：
- 要明确有什么重要的参数需要传递（index，pingpongvalue，direction）
- 需要返回什么

反思：
- 使用递归时要时刻想到**分治法** --> 将问题分解
- 可以考虑将反向的递归（分解）转换为正向的递归（合并）
- 实在想不出来怎么实现递归时不妨先实现迭代，再将迭代转化为递归

### Q4:Count coins值得回顾！！！
http://composingprograms.com/pages/17-recursive-functions.html#example-partitions

## [HW 04: Trees, Data Abstraction](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw04/) 	


## [HW 05: Object-Oriented Programming, Linked Lists, Iterators and Generators](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw05/) 未完成


## [HW 06: Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw06/)	未完成


## [HW 07: Scheme, Scheme Lists](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw07/)	未完成


## [HW 08: Tail Recursion, Interpreters, Scheme](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw08/)	未完成


## [HW 09: Regular Expressions, BNF, Macros](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw09/)	未完成


## [ HW 10: Finale](https://inst.eecs.berkeley.edu/~cs61a/sp21/hw/hw10/)	未完成


# Project:

## [Hog](https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/hog/)	

## [ Cats](https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/cats/)

## [Ants](https://inst.eecs.berkeley.edu/~cs61a/sp21/proj/ants/)	未完成




