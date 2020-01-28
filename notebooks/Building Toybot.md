---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
Building a simple graphics language based on a scene graph.


SceneGraph
==

The scenegraph stores operations as nodes.

These include that change state (fill, stroke etc) and operations that result in elements being drawn (path)
<!-- #endregion -->

```python
class SceneGraph:
    def __init__(self):
        self.nodes = []
        
    def add_node(self, node):
        self.nodes.append(node)
    
    def __iter__(self):
        """Iterates over every node in the graph
        """
        yield from self.nodes.__iter__()
```

## Nodes

### Path

We'll start with the simplest shape -- a path made of straight lines -- and later implement new ones once we agree on a clear structure for the node/graph architecture.

It should only need:

* The minimum number of vars to store values
* methods to edit the path
* a method to represent the path in the repl to aid debugging.

We will probably want a `Node` base class, but let's start simple.

```python
class Path:
    def __init__(self, coords=None):
        if coords is None:
            self.coords = []
        else:
            self.coords = coords
    
    def add_point(self, x, y):
        self.coords.append((x, y))

    def __repr__(self):
        return f'<Path: {self.coords}>'
```

Let's try it now:

```python
p = Path()
p.add_point(10, 10)
p.add_point(10, 100)
p.add_point(100, 100)
p.add_point(100, 10)

print(p)
```

Now it's time to create an instance of our scene graph and add this path to it, so we can render it later.

```python
graph = SceneGraph()
graph.add_node(p)
```

ConsoleRenderer
==

The ConsoleRenderer outputs every node of scenegraph to the console.

JSON is the default output format, to make data transfer easy.

Data formats are changed by passing a function to `outputformat` that accepts nodes and returns data in the desired format.


```python
import jsons

class ConsoleRenderer:
    def __init__(self, outputformat=jsons.dumps):
        if not outputformat:
            outputformat = lambda data: data
        self.outputformat=outputformat
    
    def render(self, graph):
        print(self.outputformat([node for node in graph]))
```

Now render our graph:

```python
renderer = ConsoleRenderer()
renderer.render(graph)
```

If JSON is not required, setting `outputformat` to None will output the scene graph content in the format used by the python repl:

```python
renderer = ConsoleRenderer(outputformat=None)
renderer.render(graph)
```

Grammar
==

The ToyBot class provides the user-facing API for drawing and setting up colours.

```python
class ToyBot:
    def __init__(self, graph):
        self.graph = graph
    
    def rect(self, x, y, width, height, fill=None, stroke=None):
        p = Path(coords=[(x, y),
                         (x, y+height),
                         (x+width, y+height),
                         (x+width, y)])
        self.graph.add_node(p)
```

# Scripting


## Setup the scripting namespace

This function adds all the user-facing API of a bot into a namespace to enable scripting.

```python
import inspect

def create_scripting_namespace(bot):
    namespace = {}
    for name, method in inspect.getmembers(bot, predicate=inspect.ismethod):
        if name.startswith('__'):
            continue
        namespace[name] = method
    return namespace
```

## Running a script

The run function accepts a bot script, does the setup needed to render a bot and then renders.

```python
def run(source):
    renderer = ConsoleRenderer()
    
    graph = SceneGraph()
    bot = ToyBot(graph)

    namespace = create_scripting_namespace(bot)
    
    exec(source, namespace)

    renderer.render(graph)
```

## Putting it all together - using the scripting interface

The scripting interface provides the simplest way of using ToyBot.

Pass the code to render to run function.

```python
code = """
rect(0, 0, 100, 100)
rect(25, 30, 50, 70)
"""

run(code)
```
