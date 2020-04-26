---
marp: true
theme: uncover
paginate: true
header: "The Word Problem for Automatic Groups"
footer: "Arden Rasmussen"
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

---

## Outline

- The Word Problem
  - What is it?
  - Motivation
  - Cyclic Group of Order $3$
- ShortLex
- Knuth-Bendix Algorithm
- Finite State Automata
- Solving the Word Problem

---

<!--_class: invert-->

## **The Word Problem**

---

### What is it?

The most common form of the word problem is; given two representations of
elements in a set, determine if the two expressions are equivalent.

---

### Motivation

Consider the group $D_4=\left\langle r,s\vert r^4=s^2=(sr)^2=1\right\rangle$,
then the question becomes:

> Are $rrsrsr^{-1}ssrssrrs^{-1}r^{-1}s$ and $rsr^{-1}r^{-1}srrrs^{-1}r^{-1}s$
> the same? And can we always tell if two sequences of generators are the same.

---

### Cyclic Group Of Order 3

To demonstrate the proof of the word problem, we will directly prove that it
is solvable for the cyclic group of order 3.

$$
\mathbb{Z}_3=\left\langle x\vert x^3=1\right\rangle
$$

---

#### (Cyclic Group Of Order 3) Step 1

First we construct our alphabet for this group. Since we only have one
generator $x$ it will simply be

$$
\Sigma=\left\{x,x^{-1}\right\}
$$

---

#### (Cyclic Group Of Order 3) Step 2

Now we construct our initial list of relations

$$
\begin{aligned}
xxx&= e\\
xx^{-1}&= e\\
x^{-1}x&= e\\
\end{aligned}
$$

---

$$
\begin{aligned}
e&= e\\
xx^{-1}&= e\\
xx^{-1}xx^{-1}&= e\\
xx^{-1}xx^{-1}xx^{-1}&= e\\
xxxx^{-1}x^{-1}x^{-1}&= e\\
x^{-1}x^{-1}x^{-1}&= e
\end{aligned}
$$

---

$$
\begin{aligned}
x^{-1}&=ex^{-1}\\
&=xxxx^{-1}\\
&=xx
\end{aligned}
$$

$$
\begin{aligned}
x^{-1}x^{-1}&=ex^{-1}x^{-1}\\
&=xxxx^{-1}x^{-1}\\
&=x
\end{aligned}
$$

---

#### (Cyclic Group Of Order 3) Step 3

The final set of relations available are listed below

1. $xxx=e$
2. $xx^{-1}=e$
3. $x^{-1}x=e$
4. $x^{-1}x^{-1}x^{-1}=e$
5. $x^{-1}=xx$
6. $x^{-1}x^{-1}=x$

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

---

If we attempted this same process with only the basic relations we would get

$$
\begin{aligned}
w&=xxxx^{-1}x^{-1}x^{-1}x^{-1}\\
(1)&\rightarrow x^{-1}x^{-1}x^{-1}x^{-1}\\
\end{aligned}
$$

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

---

<!--_class: smallFont--->

This means that without our new releations, we would have that
$w=x^{-1}x^{-1}x^{-1}x^{-1}=x^{-1}$, and we would never know that this is
also equivalent to $xx$.

Since we have no way to reduce $x^{-1}$, or $x^{-1}x^{-1}x^{-1}x^{-1}$, then
we are forced to conclude that they are unique elements of the group. However
there is a contradiction, that $w$ is equal to two distinct elements.

---

#### (Cyclic Group Of Order 3) Conclusion

This demonstration shows why it is important to construct these new
relations, as otherwise it may not be possible to reduce the sequence of
generators to the element which it represents.

---

<!--_class: invert-->

## **Shortlex Ordering**

---

Shortlex ordering implements a notion of order for our representations.
Shortlex ordering is simply alphabetical ordering, where shorter words are
considered smaller.

Given the alphabet $\Sigma=\left\{x,y\right\}$, then the ordering is
represented by

$$
<!-- \varepsilon <x<y<xx<xy<yx<yy<\ldots -->
$$

where $\varepsilon$ is the empty string.

---

<!--_class: invert-->

## **Knuth-Bendix Method**

---

### Confluence

Multiple methods that provide the same result. In this case applying the
different relations in different orders ($\mathbb{Z}_3$).

---

The Knuth-Bendix method resolves the lack of confluence, by rewriting the
relations such that there is no conflict of confluence.

---

### Goal

Constructs a set of relations that preserve confluence, and all reducible
elements can be easily reduced by the relations. For $D_4$, $r^2$ cannot be
reduced, but $r^6$ would be reduced to $r^2$.

---

### The Algorithm

Consider the group presented by $\left\langle X\vert R\right\rangle$,
where $X$ is the set of generators, and $R$ is the set of relations given by
$P_i=Q_i$, where $P_i,Q_i\in\Sigma^*$ as defined previously, and $i$ is the
number of relations in $R$.

---

First we construct the initial relations. For this algorithm these relations are
defined in a single direction, so let us assume that by shortlex ordering
$Q_i \lt P_i$, then our first set of relations is given by
$$
P_i\rightarrow Q_i
$$

---

Take $P_i$, $P_j$, with $i\neq j$, where $P_i$ and $P_j$ have some overlap.

1. The prefix of $P_i$ is equal to the suffix of $P_j$. Consider $P_i=BC$ and
   $P_j=AB$.
2. $P_i$ is contained within $P_j$. Let $P_i=B$ and $P_j=ABC$.

---

Consider the word $ABC$, and apply $P_i$ and $P_j$ to get the words $r_i$ and
$r_j$ respectively. If $r_i\neq r_j$, then define the new relations
$$
\max\{r_i,r_j\}\rightarrow\{r_i,r_j\}
$$

---

Remove all relations that this relation can reduce the left side. Repeated this
process until no relations can be reduced.

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
> \delta)$, where $\Sigma$ is the alphabet, $S$ is the non-empty set of
> states, $s_0\in S$ is the initial state, $\delta$ is the state transition
> function $\delta :S\times\Sigma\rightarrow S$.

---

For $D_4$, $\Sigma=\left\{r,r^{-1},s,s^{-1}\right\}$.,
$S=\left\{e,r,r^2,r^3,s,rs,r^2s,r^3s\right\}$, and $s_0=e$.

---

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

To apply an automaton, consider some word $w\in\Sigma^*$, then apply the
relations until none of them can be applied.

Confluence ensures that the order of applying the relations does not matter.

---

After applying all possible relations, then the current state is the result of
the automaton. With this process, we can define the mapping for this automaton
$$
A:\Sigma^*\rightarrow S
$$

---

<!--_class: invert-->

## **The Word Problem For Automata Groups**

---

By the Knuth-Bendix method, we construct a set of relations that preserve
confluence. This ser of relations are then used for the transition function for
a finite state automaton $\delta$. Thus by $A$, we have a mapping
$\Sigma^*\rightarrow S$. Applying $A$ to two words $w,u\in\Sigma^*$ to get
$s_w$, s_u$, which can trivially be checked for equality.
