---
marp: true
theme: uncover
---

<style>
section.multicol p {
    columns: 2;
}
section.smallFont p {
    font-size: 90%;
}
</style>

<!--_class: invert-->

# **The World problem for Automatic Groups**

_Arden Rasmussen_

<!--Hello everyone, I'm going to be talking about the word problem for automatic
groups or automata groups-->

---

## Outline

- The Word Problem
- Knuth-Bendix Algorithm
- Finite State Automata
- Solving the Word Problem

<!--First I'll explain what the word problem is, and why we should care about it-->
<!--Then I'll walk through the process that is the core of the word problem for automatic groups-->
<!--Third I'll explain exactly what Automata are, and how they are related to the word problem-->
<!--Finally we will put everything together to show the solvability for automatic groups-->

---

<!--_class: invert-->

## **The Word Problem**

<!--Starting with the word problem, what it is and why we should care about it-->

---

### Some definition and notation

An alphabet is a set of letters, denoted $\Sigma=\{a,b,\ldots,z\}$. For groups it is the set of generators union with the inverses of generators.

<!--First we need to start with some definitions and notation that are used
throughout the rest of the presentations-->
<!--The starting point is an alphabet. The alphabet is a finite set of
characters, or symbols, each element of the alphabet is called a letter.-->
<!--For groups, the alphabet will be the set of generator, combined with the
inverses of each generator-->

---

### Some definition and notation

An alphabet is a set of letters, denoted $\Sigma=\{a,b,\ldots,z\}$. For groups it is the set of generators union with the inverses of generators.

A language is the "Free monoid" of the alphabet, denoted $\Sigma^*=\{a,aa,\ldots,ab,aba,\ldots\}$. These "words" for groups are products or sums of generators and inverses.

<!--Next we construct the free monoid of the alphabet, and that free monoid is
called the language-->
<!--Quickly the free monoid is simply the set whose elements are all finite
sequences of elements from the group, including the sequence of zero elements,
which is denoted by epsilon.-->
<!--For groups, the language is products or sums of generators and their
inverses, depending on the operation for the group.-->

---

#### Example

For $D_4$, whose generators are given by $X=\{r,s\}$

<!--For a quick example to explain these definitions, lets consider D_4, whose
generates are r, and s.-->

---

#### Example

For $D_4$, whose generators are given by $X=\{r,s\}$

$$
\begin{aligned}
\Sigma &= \{r,s,r^{-1},s^{-1}\}
\end{aligned}
$$

<!--For this group, the alphabet sigma will simply be r and s along with r and
s inverses.-->

---

#### Example

For $D_4$, whose generators are given by $X=\{r,s\}$

$$
\begin{aligned}
\Sigma &= \{r,s,r^{-1},s^{-1}\}\\
\Sigma^* &= \{\varepsilon, r, s, rr, rs, rrr, rrs\ldots\}
\end{aligned}
$$

<!--Then to construct the language for this alphabet, we consider products of
the letters in the alphabet, which in this case will be all products of r, s, r
inverse, and s inverse. Note that these products can be of any finite length.
It cannot be an infinite product.-->

---

### What is it?

The most common form of the word problem is; given two representations of elements in a set, determine if the two expressions are equivalent.

<!--The word problem generally stated is to determine if two words in a language
are equivalent. An equivalent definition is determining if some word is equivalent to the identity element of the group.-->

<!--Doing this for a single pair of words could be possible, but for the word problem to be solvable it must be possible that given any two words, to determine if they are equivalent.-->

---

### Motivation

Consider the group $D_4=\left\langle r,s\vert r^4=s^2=(sr)^2=1\right\rangle$, then the question becomes:

<!--Going back to our previous example of D_4, then the word problem becomes the question of if two products of r, s, and their inverse are equal.-->

---

### Motivation

Consider the group $D_4=\left\langle r,s\vert r^4=s^2=(sr)^2=1\right\rangle$, then the question becomes:

> Are $rrsrsr^{-1}ssrssrrs^{-1}r^{-1}s$ and $rsr^{-1}r^{-1}srrrs^{-1}r^{-1}s$ the same? And can we always tell if two sequences of generators are the same.

