# ToyBot Scenegraph

This repository is the testing ground for the Shoebot 2 scene graph implementation.

## Scene graph specification

A scene graph is a simple collection of nodes, which can be

* **Drawable shapes** to be rendered
* **State changes** that affect other nodes after them

### Shape nodes

```json
{
  "type": "path"
  "coords": [
    [0, 0],
    [0, 100],
    [100, 100],
    [100, 0]
  ]
}
```

### State nodes

```json
{
  "type": "state",
  "target": "fill",
  "value": [0.3, 0.2, 0.1, 0.7]
}
```

```json
{
  "type": "state",
  "target": "size",
  "value": [800, 600]
}
```

