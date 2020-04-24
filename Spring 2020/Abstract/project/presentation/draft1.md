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

## Knuth-Bendix Method

---

### Confluence

Multiple methods that provide the same result. In this case applying the
different relations in different orders ($\mathbb{Z}_3$).

---

The Knuth-Bendix method resolves the lack of confluence, by rewriting the
relations such that there is no conflict of confluence.

---

### The Algorithm
