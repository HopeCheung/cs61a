""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty or link.rest == Link.empty:
        return
    elif link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    elif link.first == value:
        link = link.rest
        remove_all(link, value)
    remove_all(link.rest, value)
    

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return
    elif not isinstance(link.first, Link):
        link.first = fn(link.first)
    else:
        deep_map_mut(fn, link.first)
    deep_map_mut(fn, link.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    link1 = link.rest
    link2 = link.rest.rest
    while link1 != Link.empty and link2!= Link.empty and link2.rest != Link.empty:
        if link1 == link2:
            return True
        link1 = link1.rest
        link2 = link2.rest.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    link1 = link.rest
    link2 = link.rest.rest
    while link1 != Link.empty and link2!= Link.empty and link2.rest != Link.empty:
        if link1 == link2:
            return True
        link1 = link1.rest
        link2 = link2.rest.rest
    return False

# Q9
def reverse_other(t):
    """Reverse the entries of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def reverse_helper(t, need_reverse):
        if t.is_leaf():
            return
        new_labs = [child.label for child in t.branches][::-1]
        for i in range(len(t.branches)):
            child = t.branches[i]
            reverse_helper(child, not need_reverse)
            if need_reverse:
                child.label = new_labs[i]
    reverse_helper(t, True)
        
        
    
