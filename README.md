# multiplexer

This is a library, that takes input commands from the console and then prints the output provided by a handler that is registered with the library.

## Usage

Input entered will be checked with the decorator parameter of function and if it is matched then will print the returned string.

```python
from multiplexer import myplexer
app = myplexer()

@app.route('hello')
def hello_world():
    return 'Hello, World!'

@app.route('bye')
def bye():
    return 'bye'
```
