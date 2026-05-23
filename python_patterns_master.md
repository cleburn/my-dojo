# Python Patterns Master Reference
## Systematic Python Fluency Curriculum

**Last Updated:** January 3, 2026  
**Current Module:** 4  
**Next Review:** Start of Module 5

**Purpose:** Master inventory of Python idioms and patterns to be introduced through daily Foundation Drilling. Ensures systematic coverage of professional Python skills beyond data science tasks.

**Authority:** This document owns the complete pattern catalog, priority rankings, module alignment, and status tracking. Weekly Foundation Drilling docs reference this document—they do not duplicate pattern explanations.

---

## Integration with Foundation Drilling

### Pacing Principle (Critical)

**Exposure ≠ Learning.** Seeing a pattern once and moving on creates false familiarity without usable skill.

**Required pacing:**
- **Maximum 3-4 new patterns per module**
- **Minimum 4 consecutive days drilling each pattern before advancing**
- **Pattern must reach "can use without template" before introducing next**

**The math:** A typical module spans ~20 training days. With 4 patterns at 5 days each, that's full coverage with genuine learning. Cramming 9 patterns into 20 days (2 days each) produces exposure theater.

**Carryover rule:** Patterns scheduled but not mastered in previous module get priority in next module's queue. Don't abandon unfinished patterns for new ones.

---

### Part 1 Structure

**Part 1a: Fluency Rep**
- Rotate through adopted patterns
- Reinforce learned material
- Pull from "Adopted" or "Fluency Pool" status patterns

**Part 1b: New Pattern Exposure**
- Introduce one new pattern OR drill a "Learning" status pattern
- **Drill same pattern for 4-5 consecutive days minimum**
- Format: Pattern → Example → Translation → Variations
- Pattern selection follows module schedule below

### Teaching Format Template

When introducing any new pattern, use this format:

```python
# Basic pattern
<syntax template>

# Real example
<concrete code with actual values>
# Translation: "<plain English explanation>"

# Common variations
<2-3 variations showing flexibility>
```

### Repetition Rules

| Pattern Value | Repetition | Advancement Criteria |
|---------------|------------|----------------------|
| High | 4-5 days drilling | Can use without looking at template |
| Medium | 3-4 days drilling | Can recognize and apply with minor reference |
| Novel/Lower | 2-3 days exposure | Saved in notes, can look up when needed |

---

## Pattern Catalog

### HIGH PRIORITY — Essential Professional Python

These patterns appear constantly in professional code, interviews, and code reviews. Must reach "Adopted" status.

---

#### Category: Unpacking & Argument Handling

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `*` iterable unpacking | Unpack list/tuple into separate elements | 4 | Not Adopted |
| `**` dict unpacking | Unpack dict into keyword arguments | 4 | Not Introduced |
| `*args` in functions | Accept variable positional arguments | 4 | Not Introduced |
| `**kwargs` in functions | Accept variable keyword arguments | 4 | Not Introduced |
| Multiple assignment | `a, b, c = [1, 2, 3]` | 4 | Not Introduced |
| Swap values | `a, b = b, a` | 4 | Not Introduced |
| `*` in zip | `list(zip(*nested_list))` transpose | 5 | Not Introduced |

**Pattern Details:**

```python
# * iterable unpacking
# Basic pattern
function(*iterable)

# Real example
numbers = [1, 2, 3]
print(*numbers)  # prints: 1 2 3
# Translation: "Unpack list into separate arguments"

# Variations
combined = [*list1, *list2]  # Merge lists
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
```

```python
# ** dict unpacking
# Basic pattern
function(**dictionary)

# Real example
config = {'color': 'red', 'size': 10}
plot(**config)  # Same as plot(color='red', size=10)
# Translation: "Unpack dict keys as parameter names, values as arguments"

# Variations
merged = {**dict1, **dict2}  # Merge dicts (dict2 overwrites)
new_dict = {**old_dict, 'extra_key': 'value'}  # Copy and add
```

