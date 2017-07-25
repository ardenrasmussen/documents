==========================================================================
Mathematic Formulation of the Double-Precision Orbit Determination Program
==========================================================================

********
Abstract
********

This documents the complete mathematical model for the Double-Precision Orbit
Determination Program (DPODP), a third-generation program which has recently
been completed at the Jet Propulsion Laboratory. The DPODP processes
earth-based doppler, range, and angular observable of the spacecraft to
determine values of the parameters that specify the spacecraft trajectory for
lunar and planetary missions.

.. contents::

************
Introduction
************

The DPODP has more accurate mathematical models, significantly more numerical
precision, and more flexibility then the second-generations Single-Precision
Orbit Determination Program. The basic limitations on the accuracy of computed
observable are the inaccuracies in the troposphere and ionosphere
corrections. Before these corrections are added, the computed values of the
doppler observable have inaccuracies of :math:`10^{-5}m/s` and :math:`0.1m`,
respectively.
