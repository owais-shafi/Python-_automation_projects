import requests
import random
from bs4 import BeautifulSoup

def fetch_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    print("\n>>>  Todays quote of the day is: " + random.choice(quotes).text + "\n")
    # for quote in quotes:
        # print(quote.text)

if __name__ == "__main__":
    fetch_quotes()




# random.choice() is a function from the random module in Python. It selects a random item from a non-empty sequence (such as a list, tuple, or string).
# In this case, the sequence is quotes. This implies that quotes is a list (or similar sequence) containing multiple items, such as text strings, objects, or elements.
# Example:
# quotes = ["Be yourself.", "Stay positive.", "Keep learning."]
# random_quote = random.choice(quotes)
# print(random_quote)
# This will randomly choose one of the quotes from the list and print it.

# .text:

# The .text attribute (or method) is commonly found in libraries like BeautifulSoup (which is used to parse HTML/XML data). It is often used to extract the text content from an HTML tag or element.
# If quotes is a list of objects (like HTML elements), then using .text will extract the inner text from that specific object.
# In Python, the statement `if __name__ == "__main__":` is a common construct used to control the execution of code when a Python file is either **run directly** or **imported** as a module. Here's an explanation of what it means:

# ### Understanding the Components

# 1. **`__name__`**:
#    - Every Python file/module has a special built-in variable called `__name__`.
#    - If the file is **run directly** (for example, by typing `python my_script.py` in the terminal), the value of `__name__` will be `"__main__"`.
#    - However, if the file is **imported** as a module in another script, then the value of `__name__` will be the **name of the module** (the file name without the `.py` extension).

# 2. **`__main__`**:
#    - `"__main__"` is a string, and it represents the name of the top-level script that is being run.

# 3. **`if __name__ == "__main__":`**:
#    - This line checks if the current file is being run directly (not imported). 
#    - If `__name__` is equal to `"__main__"`, it means that the script is being run directly, and the code inside the `if` block will be executed.
#    - If the file is **imported as a module**, this block of code will **not** be executed.

# ### Why Use It?
# This construct allows you to separate the **execution of code** from the **definition of functions** or classes in a module. It ensures that certain code (like tests, main logic, or scripts) is only run when the script is executed directly, not when it's imported elsewhere.

# ### Example:

# ```python
# # my_module.py

# def greet():
#     print("Hello, world!")

# if __name__ == "__main__":
#     # This block will only run if this script is run directly.
#     print("This script is being run directly.")
#     greet()
# ```

# ### Behavior:

# - If you **run** the file directly:
#   ```bash
#   python my_module.py
#   ```
#   Output:
#   ```
#   This script is being run directly.
#   Hello, world!
#   ```

# - If you **import** this file in another script:
#   ```python
#   # another_script.py

#   import my_module

#   my_module.greet()
#   ```
#   Output:
#   ```
#   Hello, world!
#   ```

#   In this case, the block `if __name__ == "__main__":` does not execute, so the message `"This script is being run directly."` is not printed.

# ### Why is it useful?

# - **Modularity**: You can write Python files that have both reusable functions/classes and standalone code for testing.
# - **Testing**: You can add code inside `if __name__ == "__main__":` to test your module's functionality without interfering with other scripts that import the module.
# - **Code reusability**: It makes your code cleaner and more reusable across different projects or scripts without running unintended code when imported.

# This pattern is particularly useful in larger projects and scripts where you want to ensure certain code only runs when the file is executed as a standalone program.
