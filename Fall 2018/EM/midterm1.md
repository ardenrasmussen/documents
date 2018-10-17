---
title: E&M Midterm 1
author: Arden Rasmussen
---

# Electric Field #

Gauss's Law:
: $\oint\vec{E} \cdot d\vec{a}=\frac{Q_{enc}}{\epsilon_0}$

Point Charge:
: $\vec{E}=\frac{Q}{4\pi \epsilon_0 r^2}\hat{r}$

# Work #
$$
W=\int_{\vec{r}}^{\infty}Q\vec{E}\left(\vec{r'}\right)\vec{dl}
$$

# Potential #
$$
V=-\int_{\infty}^{\vec{r}}\vec{E}\left(\vec{r'}\right)\cdot\vec{dl}
$$

Point Charge:
: $V=\frac{1}{4\pi\epsilon_0}\frac{q}{r}$

Charge Distribution:
: $V=\frac{1}{4\pi\epsilon_0}\int_{\Omega}\frac{\rho\left(\vec{r'}\right)}{\mathcal{R}}d\tau'$

Potential Difference:
: $V(\vec{b}) - V(\vec{a}) = -\int_{\vec{a}}^{\vec{b}}\vec{E}\left(\vec{r'}\right)\vec{dl}$

$$
\vec{E} = \nabla V
$$

# Conductors #

A conductor is a material with an "infinite" number of free charges that can
move freely without resistance.

(#) Electric field inside a conductor is zero. $\vec{E}=0$
(#) $\rho=0$ everywhere inside the conductor.
(#) Any excess charge must be on surface of conductor.
(#) The entire conductor has the same potential.
(#) Electric fields from excess charges are always perpendicular to the
surface.

Laplace's Equation:
: $\vec{\nabla}^2V\equiv 0$

The potential in a space $\Omega$ is uniquely determined if:

(#) The charge density of $\rho\left(\vec{r}\right)$ is specified.
(#) The value of $V$ is specified on the boundaries.

# Differential Equations #

$$
\frac{\partial^2\mathbf{X}}{\partial x^2}=k^2\mathbf{X} \implies \mathbf{X} =
Ae^{kx}+Be^{-kx}
$$
$$
\frac{\partial^2\mathbf{X}}{\partial x^2}=-k^2\mathbf{X} \implies \mathbf{X} =
Asin(kx)+Bcos(ky)
$$

Apply all boundary conditions, then solve for coefficients through dot product.

