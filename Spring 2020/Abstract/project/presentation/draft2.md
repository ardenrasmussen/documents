---
marp: true
theme: uncover
paginate: true
---

<!--_class: invert-->

# **The Solvability of The Word Problem for Automatic Groups**

_Arden Rasmussen_

<!--Hello everyone, I'm Arden Rasmussen, and I am going to talking about the
solvability of the word problem for automatic groups.-->

---

## Outline

<!--First a brief outline. First I am going to explain what the word problem
is, and why it is important. Then I will go though the Knuth-Bendix method,
following that I will explain finite state automata. Then
we will put everything together, and use finite state automata along with the
Knuth-Bendix method to show the solvability of the word problem for automatic
groups. I do want to note that I will not actually be going through the proof,
but just the key points and details of what the proof does.-->

---

<!--_class: invert-->

## **The Word Problem**

<!--First lets start with the word problem.-->

---

### Some definitions

<!--Unfortunately before I can get into the meat of the word problem, it is
important to setup some definitions and notations that will commonly be used.-->

---

#### Alphabet

For a set of generators $X=\left\{x,y,z\right\}$, we create a set of _letters_ called the alphabet $\Sigma=\left\{a,b,c,d,e,f\right\}$, where

$$
\begin{aligned}
a&=x\quad b=x^{-1}\\
c&=y\quad d=y^{-1}\\
e&=z\quad f=z^{-1}\\
\end{aligned}
$$

<!--First we define the alphabet. The alphabet is simply a set of letters. In the context of groups, it can be though of as the set of generators union the set of inverses of the generators. So there should be twice as many letters as there are generators.-->

---

#### Language

Since any element of a group can be constructed as some combination of the groups generators, then we can equivalently express any element of the group as some _word_, or a product of letters in $\Sigma$. All words are denoted by $\Sigma^*=\left\{\varepsilon,a,b,\ldots,f,aa,ab,\ldots\right\}$.

<!--Since we can construct any element of a group through some combination of the generators of that group, then we can express this combination of generators as the product of letters. This is because the generators directly map to the letters, so a product of generators would be identical to the product of letters. The product of letters will be called a word. All possible words, including the word which is a product of no letters, construct the language, which is denoted by sigma start. The word with no letters is denoted by epsilon.-->

---

#### Shortlex Ordering

Given the language $\Sigma^*=\left\{\varepsilon, a, b, \ldots\right\}$, shortlex ordering defines

$$
\varepsilon < a < b < \ldots < f < aa < ab < \ldots < ff< aaa < \ldots
$$

<!--Shortlex ordering is a method to apply ordering to languages. It is similar to what we use for dictionaries. Shortlex ordering orders shorter words preceding longer words, and for words of the same length it uses lexicographical order, which is just alphabetical ordering. So for our made up language, the ordering would be, epsilon, a, b, c, d, e, f, followed by aa, ab, ac, you get the idea. Note that this will be different from the ordering of the group, as there is no relation to which generators are greater than one another. All that matters is the order which the generators are defined. This means that changing the order which the generators are defined will indeed change the ordering, but this is the same as with english. If you would define the letter $z$ as the first letter, then this changes alphabetical ordering. The use of ordering for the language will become useful in the Knuth-Bendix method, which relies on some ordering of the language.-->

---

#### Normal Form

<!--The last thing that we need to define, is the normal form. The normal form is a subset of the language, where frequently the normal form of an element is a word which cannot be rewritten any further, I will explain what I mean by "rewritten" later, bur for now, we can think of the normal form as the set of words that we will use as the representatives for each element of the group.-->

---

#### Example

$$
\mathbb{Z}_3=\left\langle x \vert x^3=1\right\rangle
$$

<!--Lets go though these definitions with a more concrete example. Lets consider the cyclic group of order 3. Z_3 is given by the generators x, and the relation x cubed equals 1.-->

---

#### Example

$$
\begin{aligned}
\mathbb{Z}_3&=\left\langle x \vert x^3=1\right\rangle\\
\Sigma&=\left\{x,x^{-1}\right\}
\end{aligned}
$$

<!--From here we construct our alphabet, which in this case consists of two elements, one representing x and one x inverse. Although we could define these are arbitrary letters, I find it most useful to just use x and x inverse to denote their corresponding letters.-->

---

#### Example

$$
\begin{aligned}
\mathbb{Z}_3&=\left\langle x \vert x^3=1\right\rangle\\
\Sigma&=\left\{x,x^{-1}\right\}\\
\Sigma^*&=\left\{\varepsilon, x, x^{-1}, xx, xx^{-1},x^{-1}x,\ldots\right\}
\end{aligned}
$$

<!--Now we construct the language from the alphabet, and again this is just all possible combinations of the letters. Note that every element of Z3 is represented in this set, and as a matter of fact it is represented many many times.-->