```python
# *args and **kwargs in function definitions
# Basic pattern
def func(*args, **kwargs):
    pass

# Real example
def flexible_print(*args, **kwargs):
    for item in args:
        print(item, **kwargs)

flexible_print('hello', 'world', sep='-', end='!\n')
# Translation: "Accept any number of positional args, any keyword args"

# Common use: wrapper functions, decorators, inheritance
```

---

#### Category: Dictionary Methods

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `.get()` | Safe key access with default | 4 | Not Introduced |
| `.setdefault()` | Get or set if missing | 5 | Not Introduced |
| `.items()` | Iterate key-value pairs | 2 | Adopted |
| `.keys()` / `.values()` | Access keys or values | 2 | Adopted |
| `.update()` | Merge dictionaries | 5 | Not Introduced |
| `.pop()` | Remove and return value | 5 | Not Introduced |
| Dict comprehension | `{k: v for k, v in ...}` | 5 | Not Introduced |

**Pattern Details:**

```python
# .get() - safe key access
# Basic pattern
dict.get(key, default_value)

# Real example
user = {'name': 'Alice', 'age': 30}
city = user.get('city', 'Unknown')  # Returns 'Unknown', no KeyError
# Translation: "Get value if key exists, otherwise return default"

# vs dangerous way
city = user['city']  # KeyError if missing!

# Common use
count = counts.get(word, 0) + 1
```

```python
# .setdefault() - get or initialize
# Basic pattern
dict.setdefault(key, default_value)

# Real example
groups = {}
groups.setdefault('fruits', []).append('apple')
groups.setdefault('fruits', []).append('banana')
# groups = {'fruits': ['apple', 'banana']}
# Translation: "If key missing, set it to default, then return the value"

# Common use: building grouped data structures
```

```python
# Dict comprehension
# Basic pattern
{key_expr: value_expr for item in iterable}

# Real example
prices = {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}
doubled = {fruit: price * 2 for fruit, price in prices.items()}
# Translation: "Build dict by transforming each key-value pair"

# Variations
filtered = {k: v for k, v in prices.items() if v > 0.6}  # With condition
squared = {x: x**2 for x in range(5)}  # From other iterable
```

---

#### Category: Iteration Tools

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `enumerate()` | Loop with index | 2 | Adopted |
| `zip()` basic | Pair up iterables | 2 | Adopted |
| `zip()` with `*` | Transpose / unzip | 5 | Not Introduced |
| `sorted()` with `key=` | Custom sort order | 5 | Not Introduced |
| `reversed()` | Iterate backwards | 5 | Not Introduced |
| `range()` variations | Start, stop, step | 1 | Adopted |

**Pattern Details:**

```python
# sorted() with key
# Basic pattern
sorted(iterable, key=function, reverse=False)

# Real example
words = ['banana', 'pie', 'Washington', 'a']
by_length = sorted(words, key=len)  # ['a', 'pie', 'banana', 'Washington']
# Translation: "Sort by the result of applying function to each element"

# Variations
sorted(words, key=str.lower)  # Case-insensitive
sorted(words, key=len, reverse=True)  # Longest first

# With lambda
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted(people, key=lambda p: p['age'])  # Sort by age
```

```python
# zip with * (transpose)
# Basic pattern
list(zip(*nested_list))

# Real example
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))  # [(1, 4), (2, 5), (3, 6)]
# Translation: "Flip rows and columns"

# Unzipping paired data
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)  # ('a', 'b', 'c'), (1, 2, 3)
```

---

#### Category: Comprehensions

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| List comprehension | `[x for x in ...]` | 1 | Adopted |
| List comp with condition | `[x for x in ... if ...]` | 2 | Adopted |
| Dict comprehension | `{k: v for ...}` | 5 | Not Introduced |
| Set comprehension | `{x for x in ...}` | 5 | Not Introduced |
| Nested comprehension | `[[... for ...] for ...]` | 6 | Not Introduced |
| Conditional expression | `x if cond else y` | 2 | Adopted |