<!--Consider this example, we have the tools to do this by hand, but is there some fixed process that can determine the answer for any two words, and will it always be possible? Or when is it not possible?-->
<!--If your curious these two elements are indeed the same, and I believe that they are actually 1.-->

---

### Cyclic Group Of Order 3

To demonstrate the proof that the word problem, we will directly prove that it is solvable for the cyclic group of order 3.

$$
\mathbb{Z}_3=\left\langle x\vert x^3=1\right\rangle
$$

<!--Its much easier to understand the word problem, when given a direct example. So let us consider Z_3.-->

---

#### (Cyclic Group Of Order 3) Step 1

First we construct our alphabet for this group. Since we only have one generator $x$ it will simply be

$$
\Sigma=\left\{x,x^{-1}\right\}
$$

<!--The first set is to construct our alphabet, which will simply be x and x inverse.-->

---

#### (Cyclic Group Of Order 3) Step 2

$$
\mathbb{Z}_3=\left\langle x\vert x^3=1\right\rangle
$$

Now we construct our initial list of relations

$$
\begin{aligned}
(1)&\quad xxx&= e\\
(2)&\quad xx^{-1}&= e\\
(3)&\quad x^{-1}x&= e\\
\end{aligned}
$$

<!--The first relation comes form the given relation x^3=1-->
<!--The second and third relation comes form the definition of inverses.-->

---

$$
\begin{aligned}
e&= xx^{-1}\quad &(2)\\
&=xx^{-1}xx^{-1}\quad &(2)\\
&=xx^{-1}xx^{-1}xx^{-1}\quad &(2)\\
&=xxxx^{-1}x^{-1}x^{-1}\\
&=x^{-1}x^{-1}x^{-1}\quad &(1)
\end{aligned}
$$

<!-- Now we construct some new relations from our initial three relations. So first we consider the identity, then by the second relations, we multiply by the identity three times. Then since Z_3 is abelian, we reorder this this, and finally by applying the first relation, we can remove the three x's, and are left with three x inverse's, this gives us a new relation-->

---

$$
\begin{aligned}
x^{-1}&=ex^{-1}\\
&=xxxx^{-1}\quad &(1)\\
&=xx\quad &(2)
\end{aligned}
$$

<!--Now we construct a second relation, by first considering x inverse, and multiplying by the identity, and applying the first relation, and then reducing by applying the second relation. we are now left with a new relation from x inverse to x squared.-->

---

$$
\begin{aligned}
x^{-1}x^{-1}&=ex^{-1}x^{-1}\\
&=xxxx^{-1}x^{-1}\quad &(1)\\
&=x\quad &(2)(2)
\end{aligned}
$$

<!-- Using the same process, we construct a final relation from x inverse x inverse to x-->

---

#### (Cyclic Group Of Order 3) Step 3

The final set of relations available are listed below

1. $xxx=e$
2. $xx^{-1}=e$
3. $x^{-1}x=e$
4. $x^{-1}x^{-1}x^{-1}=e$
5. $x^{-1}=xx$
6. $x^{-1}x^{-1}=x$

<!--The final set of relations are [READ THEM]. Using this set of relations, we can take any word in the language for this, and rewrite it to be one of 1, x, or xx.-->

---

#### (Cyclic Group Of Order 3) Verification

Lets verify this with $w=xxxx^{-1}x^{-1}x^{-1}x^{-1}$.

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
\end{aligned}
$$

<!-- Lets check that these relations actually do what we want, so consider this w.-->

---

#### (Cyclic Group Of Order 3) Verification

Lets verify this with $w=xxxx^{-1}x^{-1}x^{-1}x^{-1}$.

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(1)&\rightarrow x^{-1}x^{-1}x^{-1}x^{-1}\\
\end{aligned}
$$

<!-- First we apply relation 1 to remove the x cubed from the begining.-->

---

#### (Cyclic Group Of Order 3) Verification

Lets verify this with $w=xxxx^{-1}x^{-1}x^{-1}x^{-1}$.

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(1)&\rightarrow x^{-1}x^{-1}x^{-1}x^{-1}\\
(4)&\rightarrow x^{-1}\\
\end{aligned}
$$

<!--Now we apply the fourth relation, to remove three of the x inverse.-->

---

#### (Cyclic Group Of Order 3) Verification

