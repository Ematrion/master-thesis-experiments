

<p align="center">
  <strong>Evaluation of Ranking & Matchmaking in Competiton</strong>
  <br>A Simulation and Humanist Approach<br>
  <em>Master Thesis</em>
  <br>David Bucher<br>
  January 2025<br>
  University of Fribourg
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17680159.svg)](https://doi.org/10.5281/zenodo.17680159)


## Installation (AI generated section)

This project is written in Python and uses uv for environment and dependency management.

1. Clone the repository
```
git clone https://github.com/Ematrion/master-thesis-experiments


cd master-thesis-experiments
```

2. Install uv (if you don't have it already)
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Or with wget
```
wget -qO- https://astral.sh/uv/install.sh | sh
```
On Windows use
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Create and sync the environment
uv will read both pyproject.toml and uv.lock to create a fully reproducible environment:
```
uv sync
```

4. Launch JupyterLab or Notebook
```
uv run jupyter lab
```
or
```
uv run jupyter notebook
```



## Content Summary

The repository focuses on *Chapter 4* - the experimental part of the thesis.  

Each notebook is a standalone experiment. All start with a number matching the section of the writen document. They contain the code and comments from the thesis. It is recommanded to consult them in order. 

- **4.1 Baseline**: I claim we can use kendall tau rank correlation to track Elo convergence. This notebook present values to expect in settings relevant to the thesis.
- **4.2 Elo Prediction**: I claim that a perfectly tuned ranking - from a *predictive* metric perspective - can overfit data even with proper training/validation. I build a synthetic illustrating it.
- **4.3 The Snake Scheduler**: I propose a simple model for skilled based matchmaking. I run a simulation where I measure *game quality* computed by Elo, Glicko, TrueSkill and OpenSkill.
- **4.4 Random Snake**: is a conceptual benchmark test highighting qualitative difference between SOTA rankings. (I am very proud of this setting).
- **4.5 Convergence in the snake format**: is an extention of 4.4 showing how the conceptual test translate to a more realistic scenario.


#### Remark
Texts are close to the one in the thesis pdf. It as been slighlty adjusted to make the notebook self readable but can contain references to others chapter not available in this repo. 

#### Extention
Some notebooks include a section **Further Notes** which contains insight not presented in the thesis nor the expert panel during chapter 5. These are not necessary to follow the experimentation but brings valuable context and elements to anyone exploring my work. 


## Addendum

- *3.4.2 Access The pakcage is available upon request from the author.*
This is no longer relevant. The [RSTT](https://github.com/Ematrion/rstt) package is now publicly available with *pip install rstt*. User and API [documentation](https://rstt.readthedocs.io/en/latest/) are available. Currently the package is under review by the [python open science](https://github.com/pyOpenSci/software-submission/issues/258) initiative.



