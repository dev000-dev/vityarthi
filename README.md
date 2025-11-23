Number Theory Explorer
A Comprehensive Collection of 34 Classic & Advanced Number Theory Algorithms in Python

Overview of the Project
NumberTheory Explorer is a clean, well-documented, educational Python library containing 34 carefully implemented number-theoretic algorithms, ranging from beginner-friendly concepts (factorial, palindrome check) to advanced topics (Miller–Rabin primality test, Chinese Remainder Theorem, Carmichael numbers, integer partitions, etc.).
This repository is perfect for:
•	Students learning number theory & algorithms
•	Competitive programmers needing fast, correct implementations
•	Anyone preparing for interviews or building cryptographic prototypes
•	Teachers looking for ready-to-use examples
All functions are pure Python, require zero external dependencies, and include performance profiling where relevant.


Features (34 Algorithms)
#	Algorithm / Function	Category
1.	Recursive Factorial	Basics
2.	Palindromic Number Check	Digital Properties
3.	Mean of Digits	Digital Properties
4.	Digital Root	Digital Properties
5.	Abundant Number	Divisor Theory
6.	Harshad (Niven) Number	Digital + Divisor
7.	Automorphic Number	Fun Properties
8.	Pronic Number	Fun Properties
9.	Prime Factorization	Primes
10.	Count Distinct Prime Factors	Primes
11.	Prime Power Detection	Primes
12.	Mersenne Prime Test	Special Primes
13.	Twin Prime Generator	Special Primes
14.	Number of Divisors	Divisor Theory
15.	Aliquot Sum (Proper Divisors Sum)	Divisor Theory
16.	Amicable Pair Checker	Divisor Theory
17.	Multiplicative Persistence	Digital Persistence
18.	Highly Composite Number Checker	Divisor Theory
19.	Fast Modular Exponentiation	Modular Arithmetic
20.	Modular Inverse (Extended Euclidean)	Modular Arithmetic
21.	Chinese Remainder Theorem Solver	Modular Arithmetic
22.	Quadratic Residuosity (Euler Criterion)	Modular Arithmetic
23.	Multiplicative Order	Modular Arithmetic
24.	Fibonacci Prime Checker	Sequences + Primes
25.	Lucas Sequence Generator	Sequences
26.	Perfect Power Detection	Powers
27.	Collatz Sequence Length	Conjectures
28.	Polygonal Number Generator	Sequences
29.	Carmichael Number Checker	Composite Numbers
30.	Miller–Rabin Primality Test (with profiling)	Probabilistic Primality
31.	Riemann Zeta Function Approximation	Analytic Number Theory
32.	Integer Partition Function p(n) (DP)	Combinatorial Number Theory
Performance profiling using time.perf_counter() and tracemalloc is included for heavy algorithms.

Technologies / Tools Used
•	Python 3.11+
•	Standard Library only (math, random, time, tracemalloc, sys)
•	No external packages required

Steps to Install & Run
 # 1. Clone the repository
git clone https://github.com/your-username/numbertheory-explorer.git
cd numbertheory-explorer

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
# or
venv\Scripts\activate       # Windows

# 3. Run the interactive demo
python demo.py

# Or run individual files
python basics/factorial.py
python advanced/miller_rabin.py


Instructions for Testing
# Run the full test suite (130+ test cases)
pytest tests/ -v

# Or run specific test
pytest tests/test_primes.py







