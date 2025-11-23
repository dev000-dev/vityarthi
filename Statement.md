# Project Title: NumPy – A Comprehensive Python Library for Number Theory Exploration

## Problem Statement
In the fields of mathematics, competitive programming, cryptography, and computer science education, there is a persistent need for fast, reliable, and well-documented functions that determine properties of integers (prime checking, factorisation, special number classifications, modular arithmetic, etc.). Existing solutions are either scattered across multiple sources, poorly optimised, lack proper documentation, or are not beginner-friendly. This leads to repeated code duplication, subtle bugs, and wasted time when students, educators, or developers need to verify number-theoretic properties.

## Scope of the Project
NumPy (Number Theory Utilities in Python) is a lightweight, pure-Python library that provides a rich, correctly implemented, and extensively tested collection of functions for number-theoretic computations. The library covers:

- Basic properties (palindrome, digital root, mean of digits, etc.)
- Special number classifications (abundant, Harshad, automorphic, pronic, perfect, amicable, highly composite, Carmichael, etc.)
- Prime-related utilities (fast primality testing, Mersenne primes, twin primes, Fibonacci primes, Miller-Rabin with performance metrics)
- Divisor functions (count, sum, aliquot sum)
- Modular arithmetic (fast exponentiation, extended Euclidean algorithm, modular inverse, Chinese Remainder Theorem, quadratic residuosity, multiplicative order)
- Sequence generators (Fibonacci, Lucas, polygonal, Collatz steps, multiplicative persistence, partition function)
- Advanced tools (perfect power detection, Riemann zeta approximation, etc.)

The project is deliberately kept dependency-free (only standard library + optional math/random/time/tracemalloc for performance demos) so it can be used in educational environments, online judges, and embedded scripts without external requirements.

## Target Users
1. Competitive programmers preparing for IOI, ICPC, Codeforces, AtCoder, and other platforms
2. Undergraduate and high school students learning number theory and algorithms
3. Mathematics and cryptography educators needing clean, readable reference implementations
4. Developers building cryptographic prototypes or mathematical tools in Python
5. Hobbyists and math enthusiasts exploring integer sequences and properties

## High-Level Features
- 100% pure Python – no compilation or external dependencies required
- Comprehensive test cases and examples for every function
- Optimised algorithms (O(sqrt(n)) divisor loops, binary exponentiation, Miller-Rabin probabilistic testing, dynamic programming for partitions, etc.)
- Clear docstrings and type hints for excellent IDE support
- Educational focus: every function is written to be readable and understandable by students
- Performance monitoring utilities (time & memory tracing) for primality testing
- Ready-to-use script collection that serves as both library and learning resource
- MIT licensed – free for commercial, academic, and personal use

NumPy aims to become the go-to single-file (or small module) number theory toolkit for the Python community.
