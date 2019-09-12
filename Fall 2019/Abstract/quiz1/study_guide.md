---
title: Quiz Study Guide
author: [Arden Rasmussen]
date: "2019-09-11"
fontsize: 10pt
...

# Terminology

1. State the commutative and the associative rules for an operation. State the
   distributive rule.
  Commutative Rule ($\bigstar$):
  $$a\bigstar b=b\bigstar a$$
  Associative Rule ($\bigstar$):
  $$( a \bigstar b)\bigstar c) = a\bigstar(b\bigstar c)$$
  Distributive Rule ($\bigstar$, $\circ$):
  \begin{align*}
    (a\bigstar b)\circ c&= (a\circ c)\bigstar(b \circ c)\\
    a\circ(b\bigstar c)&=(a\circ b)\bigstar(a\circ c)
  \end{align*}

2. What do we mean when we say that...

  a. Something is an "identity" with respect to an operation? E.g. what do we mean by an "additive identity"? Or by a "multiplicative identity"?

Something is an identity if $a\bigstar \text{Id}=a$, and $\text{Id}\bigstar
a=a$. That operation applied to the identity and any other value is equal to
that other value.

### An element is "invertible with respect to an operation"? What do we mean by a "multiplicative inverse"?

An element is invertible with respect to an operation if there exists an
"identity" for that operation, and there exists a value such that
$a\bigstar a^{-1}=\text{Id}$, and $a^{-1}\bigstar a=\text{Id}$.

### $(G,\bigstar)$ constitutes a group?

* $\bigstar$ is Associative, and has Id.
* Every element of $G$ has an inverse with respect to $\bigstar$.
* May or may not be commutative.

### $(R,\oplus,\otimes)$ constitures a ring? A commutative ring? How about a field?

* $(R,\oplus)$ is a commutative group.
* $\otimes$ is associative.
* $\otimes$ distributes over $\oplus$.
* $\otimes$ may or may not be commutative.
* $\otimes$ may or may not have identity.
* Elements of $R$ may or may not have an inverse.

### an element is a "unit" in a ring?

### an element is a "zero divisor" in a ring?

### something is an "integral domain"?

# Examples

## Consider a collection $\mathcal{F}$ of functions $f:\mathbb{R}\rightarrow\mathbb{R}$. Composition of functions is an operation in the set $\mathcal{F}$.
$$
f,g\in\mathcal{F}\rightarrow f\circ g\in\mathcal{F}.$$

### Which rules does this operation satisfy?

### Does it have an identity?

### Does every element of $\mathcal{F}$ have its inverse?

### Does $\mathcal{F}$ constitute a group? A ring? A field?

## Let $M_n(\mathbb{R})$ be the set of $n\times n$ matricies whose entries are real numbers.

### Which rules do matric addition and multiplication satisfy?

### Does matric addition have an identity? if so, what is it? Likewise is there a multiplicative identity? If so, what is it?

### Does every matrix in $M_n(\mathbb{R})$ have its additive inverse? For matricies with additive inverse exaplain how one would go about finding the supposed inverse. How about multiplicative inverse? Explain how one would go about finding it.