**Pattern Details:**

```python
# Set comprehension
# Basic pattern
{expression for item in iterable}

# Real example
words = ['hello', 'world', 'hello', 'python']
unique_lengths = {len(w) for w in words}  # {5, 6}
# Translation: "Build a set (unique values only) from iterable"

# With condition
long_unique = {w for w in words if len(w) > 4}  # {'hello', 'world', 'python'}
```

```python
# Nested comprehension
# Basic pattern
[[expr for inner] for outer]

# Real example
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# Translation: "For each outer, build an inner list"

# Flattening (common pattern)
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]  # [1, 2, 3, 4, 5, 6]
# Read left-to-right: "for each sublist, for each x in sublist, take x"
```

---

#### Category: Error Handling

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Basic try/except | Catch exceptions | 4 | Not Introduced |
| Specific exceptions | Catch by type | 4 | Not Introduced |
| try/except/else | Run if no exception | 5 | Not Introduced |
| try/except/finally | Always run cleanup | 5 | Not Introduced |
| Raising exceptions | `raise ValueError(...)` | 6 | Not Introduced |
| Multiple except blocks | Handle different errors | 5 | Not Introduced |

**Pattern Details:**

```python
# Basic try/except
# Basic pattern
try:
    risky_code()
except ExceptionType:
    handle_error()

# Real example
try:
    result = int(user_input)
except ValueError:
    result = 0
    print("Invalid number, using 0")
# Translation: "Try this, if it fails with ValueError, do this instead"

# Catch-all (use sparingly)
except Exception as e:
    print(f"Error: {e}")
```

```python
# try/except/else/finally
# Basic pattern
try:
    risky_code()
except SomeError:
    handle_error()
else:
    runs_if_no_exception()
finally:
    always_runs()

# Real example
try:
    file = open('data.txt')
    data = file.read()
except FileNotFoundError:
    data = "default"
else:
    print("File loaded successfully")
finally:
    if 'file' in locals():
        file.close()
# Translation: "Try, handle errors, else runs on success, finally always runs"
```

---

### MEDIUM PRIORITY — Professional Competence

These patterns strengthen code quality and appear in interviews. Should reach "Adopted" status by Module 6.

---

#### Category: Functions

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Default arguments | `def f(x=10):` | 2 | Adopted |
| Keyword-only args | `def f(*, required):` | 6 | Not Introduced |
| Lambda functions | `lambda x: x * 2` | 5 | Not Introduced |
| Lambda with key= | `sorted(..., key=lambda)` | 5 | Not Introduced |
| Type hints basic | `def f(x: int) -> str:` | 6 | Not Introduced |
| Docstrings | `"""Description"""` | 5 | Not Introduced |
| `return` multiple values | `return a, b, c` | 2 | Adopted |

**Pattern Details:**

```python
# Lambda functions
# Basic pattern
lambda arguments: expression

# Real example
double = lambda x: x * 2
double(5)  # 10
# Translation: "Anonymous function, one expression, auto-returns result"

# Most common use: inline with other functions
sorted(items, key=lambda x: x['price'])
filter(lambda x: x > 0, numbers)
map(lambda x: x.upper(), words)

# When NOT to use: multi-line logic, reusable functions
```

```python
# Type hints
# Basic pattern
def function(param: type) -> return_type:
    pass

# Real example
def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)
# Translation: "Expects list of floats, returns float"

# Variations
from typing import Optional, Union
def greet(name: str, age: Optional[int] = None) -> str:
    pass
```

---

#### Category: Built-in Functions

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `any()` | True if any element truthy | 4 | Not Introduced |
| `all()` | True if all elements truthy | 4 | Not Introduced |
| `map()` | Apply function to all | 5 | Not Introduced |
| `filter()` | Keep elements passing test | 5 | Not Introduced |
| `min()`/`max()` with key | Find by custom criteria | 5 | Not Introduced |
| `sum()` with generator | Memory-efficient sum | 5 | Not Introduced |
| `isinstance()` | Type checking | 5 | Not Introduced |

