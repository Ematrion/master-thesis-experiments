

<p align="center">
  <strong>Evaluation of Ranking & Matchmaking in Competiton</strong>
  <br>A Simulation and Humanist Approach<br>
  <em>Master Thesis</em>
  <br>David Bucher<br>
  January 2025<br>
  University of Fribourg
</p>

[![DOI](https://zenodo.org/badge/17680159.svg)](https://doi.org/10.5281/zenodo.17680159)


## Content Summary

The repository focuses on *Chapter 4* - the experimental part of the thesis.  

Each notebook is a standalone experiment. All start with a number matching the section of the writen document. They contain the code and comments from the thesis. It is recommanded to consult them in order. 

- **4.1 Baseline**: I claim we can use kendall tau rank correlation to track Elo convergence. This notebook present values to expect in settings relevant to the thesis.
- **4.2 Elo Prediction**: I claim that a perfectly tuned ranking - from a *predictive* metric perspective - can overfit data even with proper training/validation. I build a synthetic illustrating it.
- **4.3 The Snake Scheduler**: I propose a simple model for skilled based matchmaking. I run a simulation where I measure *game quality* computed by Elo, Glicko, TrueSkill and OpenSkill.
- **4.4 Random Snake**: is a conceptual benchmark test highighting qualitative difference between SOTA rankings. (I am very proud of this setting).
- **4.5 Convergence in the snake format**: is an extention of 4.4 showing how the conceptual test translate to a more realistic scenario.


## Addendum

- *3.4.2 Access The pakcage is available upon request from the author.*
This is no longer relevant. The [RSTT](https://github.com/Ematrion/rstt) package is now publicly available with *pip install rstt*. User and API [documentation](https://rstt.readthedocs.io/en/latest/) are available. Currently the package is under review by the [python open science](https://github.com/pyOpenSci/software-submission/issues/258) initiative.



