# HW.6

<!-- ## Problem 1 -->

<!-- > Is $f(x)=21x^3-3x^2+2x+8$ irreducible over $\mathbb{Q}$? -->

<!-- ## Problem 2 -->

<!-- > Is $f(x)=x^5+2x+4$ irreducible over $\mathbb{Q}$? -->

<!-- ## Problem 3 -->

<!-- > Let $K/F$ be a field extension. Prove that $[K:F]=1\begin{align*} if and only if $K=F$. -->

## Problem 4

> Suppose $F$ is a field, and $R$ is an integral domain that contains $F$ as a
> subring. If $R$, considered as a vector space over $F$, is finite dimensional
> then show $R$ is a field.

Considering $R$ as a finite dimensional vector space over $F$, with dimension
$n$, then we known $R$ is spanned by a set of linearly independent basis
vectors, which we will denote $\{v_1,\ldots,v_n\}$. Now we define a mapping
$f:V\mapsto F^n$. defined as
\begin{align*}
f(v_i)=(\overbrace{0, \ldots, 0}^{i-1},1,\overbrace{0,\ldots,0}^{n-i-2})
\end{align*}
Now we demonstrate that $f$ is an isomorphism between these two vector spaces.

First consider $a,b\in R$, we can write these as
\begin{align*}
a=a_0v_0+\ldots+a_nv_n\\
b=b_0v_0+\ldots+b_nv_n
\end{align*}
Let us compute $f(a+b)$
\begin{align*}
f(a+b)&=f(a_0v_0+\ldots+a_nv_n+b_0v_0+\ldots+b_nv_n)\\
&=f((a_0+b_0)v_0+\ldots+(a_n+b_n)v_n)\\
&=(a_0+b_0)f(v_0)+\ldots+(a_n+b_n)f(v_n)\\
&=a_0f(v_0)+\ldots+a_nf(v_n)+b_0f(v_0)+\ldots+b_nf(v_n)\\
&=f(a)+f(b)
\end{align*}
Thus $f$ is a homomorphism.

Consider some element $a\in F^n$, we can write this as $a=(a_0,a_1,\ldots,a_n)$,
and thus this is equivalent to $a_0e_0+a_1e_1+\ldots+a_ne_n$, and now we can
take $a_0v_0+\ldots+a_nv_n\in R$, then
\begin{align*}
f(a_0v_0+\ldots+a_nv_n) &= a_0f(v_0)+\ldots+a_nf(v_n)\\
&=a_0e_0+\ldots+a_ne_n=a
\end{align*}
Thus $f$ is injective.

Consider some $a,b\in R$ such that $f(a)=f(b)$. This means that
\begin{align*}
f(a_0v_0+\ldots+a_nv_n)&=f(b_0v_0+\ldots+b_nv_n)\\
a_0f(v_0)+\ldots+a_nf(v_n)&=b_0f(v_n)+\ldots+b_nf(v_n)\\
\end{align*}
Thus we can conclude that $a_i=b_i$ for $i=1,\ldots,n$, and so $a=b$, and thus
$f$ is surjective.

Thus $f$ is an isomorphism between $R$ and $F^n$, so $R$ and $F^n$ are isomorphic.
We have previously shown that $F^n$ is a field, and so since $R$ is isomorphic
to $F^n$ then we conclude that $R$ must also be a field.

## Problem 5

> Let $\theta$ be a complex root of the irreducible polynomial
> $x^3-3x+4\in\mathbb{Q}[x]$. Find the inverse of $\theta^2+\theta+1$ in
> $\mathbb{Q}(\theta)$ explicitly in the form $a+b\theta+c\theta^2$ with
> $a,b,c\in\mathbb{Q}$.

First we compute
\begin{align*}
(\theta^2+\theta+1)(c\theta^2+b\theta+a)&=1\\
(a-4c-4b)+(4b+a-c)\theta+(4c+b+a)\theta^2&=1
\end{align*}
Then we can construct a system of linear equations
\begin{align*}
4c+b+a&=0\\
4b+a-c&=0\\
a-4c-4b&=1
\end{align*}
We then solve this system for $c$ to find $c=-\frac{3}{49}$, $b=-\frac{5}{49}$,
and $a=\frac{17}{49}$. So we conclude that the inverse if given by
\begin{align*}
\frac{17}{49}-\frac{5}{49}\theta-\frac{3}{49}\theta^2
\end{align*}