**Pattern Details:**

```python
# any() and all()
# Basic pattern
any(iterable)  # True if ANY element is truthy
all(iterable)  # True if ALL elements are truthy

# Real example
numbers = [1, 2, -3, 4]
has_negative = any(n < 0 for n in numbers)  # True
all_positive = all(n > 0 for n in numbers)  # False
# Translation: "Check if any/all elements meet condition"

# Common use: validation
if all(field in data for field in required_fields):
    process(data)
```

```python
# min/max with key
# Basic pattern
min(iterable, key=function)

# Real example
products = [{'name': 'A', 'price': 100}, {'name': 'B', 'price': 50}]
cheapest = min(products, key=lambda p: p['price'])  # {'name': 'B', 'price': 50}
# Translation: "Find item with minimum value when function applied"

# Variations
longest_word = max(words, key=len)
oldest_person = max(people, key=lambda p: p['age'])
```

---

#### Category: String Methods

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `.join()` | Combine list into string | 5 | Not Introduced |
| `.split()` | Break string into list | 2 | Adopted |
| `.strip()` / `.replace()` | Clean strings | 2 | Adopted |
| f-string formatting | `f"{var:.2f}"` | 4 | Not Introduced |
| f-string expressions | `f"{x + 1}"` | 4 | Not Introduced |
| `.startswith()`/`.endswith()` | Check prefix/suffix | 5 | Not Introduced |
| `.format()` method | `"{} {}".format(a, b)` | 6 | Not Introduced |

**Pattern Details:**

```python
# .join() - combine iterable into string
# Basic pattern
separator.join(iterable_of_strings)

# Real example
words = ['hello', 'world']
sentence = ' '.join(words)  # 'hello world'
# Translation: "Put separator between each element, combine into one string"

# Variations
csv_line = ','.join(values)
path = '/'.join(['home', 'user', 'data'])  # 'home/user/data'
no_sep = ''.join(chars)  # Concatenate with nothing between
```

```python
# f-string formatting
# Basic pattern
f"{variable:format_spec}"

# Real examples
price = 19.99
f"${price:.2f}"  # '$19.99' - 2 decimal places
f"{price:>10.2f}"  # '     19.99' - right-align in 10 chars

percent = 0.856
f"{percent:.1%}"  # '85.6%' - as percentage

big_num = 1234567
f"{big_num:,}"  # '1,234,567' - thousands separator
# Translation: "Format variable according to spec after colon"
```

---

### LOWER PRIORITY — Recognition & Reference

These patterns should be recognizable. Full fluency not required until needed in projects.

---

#### Category: Classes (Basic OOP)

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Class definition | `class Name:` | 6 | Not Introduced |
| `__init__` method | Constructor | 6 | Not Introduced |
| Instance methods | `def method(self):` | 6 | Not Introduced |
| `self` convention | Instance reference | 6 | Not Introduced |
| Class attributes | Shared across instances | 7 | Not Introduced |
| Basic inheritance | `class Child(Parent):` | 7 | Not Introduced |

**Pattern Details:**

```python
# Basic class
# Basic pattern
class ClassName:
    def __init__(self, param):
        self.attribute = param
    
    def method(self):
        return self.attribute

# Real example
class Property:
    def __init__(self, address, price):
        self.address = address
        self.price = price
    
    def price_per_sqft(self, sqft):
        return self.price / sqft

house = Property("123 Main St", 300000)
print(house.price)  # 300000
# Translation: "Blueprint for creating objects with attributes and methods"
```

---

#### Category: Decorators

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Using `@decorator` | Apply decorator syntax | 7 | Not Introduced |
| `@property` | Getter as attribute | 7 | Not Introduced |
| `@staticmethod` | No self needed | 7 | Not Introduced |
| `@classmethod` | Receives class, not instance | 7 | Not Introduced |
| Reading decorator code | Understand what it does | 7 | Not Introduced |

