---
title: E\&M Final
author: Arden Rasmussen
date: today
documentclass: amsart
---

# Electrodynamics #

## Electromotive Force ##

### Ohm's Law ###
Circuits work pretty predictably. But maybe check with someone else to see if I
know everything for this stuff.

### Electromotive Force ###
EMF is the "force" caused by the magnetic field caused by the current in the
wire.

### Motional EMF ###
**Motional emf** is generated when a wire is moved through some magnetic field.
From a different point of view this is the same of stationary emf.

Note that the magnetic field is constructing the emf, it is not doing work. The
EMF is the negative of the change of the flux of the magnetic field with
respect to time.

## Electromagnetic Induction ##

### Faraday's Law ###
A changing magnetic field induces an electric field. No matter how the flux
changes (through motion or changing current etc.) there will be an induced EMF.

### Inductance ###
The flux on loop 2 due to loop 1 is proportional to the current 1, thus we
define mutual inductance of the two loops, such that the flux in loop b is
equal to the mutual inductance times the current of loop a. And the mutual
inductance is irrelevant of the order of a and b. The mutual inductance is
only dependent on the shapes of the loops, not the currents.

A changing current produces emf on itself, and the flux of this self produced
emf is found by multiplying the inductance with the current.

Because the emf is negative, then the emf will fight against any change in
current, attempting to keep it constant.

### Energy in Magnetic Fields ###
There is some amount of work needed to be done in order to oppose the back emf.
We say this energy is stored in the magnetic field.

Constructing a magnetic field requires energy, because to get a magnetic field
where there was none, requires changing a magnetic field, which then induces
an electric field, which can do work.

## Maxwell's Equations ##

### Electrodynamics Before Maxwell ###

$$
\nabla\cdot E=\frac{1}{\epsilon_0}\rho
$$
$$
\nabla\cdot B=0
$$
$$
\nabla\times E=-\frac{\partial B}{\partial t}
$$
$$
\nabla\times B=\mu_0J
$$

But there is an issue with this. The example is a circuit with a capacitor.
Consider the Ampèrian loop with a surface that goes through the capacitor. Then
there is no current passing through the surface. But this will cause issues and
so must not be true. Thus our notion of "current enclosed by the loop" is
ill-defined

### How Maxwell Fixed Ampère's Law ###
Maxwell said to rewrite the final equation to be

$$
\nabla \times B=\mu_0J+\mu_0\epsilon_0\frac{\partial E}{\partial t}
$$
This resolves the issues that were being caused.

### Maxwell's Equations ###

$$
\nabla\cdot E=\frac{1}{\epsilon_0}\rho
$$
$$
\nabla\cdot B=0
$$
$$
\nabla\times E=-\frac{\partial B}{\partial t}
$$
$$
\nabla \times B=\mu_0J+\mu_0\epsilon_0\frac{\partial E}{\partial t}
$$

# Conservation Laws #

## Charge And Energy ##

### The Continuity Equation ###
Charge is conserved, and so
$$
\frac{\partial \rho}{\partial t}=-\nabla\cdot J
$$

### Poynting's Theorem ###
Since work is needed to construct static charge distrobutions, and work is
needed to get currents going, then there is an expression for the energy in the
electromagnetic fields per unit volume $u$.

The work done on the charges by the electromagnetic force is equal to the
decrease in energy remaining in the fields, less the energy the flowed out
through the surface.

The energy per unit time, per unit area transported by the fields is called the
poynting vector.

# Electromagnetic Waves #

## Waves In One Dimension ##

### The Wave Equation ###
You know waves, but the one important equation is
$$
\frac{\partial^2f}{\partial z^2}=\frac{1}{v^2}\frac{\partial^2f}{\partial t^2}
$$
Where $v$ is the speed of propagation. The sum of any two solutions is also a
solution.

### Sinusoidal Waves ###
The sinusoidal waveform is of the form
$$
A\cos[k(z-vt)+\delta]
$$
Any wave can be expressed as a combination of sinusoidal ones.

## Electromagnetic Waves in Vacuum ##

### The Wave Equation for E and B ###
In a vacuum Maxwell's equations can be simplified. Then they can be separated
to become
$$
\nabla^2E=\mu_0\epsilon_0\frac{\partial^2E}{\partial t^2},\quad
\nabla^2B=\mu_0\epsilon_0\frac{\partial^2B}{\partial t^2}.
$$
Thus each of these solve the tree dimensional wave equation
$$
\nabla^2f=\frac{1}{v^2}\frac{\partial^2f}{\partial t^2}
$$
Where the speed of propagation $v=c$! This is some cool stuff.

### Monochromatic Plane Waves ###
Electric and Magnetic waves are perpendicular to the direction of propagation,
and perpendicular to one another.

Take the direction of propagation to be in the $z$ direction, then the $B$
field could be only in the $y$ direction, and the $E$ field only in the $x$
direction.


