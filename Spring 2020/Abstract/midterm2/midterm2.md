---
title: Midterm2
author: Arden Rasmussen
date: 2020-04-15
documentclass: amsart
---

# Problem 1

> Festival of finite abelian groups.

## a

> Please prove that $\mathbb{Z}/7\mathbb{Z}\times\mathbb{Z}/7\mathbb{Z}$ is not
> isomorphic to $\mathbb{Z}/49\mathbb{Z}$.

By Proposition 5.2.6 we known
$\mathbb{Z}/7\mathbb{Z}\times\mathbb{Z}/7\mathbb{Z}\cong\mathbb{Z}/49\mathbb{Z}$
if and only if $gcd(7,7)=1$, but clearly $gcd(7,7)=7$, so we conclude that
$\mathbb{Z}/7\mathbb{Z}\times\mathbb{Z}/7\mathbb{Z}\not\cong\mathbb{Z}/49\mathbb{Z}$.

## b

> Let $A$ be an abelian group of order $392$. List all possible isomorphism
> classes of $A$.

By the fundamental theorem of finite abelian groups, we will first consider the
factorization of $|A|=392=2^3\cdot7^2$. Thus the list of all isomorphism
classes of $A$ are given below

* $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_7\times\mathbb{Z}_7$
* $\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_7\times\mathbb{Z}_7$
* $\mathbb{Z}_8\times\mathbb{Z}_7\times\mathbb{Z}_7$
* $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_{49}$
* $\mathbb{Z}_4\times\mathbb{Z}_2\times\mathbb{Z}_{49}$
* $\mathbb{Z}_8\times\mathbb{Z}_{49}$

**NOTE:** from $a$, the first half or the second half may not be valid?

## c

> Assume further that $A$ contains an element of order $196$. List the possible
> isomorphism classes of $A$.

From the work of (1.b), we already have all possible isomorphism classes. To
enforce the existance of an element of order $196$, then we must have a cyclic
group of at least order $196$, so we are left with

* $\mathbb{Z}_{196}\times\mathbb{Z}_2$.

## d

> Let
> $G=\mathbb{Z}/49\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$.
> Find subgroup $H,K$ of $G$ both of order $2$ so that $G/H$ and $G/K$ are not
> isomorphic.

# Problem 2

> Suppose a group of prime order $p$ acs on a finite set. What are the possible
sizes of the orbits of this action?

# Problem 3

> Here is a nice fact: "If $G$ is a finite group and $p$ is a prime dividing
$|G|$, then $G$ has an element of order $p$". There are many proofs of this
fact. For this problem, please follow the steps below to prove this result.

## a

> Let $S$ denote the set of ordered $p$-tuples of element sof $G$ the product
> of whose coordinates is $1$. So
> $$
> X=\left\{(x_1,x_2,\ldots,x_p):x_i\in G \text{ and } x_1x_2\cdots x_p=1\right\}.
> $$
> Show that $S$ contains $|G|^{p-1}$ elements.

## b

> We would like to define an action of the cyclic group of order $p$, $C_p$, on
> $S$. Do this by letting a permutation act on the indices of an element of $S$.
> Please prove that this is a group action.

## c

> Using your work above, including Problem 2, prove the nice fact.

# Problem 4

> The Class Equation expresses the order of a finite group as the sum of a list
of natural numbers $n_1+n_2+\cdots+n_k$. Consider the following sums. Please
rule out those that could not appear on the right hand side of the Class
Equation. Please explain your reasoning.

## a

> $3+2+5$

## b

> $1+2+2+5$

## c

> $1+2+3+4$

## d

> $2+2+2+2+2$

# Problem 5

> Let $E/F$ be an extension of files. Suppose $f(x),g(x)\in F[x]$ are not both
zero. Let $d_F(x)$ be the gcd of $f(x)$ and $g(x)$ in $F[x]$. Now view
$f(x),g(x)$ as elements of $E[x]$, and let $d_E(x)$ be the gcd of $f(x)$ and
$g(x)$ in $E[x]$. Show $d_F(x)=d_E(x)$. (This is a bit surprising since various
questions involving divisibility such as irreducibility depend on the field be
used.)

# Problem 6

> The algebraic numbers $\mathcal{A}$ are all numbers in $\mathbb{C}$ that are
algebraic over $\mathbb{Q}$. They are a subfield of $\mathbb{C}$; you can
assume this without proof. (Its not a bad proof, feel free to enjoy it in a
non-test setting.) Please prove that $\mathcal{A}$ is not a finite extension of
$\mathbb{Q}$. Git lots of details.


