**Pattern Details:**

```python
# Using decorators (reading/using, not writing)
# Basic pattern
@decorator
def function():
    pass

# Common decorators you'll see
@property  # Makes method act like attribute
@staticmethod  # Method doesn't need self
@classmethod  # Method receives class as first arg
@functools.lru_cache  # Memoization/caching
@app.route('/')  # Flask/FastAPI routing

# Translation: "Decorator wraps function to add behavior"
# For now: recognize syntax, understand it modifies the function
```

---

#### Category: Generators

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Generator expression | `(x for x in ...)` | 5 | Not Introduced |
| `yield` keyword | Produce values lazily | 7 | Not Introduced |
| `next()` function | Get next value | 7 | Not Introduced |

**Pattern Details:**

```python
# Generator expression
# Basic pattern
(expression for item in iterable)

# Real example
squares_gen = (x**2 for x in range(1000000))
# No memory used yet! Values computed on demand
first_ten = [next(squares_gen) for _ in range(10)]
# Translation: "Like list comp but lazy - computes values only when needed"

# Common use: memory efficiency with large data
sum(x**2 for x in huge_list)  # Doesn't build intermediate list
```

---

#### Category: Context Managers

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `with` statement | Auto cleanup | 4 | Not Introduced |
| File handling | `with open(...) as f:` | 4 | Not Introduced |
| Multiple contexts | `with a, b:` | 6 | Not Introduced |

**Pattern Details:**

```python
# with statement
# Basic pattern
with resource as variable:
    use(variable)
# resource automatically cleaned up after block

# Real example
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed, even if error occurs
# Translation: "Open resource, use it, auto-cleanup when done"

# Multiple contexts
with open('in.txt') as src, open('out.txt', 'w') as dst:
    dst.write(src.read())
```

---

#### Category: Standard Library Highlights

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `collections.Counter` | Count occurrences | 5 | Not Introduced |
| `collections.defaultdict` | Dict with default factory | 6 | Not Introduced |
| `itertools.chain` | Flatten iterables | 7 | Not Introduced |
| `functools.partial` | Pre-fill function args | 7 | Not Introduced |
| `pathlib.Path` | Modern file paths | 4 | Not Introduced |

**Pattern Details:**

```python
# Counter
from collections import Counter

# Basic pattern
Counter(iterable)

# Real example
words = ['apple', 'banana', 'apple', 'cherry', 'apple']
counts = Counter(words)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
counts.most_common(2)  # [('apple', 3), ('banana', 1)]
# Translation: "Count occurrences of each unique element"
```

```python
# defaultdict
from collections import defaultdict

# Basic pattern
defaultdict(factory_function)

# Real example
groups = defaultdict(list)
groups['fruits'].append('apple')  # No KeyError, auto-creates empty list
groups['fruits'].append('banana')
# groups = {'fruits': ['apple', 'banana']}
# Translation: "Dict that auto-creates missing keys with factory"

# vs regular dict
regular = {}
regular['fruits'].append('apple')  # KeyError!
```

---

## Tracking Summary Table

**Status Legend:**
- **Not Introduced:** Haven't covered yet
- **Learning:** Currently drilling (4-5 day window)
- **Adopted:** Can use without template
- **Fluency Pool:** In rotation for continued reinforcement

