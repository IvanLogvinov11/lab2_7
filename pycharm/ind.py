#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # Universe
    u = set("abcdefghijklmnopqrstuvwxyz")

    # Set Data
    a = {"c", "g", "h", "k", "y"}
    b = {"a", "b", "k", "n", "u"}
    c = {"i", "j", "o", "y", "z"}
    d = {"a", "b", "f", "g", "y", "z"}

    # Definition X
    x = d.intersection(a.union (b))
    print(f'X =  {x}')

    # Inverses for a b and c
    ne_a = u.difference(a)
    ne_b = u.difference(b)
    ne_c = u.difference(c)

    # Definition Y
    y = (ne_a.intersection(d)).union(ne_c.difference(ne_b))
    print(f'Y = {y}')