---

#### Example

$$
\begin{aligned}
\mathbb{Z}_3&=\left\langle x \vert x^3=1\right\rangle\\
\Sigma&=\left\{x,x^{-1}\right\}\\
\Sigma^*&=\left\{\varepsilon, x, x^{-1}, xx, xx^{-1},x^{-1}x,\ldots\right\}\\
\varepsilon &< x < x^{-1} < xx < xx^{-1} < x^{-1}x < \ldots
\end{aligned}
$$

<!--The next step is to use shortlex ordering to define our method for ordering the words in the language. Note that the actual value of x inverse may be less than the value of x in the group, but this is not an ordering of elements of the group, but an ordering of string representing products of elements of the group, be sure to keep that in mind-->

---

#### Example

$$
\begin{aligned}
\mathbb{Z}_3&=\left\langle x \vert x^3=1\right\rangle\\
\Sigma&=\left\{x,x^{-1}\right\}\\
\Sigma^*&=\left\{\varepsilon, x, x^{-1}, xx, xx^{-1},x^{-1}x,\ldots\right\}\\
\varepsilon &< x < x^{-1} < xx < xx^{-1} < x^{-1}x < \ldots\\
&\quad\left\{1, x, xx\right\}
\end{aligned}
$$

<!--Unfortunately, the final step must go unexplained for now, but we can define the normal form for the elements in the group. In this example we commonly define them to be 1, x and x squared. These normal forms of the elements will be important for the knuth-bendix method.-->

---

#### Questions?

---

### Motivation

$$
\Sigma^*=\left\{\varepsilon, x, x^{-1}, xx, xx^{-1},x^{-1}x,\ldots\right\}\\
$$

<!--In our example, we noticed that all three elements of Z3 appear many many times in the language, there are an infinite number of words which represent each of the three elements. Wouldn't it be nice if we had some way of knowing what words represent which elements of the group? Well thats exactly what the word problem is. Which of these words represents the identity, which of them represent just x?-->

---

### The Word Problem

> The word problem for a finitely generated group $G$ is the algorithmic problem of deciding whether two words in the generators represent the same element.

<!--More formally the word problem is the algorithmic problem of determining whether two words represent the same element. This is actually a pretty big question. If I gave you two words for some group, you could probably workout if they represent the same element, but can it be done generally, for any two words of the group. Or can it be done for all groups? Well, it has been shown that generally the word problem is not solvable for all groups. However, there are some groups which have a solvable word problem, one of which is the automatic groups.-->
<!--Automatic groups are groups which can have an automaton applied to them, which I will explain later, but for know it is nice to know that all finite groups, hyperbolic groups, euclidean groups, braid groups, and several other groups are all automatic groups. So showing the word problem is solvable for automatic groups gives a lot of power.-->
<!--Also note that the word problem is solvable for other groups, but we will be focusing on automatic groups.-->

---

<!--_class: invert-->

## **Knuth-Bendix**

<!--Now that we have an understanding of what the word problem is, we can begin with the knuth-bendix method.-->

---

### Setup

$$
\begin{aligned}
G&=\left\langle X \vert R\right\rangle\\
R&=\left\{P_i=Q_i\vert P_i,Q_i\in\Sigma^*\right\}
\end{aligned}
$$

<!--For the knuth-bendix method, we will define our group G, to be presented by the generators and relations X and R respectively. I want to note that the set of relations R is a set of equations, which we will denote as P=Q. In our previous example of Z3, we would only have one relation, and that would be with P_1 equals x cubed, and Q_1 equals 1.-->

---

### Rewriting System

Given some $P_i=Q_i\in R$, with $Q_i < P_i$, then define the relation

$$
(i)\quad P_i\rightarrow Q_i.
$$

<!--The next step is to construct our rewriting system. The rewriting system consists of a number of rules, such that when the left hand side of a rules appears in a word, then it can be replaced by the right hand side of the rule. I want to note, that the reverse is not true. The right hand side of the rule cannot be replaced by the left hand side. Without loss of generality we can assume that Q_i<P_i, then we define the ith relation to be P_i to Q_i. Now that we have the structure of a rewriting system, the normal form makes sense. The normal form is the word which no P_i appears in it, so it cannot be rewritten any future. However, this could result in some issues, as what if multiple elements in the normal form are equal.-->

---

### Confluence

The order of applying rules of the rewriting system should not change the result.

<!--This is where confluence comes into play. Confluence is the concept, that the order in which the rules of the rewriting system are applied to a word, should not change the result.-->

---

#### Inequality of Normal Forms

Consider normal forms $a$ and $b$, with $a\neq b$, and both equal $c$. Then construct some word $w$, such that

$$
w\xrightarrow{(a_1),\ldots,(a_k)}b\quad

w\xrightarrow{(b_1),\ldots,(b_k)}a
$$