| Module | Patterns Introduced | Current Learning | Adopted This Module |
|--------|---------------------|------------------|---------------------|
| 1 | List comprehension, range, basic loops | — | List comp, range |
| 2 | enumerate, zip basic, .items(), .split(), default args, conditional expression | — | enumerate, zip, .items(), conditional expression |
| 3 | (ML-focused, minimal Python pattern drilling) | — | — |
| 4 (current) | .get(), try/except, *args/**kwargs, with open, f-strings | — | — |
| 5 | dict comp, sorted with key, lambda, any/all, generator expressions | — | — |
| 6 | Classes/OOP basics, type hints, defaultdict | — | — |
| 7+ | Decorators, yield, advanced patterns | — | — |

---

## Module-by-Module Introduction Schedule

### Pacing Rule (Apply to All Modules)

**Maximum 4 patterns per module. Minimum 4 consecutive days drilling each.**

If a module has fewer training days, reduce patterns proportionally. Never sacrifice depth for breadth.

---

### Module 3 (Complete) — Lesson Learned

Module 3 focused heavily on ML concepts (train/test split, classification, model evaluation). Python pattern drilling was too scattered — exposure without repetition. Patterns originally scheduled here are carried forward to Module 4+.

**Outcome:** No new patterns reached Adopted status. Schedule revised for sustainable pacing.

---

### Module 4 (Current) — API Integration

**Duration:** ~20 training days  
**Patterns:** 4 (5 days each)

| Days | Pattern | Why This Module |
|------|---------|-----------------|
| 1-5 | `.get()` for safe dict access | API responses are dicts; safe access prevents KeyError crashes |
| 6-10 | `try/except` with specific exceptions | API calls fail; graceful error handling is essential |
| 11-15 | `*args`/`**kwargs` | Wrapper functions, flexible API interfaces |
| 16-20 | `with open()` + `pathlib.Path` | File handling for configs, data, API responses |

**Also reinforce during module:**
- f-string formatting (output formatting for APIs)
- `any()`/`all()` (validation of API responses)

---

### Module 5 — Advanced ML

**Duration:** ~20 training days  
**Patterns:** 4 (5 days each)

| Days | Pattern | Why This Module |
|------|---------|-----------------|
| 1-5 | Dict comprehension | Feature engineering, data transformation |
| 6-10 | `sorted()` with `key=` + lambda | Custom sorting for feature importance, rankings |
| 11-15 | Generator expressions | Memory efficiency with large datasets |
| 16-20 | `Counter` | Analyzing class distributions, value frequencies |

---

### Module 6 — NLP

**Duration:** ~20 training days  
**Patterns:** 4 (5 days each)

| Days | Pattern | Why This Module |
|------|---------|-----------------|
| 1-5 | Classes/OOP basics | Custom text processors, pipeline components |
| 6-10 | `.join()` + string methods | Text assembly, tokenization |
| 11-15 | `defaultdict` | Building vocabularies, word counts |
| 16-20 | Type hints | Professional code quality for larger projects |

---

### Module 7+ — Deep Learning & Beyond

**Patterns deferred to these modules:**
- Decorators (`@property`, `@staticmethod`)
- `yield` and advanced generators
- `itertools` patterns
- Advanced OOP (inheritance, class attributes)

These become relevant when building custom model classes, training loops, and production code.

---

## Critical Reminders for Claude

**When generating weekly Foundation Drilling docs:**
1. Check this document for which patterns are scheduled
2. Check status column — don't re-introduce "Adopted" patterns as new
3. **Same pattern for 4-5 consecutive days minimum**
4. Part 1a = fluency rep from Adopted pool
5. Part 1b = current "Learning" pattern (NOT a new one each day)
6. Use teaching format: Pattern → Example → Translation → Variations

**When a pattern moves status:**
1. Update the tracking table in this document
2. Note date of status change
3. Adopted patterns enter fluency rotation

**When user asks about unfamiliar syntax:**
1. Check if it's in this catalog
2. If yes, use teaching format and mark as "Learning"
3. If no, add it to appropriate category
4. **Do not let ad-hoc questions derail the current pattern's drilling window**

**Pacing enforcement:**
- If user hasn't demonstrated mastery of current pattern, do not advance
- "I've seen it" ≠ "I can use it"
- Ask user to write pattern from memory before advancing

---

## End of Python Patterns Master

**This document is the single source of truth for Python fluency curriculum.**

**Referenced by:** Weekly Foundation Drilling docs, daily workflow structure  
**Updated when:** Patterns change status, new patterns identified  
**Reviewed:** Start of each module to confirm schedule alignment
