If the conjecture were false, there would be at least one map with the smallest
possible number of regions that requires five colors, the proof showed that
such a minimal counterexample cannot exists.

1.  An _unavoidable set_ is a set of configurations such that every map that
    satisfies some necessary conditions for being a minimal non-4-colorable map
    (such as minimum degree of 5) must have atleast one configurations from the
    set.
2.  A _reducible configuration_ is an arrangemnet of countries that cannot
    occur in a minimal counterexample. If a map contains a reducible
    configuration, then the map can be reduced to a smaller map. This smaller
    map has the condition that if it can be colored with four colors, then the
    original map can also. This implies that if the original map cannot be
    colored with four colors the smaller map can't either and so the original
    map is not minimal.

Appel and Haken found an unavoidable set of reducible configurations, thus
proving that a minimal counterexample to the four-color conjecture could not
exist. Their proof reduced the infinitude possible maps to 1,936 reducible
configurations which had to be checked one by one by computers. The
reducibility part of the work was checkd by many different computers and
programms. However the unavoidability part of the proof was hand checked.

The proof used the following logic:

First we can make any graph triangulated by adding edges without adding new
verticies. If the triangulated graph is four colorable, then so is the original
graph since the same coloring is valid if edges are removed. Thus we only need
to prove it for triangulated graphs.

Using Eulers formula they were able to show that there is atleast one vertex of
degree 5 or less.

If there is a graph requirering 5 colors, then there is a minimal graph where
removing any vertex maks it four colorable. Then this graph cannot have a
vertex of degree 3 or less, because we can remove that vertex, and just connect
the edges, then four color this smaller graph, then add back in the vertex, and
extend the four coloring by choosing a color different from its neighbors.

If a graph has verticy of degree 4 then when a vertex is removed, then colored.
Then any such coloring can be modified such that when the new color is added
back, the larger graph is four colorable.

The the real work came with the degree 5 vertex.

Finaly, they needed to generate the unavoidable set. This is the set that any
other graph can be reduced to using the methods described, and some other
rules. The method for generating this set of configurations is extreamly
complex. It was used to generate the 1,936 graphs, that every posible counter
example could be reduced to. And showed that each of these were four colorable.
Thus showing that there cannot be a valid counter example, and that any planar
graph must be four colorable.
