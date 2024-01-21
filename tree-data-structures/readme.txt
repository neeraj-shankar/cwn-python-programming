Tree Data Structures
-----------------------------------------------------------------------------------------------------------------------
A tree data structure is defined as a collection of objects or entities known as nodes that are linked together to 
represent a hierarchy.

It's a non linear data structure as it does not store data in a sequential manner, but stores in a hierarchical
fashion.


Terminologies and Properties of a Tree:
-----------------------------------------------------------------------------------------

Root
-----------------------------------------------------------
Root node is a node from which the entire tree originates. It does not have a parent

Parent Node	
-----------------------------------------------------------
An immediate predecessor of any node is its parent node.	

Child Node	
-----------------------------------------------------------
All immediate successors of a node are its children

Leaf
-----------------------------------------------------------
Node which does not have any child is a leaf. Usually the boundary nodes of a tree or last nodes of 
the tree are the leaf or collectively called leaves of the tree.

Edge
-----------------------------------------------------------
Edge is the connection represented by a line between one node to another. In a tree with n nodes, 
there will be ‘n-1’ edges in a tree.

Siblings
-----------------------------------------------------------
Nodes with common parents are considered to be siblings.

Path
-----------------------------------------------------------
Path is a number of successive edges from source node to destination node.	

Height of Node
-----------------------------------------------------------
Height of a node represents the number of edges on the longest path between that node and a leaf.	

Levels of node	
-----------------------------------------------------------
Level of a node represents the generation of a node. If the root node is at level 0, then 
its next child node is at level 1, its grandchild is at level 2, and so on