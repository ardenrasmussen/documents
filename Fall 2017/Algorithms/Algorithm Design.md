Algorithm Design
================

# Contents #

<!-- vim-markdown-toc GFM -->

* [Chapter 1](#chapter-1)
  * [A First Problem: Stable Matching](#a-first-problem-stable-matching)
    * [The Question](#the-question)
      * [Formulating the Problem](#formulating-the-problem)

<!-- vim-markdown-toc -->

# Chapter 1 #

## A First Problem: Stable Matching ##

### The Question ###

The Stable Matching Problem originated in 1962 from Davis Gale and Lloyd
Shapley. Gale and Shapley asked: Given a set of preferences among employers and
applicants, can we assign applicants to employers so that for every employer
$E$, and every applicant $A$ who is not scheduled to work for $E$, at least one
of the following two things in the case?

1. $E$ prefers everyone of its accepted applicants to $A$; or
2. $A$ prefers her current situation over working for employer $E$.

If this hold, the outcome is stable: individual self-interest will prevent any
applicant/employer deal from being made behind the scenes.

#### Formulating the Problem ####

A "bare-bones" version of the problem can be useful for a basic solution: each
of $n$ applicants applies to each of $n$ companies, and each company wants to
accept a *single* applicant. This preserves the fundamental issues of the
original problem.

Gale and Shapley, observed that this problem can be viewed as devising a
system that $n$ men and $n$ women can end up getting married, and everyone is
seeking to be paired with exactly one individual of the opposite gender.

So consider a set $M=\{m_1,\ldots,m_n\}$ of $n$ men, and a set
$W=\{w_1,\ldots,w_n\}$ of $N$ women. Let $M\timesW$ denote the set of all
possible ordered pairs of the form $(m,w)$, where $m \in M$ and $w \in W$. a
*matching* $S$ is a *set* of ordered pairs, each of $M\timeW$, with the
property that each member of $M$ and each member of $W$ appears in at most one
pair in $S$. A *perfect matching* $S'$ is a matching with the property that
each member of $M$ and each member of $W$ appears in *exactly* one pair in
$S'$.
