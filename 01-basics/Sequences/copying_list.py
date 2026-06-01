
"""
===================================================================================================
                                        SHALLOW COPY
===================================================================================================
"""
# Case 1 — List of Integers (Immutable Elements)
mylist = [1, 2, 3, 4, 5]
mylist_shallow = mylist.copy()
mylist_shallow[1] = 10

print(mylist)         # [1, 2, 3, 4, 5]  ← UNCHANGED
print(mylist_shallow) # [1, 10, 3, 4, 5]

# Memory model after copy
""""
===================================================================================================
mylist         →  [ ref→1 | ref→2 | ref→3 | ref→4 | ref→5 ]
                       ↓       ↓       ↓       ↓       ↓
                       1       2       3       4       5   (int objects)
                       ↑       ↑       ↑       ↑       ↑
mylist_shallow →  [ ref→1 | ref→2 | ref→3 | ref→4 | ref→5 ]
===================================================================================================

When you do mylist_shallow[1] = 10, you're replacing the reference at slot 1 of mylist_shallow to point 
to 10 instead of 2. The original mylist slot 1 still points to 2. Both lists are independent containers — 
you're only changing which object a slot points to, not mutating a shared object.
===================================================================================================
"""

"""
Case 2 — List containing a Nested List (Mutable Element)
===================================================================================================

Memory Model after copy()
-----------------------------------------------------------------------------------------
mylist         →  [ ref→1 | ref→[2,3] | ref→4 | ref→5 ]
                               ↓
                            [2, 3]   ← SHARED nested list object
                               ↑
mylist_shallow →  [ ref→1 | ref→[2,3] | ref→4 | ref→5 ]
-----------------------------------------------------------------------------------------

===================================================================================================
Both lists hold a reference to the very same [2, 3] list object. When you do mylist_shallow[1][0] = 10, 
you are:

Following mylist_shallow[1] → arrives at the shared [2, 3] object
Mutating that object in-place → it becomes [10, 3]

Since mylist[1] points to the same object, it sees [10, 3] too. 
You didn't swap out a reference — you reached inside the shared object and changed it.
===================================================================================================
"""
# Case 2 — List containing a Nested List (Mutable Element)
mylist = [1, [2, 3], 4, 5]
mylist_shallow = mylist.copy()
mylist_shallow[1][0] = 10

print(mylist)         # [1, [10, 3], 4, 5]  ← ALSO CHANGED!
print(mylist_shallow) # [1, [10, 3], 4, 5]


"""
===================================================================================================
                                        DEEP COPY
===================================================================================================
"""
import copy
mylist_deep = copy.deepcopy(mylist)
mylist_deep[1][0] = 999

print(mylist)      # [1, [2, 3], 4, 5]  ← untouched
print(mylist_deep) # [1, [999, 3], 4, 5]
