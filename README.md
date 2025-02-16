# Memory Game


A fun and interactive memory-matching game built with Python and Tkinter!

This project is designed to help you practice fundamental Python programming concepts, including:

* Variables and Data Types 
* User Input 
* Basic Operators 
* Conditional Statements 
* Loops 
* Functions 

## Essential Concepts

### Variables and Data Types 
**Variable:** A named object that stores data in memory.

**Data Type:** Defines the type of data stored in memory, usually in a variable.

In Python the basic Data Types are:

* **Int** - Integer number (e.g, 10, -3, 42)
* **float** - Decimal numbers (e.g., 3.14, -0.5, 2.0)
* **str** - Strings (text) (e.g., "Hello", 'Python')
* **bool** - Boolean values (True or False)
* **list** - Ordered collections (e.g., [1, 2, 3])

### User Input 
User Input allows the program to receive data from the user, typically trough the keyboard, using: 

```python
name = input ('Enter your name: ')
print("Hello, " + name + "!")
```

### Basic Operators 
Python provides different types of operators, including:


* **Arithmetic Operators** (+, -, *, /, //, %, **)
* **Logical Operators** (and, or, not)
* **Bitwise Operators** (&, |, ^, ~, <<, >>)

### Conditional Statements 
Conditional statements allow the program to make decision using boolean logic:

```Python
age = 18 
if age >= 18:
    print("You are an adult.")
else: 
    print("You are a minor.")
```

### Loops 
Loops allow repeated execution of a block of code while a condition holds true: 

```Python
for i in rage(5):
    print("Iteration:", i)
```

### Functions
Functions are reusable blocks of code that perform a specific task:

```Python 
def greet(name):
    return "Hello, " + name 

print(greet("Alice"))
```

## Game Features 

The Game will include the following features 

1.  4x4 grid with randomly place image pairs
2. Click to reveal and match cards
3. Timer and score tracking
4. Simple UI with images from Pixabay



## Image Assets

To use images, download them from [Pixabay](https://pixabay.com/).


## Prerequisites
1. Make sure you have Python 3.x installed. You can check by running:
```sh
python3 --version 
```
If Python 3.x is missing, refer to [this page](https://www.python.org/downloads/) for installation steps.

2. Make sure you have Tkinter installed. It comes with Python 
by default, but if missing, refer to [this guide](https://tkdocs.com/tutorial/install.html) for installation steps.


## Installation & Usage
1. Clone the repo 
```sh
git clone https://github.com/eduardorobless/memoryGame
cd memoryGame
```

2. Run the game
```sh
python3 memory.py
```


## How It Works 
* Click on a card to reveal its image. 
* Try to find and match its pair.
* The game ends when all pairs are matched or when time is out!.


## License
This project is licensed under **The Unlicense**, which means it is fully in the public domain.
You can **use, modify, and distribute** this project **without any restrictions**.

For more details see the [LICENSE](LICENSE) file.
