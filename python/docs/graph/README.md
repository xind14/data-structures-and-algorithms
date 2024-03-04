
# Graph

Branch Name: graph

Challenge Type: New Implementation

## Whiteboard Process

<!-- Embedded whiteboard image -->
None. Not a whiteboard

## Approach & Efficiency

1. Graph
    - Create a Graph class
2. The class should contain the following methods
    - add vertex
        - Arguments: value
        - Returns: The added vertex
        - Add a vertex to the graph
    - add vertices
        - Arguments: none
        - Returns:  all of the vertices in the graph as a collection (set, list, or similar) 
        - Empty collection returned if there are no vertices

    - get edge
        - Arguments: 2 vertices to be connected by the edge, weight (optional)
        - Returns: nothing
        - Adds a new edge between two vertices in the graph
        - If specified, assign a weight to the edge
        - Both vertices should already be in the Graph

    - get neighbors 
        - Arguments: vertex
        - Returns: collection of edges connected to the given vertex
            - Include the weight of the connection in the returned collection
        - Empty collection returned if there are no vertices

    - size
        - Arguments: none
        - Returns the total number of vertices in the graph
        - 0 if there are none

## Solution


[Link to code](../../data_structures/graph.py)