Lets verify this with $w=xxxx^{-1}x^{-1}x^{-1}x^{-1}$.

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(1)&\rightarrow x^{-1}x^{-1}x^{-1}x^{-1}\\
(4)&\rightarrow x^{-1}\\
(5)&\rightarrow xx\\
\end{aligned}
$$

<!-- Finally we use the fifth relation to convert the x inverse to x squared.-->

---

If we attempted this same process with only the basic relations we would get

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(1)&\rightarrow x^{-1}x^{-1}x^{-1}x^{-1}\\
\end{aligned}
$$

<!--If we attempted this without our new relations, then we would have only been able to apply the first relation, and after that step we would have been stuck with four x inverses.-->

---

Or by a different process, we could get

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(2)&\rightarrow xxx^{-1}x^{-1}x^{-1}\\
(2)&\rightarrow xx^{-1}x^{-1}\\
(2)&\rightarrow x^{-1}\\
\end{aligned}
$$

<!--A different approach, would be to instead apply the second relation three times, and that process results in x inverse.-->

---

<!--_class: smallFont--->

This means that without our new releations, we would have that $w=x^{-1}x^{-1}x^{-1}x^{-1}=x^{-1}$, and we would never know that this is also equivalent to $xx$.

Since we have no way to reduce $x^{-1}$, or $x^{-1}x^{-1}x^{-1}x^{-1}$, then we are forced to conclude that they are unique elements of the group. However there is a contradiction, that $w$ is equal to two distinct elements.

<!--This means that without our relations, we would have been left with two distinct elements that the process claims are both equal to w, however our goal is that after applying all possible relations, every element should be unique.-->

---

### Non Examples

Non examples do exist, but they can get very complex.

<!--There are some examples which have been shown that the word problem is not solvable, but those examples are relatively complex, If any one is very curious, I can show you one of them, but I will not work through the proof that the word problem is not solvable for it.-->
<!--Most "non" examples are groups where the solvability of the word problem has not been proven or disproven, and those are not very intresting.-->

---

## **Shortlex Ordering**

Shortlex ordering implements a notion of order for our representations. Shortlex ordering is simply alphabetical ordering, where shorter words are considered smaller.

Given the alphabet $\Sigma=\left\{x,y\right\}$, then the ordering is represented by

$$
\varepsilon <x<y<xx<xy<yx<yy<\ldots
$$

where $\varepsilon$ is the empty string.

<!--For quick tangent, lets talk about Shortlex ordering. This is simply a method to apply ordering to the words in the language, even if the group itself does not possess any ordering.-->
<!--Generally it is just alphabetical ordering of the words, exactly how a dictionary would be ordered.-->

---

<!--_class: invert-->

## **Knuth-Bendix Method**

<!--So the knuth-bendix method, is the core process that is used to show the solvability of the word problem for automatic groups.-->

---

### Confluence

Multiple methods that provide the same result. In this case applying the different relations in different orders (Example \$\mathbb\_{Z}\_3).

<!--Clearly the order which we apply these relations, should not result in different answers, so we need this to be fixed for our algorithm to work.-->
<!-- As we noted with our example of Z_3, we saw that the same element was equivalent to two different values-->
<!-- This is a conflict of confluence, and the relations that we have do not preserve confluence-->

---

The Knuth-Bendix method resolves the lack of confluence, by rewriting the relations such that there is no conflict of confluence.

---

### Goal

Constructs a set of relations that preserve confluence, and all reducible elements can be easily reduced by the relations. For $D_4$, $r^2$ cannot be reduced, but $r^6$ would be reduced to $r^2$.

---

### The Algorithm

Consider the group presented by $\left\langle X\vert R\right\rangle$, where $X$ is the set of generators, and $R$ is the set of relations given by $P_i=Q_i$, where $P_i,Q_i\in\Sigma^*$ as defined previously, and $i$ is the number of relations in $R$.

---

First we construct the initial relations. For this algorithm these relations are defined in a single direction, so let us assume that by shortlex ordering $Q_i \lt P_i$, then our first set of relations is given by

$$
P_i\rightarrow Q_i
$$

---

Take $P_i$, $P_j$, with $i\neq j$, where $P_i$ and $P_j$ have some overlap.

1. The prefix of $P_i$ is equal to the suffix of $P_j$. Consider $P_i=BC$ and
   $P_j=AB$.