where $a_1,\ldots,a_k$ and $b_1,\ldots,b_k$ are sequences of relations. Then to preserve confluence, $b=a$.

<!--So if we had two normal form words a and b that represent the same element c, then the two must be equal to preserve confluence. This is because we could construct a word w, such that one order of rewriting rules a's will give the normal form a, and a different order of rules b's will result in the second normal form b. And thus confluence would be broken. So we can conclude that if confluence is to be preserved, then a must be equal to b. And further, that all elements of the set of normal forms must not be equal to one another.-->

---

### Knuth-Bendix Method

Constructs a rewriting system for which confluence is conserved, and thus any word can be rewritten in a normal form, and then the equality of normal forms is trivial.

<!--The knuth bendix method is a method to construct a rewriting system for which confluence is conserved. With such a rewriting system, any word can be rewritten into its representative normal form, and then the equality of two normal forms is trivial to check.-->

---

### The Algorithm

Consider $P_i$, $P_j$ with $i\neq j$, where $P_i$ and $P_j$ have some overlap.

1. The prefix of $P_i$ is equal to the suffix of $P_j$. Consider $P_i=BC$ and
   $P_j=AB$.
2. $P_i$ is contained within $P_j$. Let $P_i=B$ and $P_j=ABC$.

<!--After constructing the initial rewriting system, which may not preserve confluence. We must begin to construct new rules to add to the rewriting system in order to preserve confluence.-->
<!--Let us consider the left hand side of two rules for the writing system, which are not the same rule, and they have some overlap. Luckily there are only two cases where overlap occurs. First when the prefix of P_i is equal to the suffix of P_j. consider P_i=BC, and P_j=AB. then the overlap is in the B term. The second case is when P_i is contained within P_j. Let P_i=B, and P_j=ABC. Again the overlap is in the B term.-->

---

Consider the word $ABC$, and apply $P_i$ and $P_j$ to get the words $r_i$ and $r_j$ respectively. If $r_i\neq r_j$, then define the new rule

$$
\max\{r_i,r_j\}\rightarrow\{r_i,r_j\}
$$

<!--Now to we consider the word ABC, ane apply P_i and P_j to get the words r_i and r_j respectively. If r_i and r_j are not equal, then this is a lack of confluence, and to resolve it we define the new rule given by the maximum of the two results mapping to the minimum of the two results. And the maximum and minimum is defined by shortlex ordering. Now that this new rule exists, remove any existing rule, which can be reduced by this new rule.-->
<!--Finally just repeated this process until no more rules can be reduced. Then this rewriting system preserves confluence, and any word can be rewritten into their normal form by following this system.-->

---

#### Example

$$
G=\left\langle a,b\vert a^3=b^3={(ab)}^2=1\right\rangle=D(2,3,3)
$$

<!--Lets do an example of the knuth bendix method, to construct a rewriting system that preserves confluence. This is the generators and relations for our group, which is also known as the von Dyck group D(2,3,3).-->

---

#### Example

$$
G=\left\langle a,b\vert a^3=b^3={(ab)}^3=1\right\rangle=D(3,3,3)
$$

$$
\begin{aligned}
&(1)\quad x^3 &\rightarrow 1\\
&(2)\quad y^3 &\rightarrow 1\\
&(3)\quad xyxyxy &\rightarrow 1
\end{aligned}
$$

<!--The first step of the process is to construct the initial rewriting system, which may not preserve confluence. This is trivially done, and we find the rules of the rewriting system to be these.-->

---

$P_1$ and $P_3$ overlap, so consider $x^3yxyxy$, and we reduce it

$$
\begin{aligned}
x^3yxyxy\xrightarrow{1} yxyxy\quad x^3yxyxy\xrightarrow{3} x^2
\end{aligned}
$$

---

$P_1$ and $P_3$ overlap, so consider $x^3yxyxy$, and we reduce it

$$
\begin{aligned}
x^3yxyxy\xrightarrow{1} yxyxy\quad x^3yxyxy\xrightarrow{3} x^2
\end{aligned}
$$

Define $(4)\quad yxyxy\rightarrow x^2$.

---

$P_1$ and $P_3$ overlap, so consider $x^3yxyxy$, and we reduce it

$$
\begin{aligned}
x^3yxyxy\rightarrow yxyxy\quad x^3yxyxy\rightarrow x^2
\end{aligned}
$$

Define $(4)\quad yxyxy\rightarrow x^2$.
Remove $(3)\quad xyxyxy\rightarrow 1$.

---

Repeating this process the set of relations become

$$
\begin{aligned}
&(1)\quad x^3 &\rightarrow 1\\
&(2)\quad y^3 &\rightarrow 1\\
&(6)\quad yxyx &\rightarrow x^2y^2\\
&(7)\quad y^2x^2 &\rightarrow xyxy
\end{aligned}
$$