2. $P_i$ is contained within $P_j$. Let $P_i=B$ and $P_j=ABC$.

---

Consider the word $ABC$, and apply $P_i$ and $P_j$ to get the words $r_i$ and $r_j$ respectively. If $r_i\neq r_j$, then define the new relations

$$
\max\{r_i,r_j\}\rightarrow\{r_i,r_j\}
$$

---

Remove all relations that this relation can reduce the left side. Repeated this process until no relations can be reduced.

---

### Example

$$
G=\left\langle x,y\vert x^3=y^3=(xy)^3=1\right\rangle
$$

$$
\begin{aligned}
x^3 &\rightarrow 1\\
y^3 &\rightarrow 1\\
xyxyxy &\rightarrow 1
\end{aligned}
$$

---

$P_1$ and $P_3$ overlap, so confider $x^3yxyxy$, and we reduce that

$$
\begin{aligned}
x^3yxyxy\rightarrow yxyxy\quad x^3yxyxy\rightarrow x^2
\end{aligned}
$$

---

$P_1$ and $P_3$ overlap, so confider $x^3yxyxy$, and we reduce that

$$
\begin{aligned}
x^3yxyxy\rightarrow yxyxy\quad x^3yxyxy\rightarrow x^2
\end{aligned}
$$

Define $yxyxy\rightarrow x^2$.

---

$P_1$ and $P_3$ overlap, so confider $x^3yxyxy$, and we reduce that

$$
\begin{aligned}
x^3yxyxy\rightarrow yxyxy\quad x^3yxyxy\rightarrow x^2
\end{aligned}
$$

Define $yxyxy\rightarrow x^2$.
Remove $xyxyxy\rightarrow 1$.

---

Repeating this process the set of relations become

$$
\begin{aligned}
x^3 &\rightarrow 1\\
y^3 &\rightarrow 1\\
yxyx &\rightarrow x^2y^2\\
y^2x^2 &\rightarrow xyxy
\end{aligned}
$$

---

<!--_class: invert-->

## **Automata Groups**

---

> A finite state automaton is defined as the quintuple $(\Sigma, S, s_0,
\delta)$, where $\Sigma$ is the alphabet, $S$ is the non-empty set of states, $s_0\in S$ is the initial state, $\delta$ is the state transition function $\delta :S\times\Sigma\rightarrow S$.

---

For $D_4$, $\Sigma=\left\{r,r^{-1},s,s^{-1}\right\}$.,
$S=\left\{e,r,r^2,r^3,s,rs,r^2s,r^3s\right\}$, and $s_0=e$.

---

<!--_class: smallFont--->

| $\delta$ | $r^4$  | $s^2$  | $rsrs$ |
| -------- | ------ | ------ | ------ |
| $e$      | $e$    | $e$    | $e$    |
| $r$      | $r$    | $r$    | $r$    |
| $r^2$    | $r^2$  | $r^2$  | $r^2$  |
| $r^3$    | $r^3$  | $r^3$  | $r^3$  |
| $s$      | $s$    | $s$    | $s$    |
| $rs$     | $rs$   | $rs$   | $rs$   |
| $r^2s$   | $r^2s$ | $r^2s$ | $r^2s$ |
| $r^3s$   | $r^3s$ | $r^3s$ | $r^3s$ |

---

To apply an automaton, consider some word $w\in\Sigma^*$, then apply the relations until none of them can be applied.

Confluence ensures that the order of applying the relations does not matter.

---

After applying all possible relations, then the current state is the result of the automaton. With this process, we can define the mapping for this automaton

$$
A:\Sigma^*\rightarrow S
$$

---

<!--_class: invert-->

## **The Word Problem For Automata Groups**

---

By the Knuth-Bendix method, we construct a set of relations that preserve confluence. This ser of relations are then used for the transition function for a finite state automaton $\delta$. Thus by $A$, we have a mapping $\Sigma^*\rightarrow S$. Applying $A$ to two words $w,u\in\Sigma^*$ to get $s_w$, $s_u$, which can trivially be checked for equality.

---

Thus we have shown, that if the Knuth-Bendix algorithm succeeds, we have also shown that the word problem is solvable by the use of finite state automaton.
