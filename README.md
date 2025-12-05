<p align="center">
  <strong>Evaluation of Ranking & Matchmaking in Competition</strong>
  <br>A Simulation and Humanist Approach<br>
  <em>Master Thesis</em>
  <br>David Bucher<br>
  January 2025<br>
  University of Fribourg
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17680159.svg)](https://doi.org/10.5281/zenodo.17680159)


---

## Content Summary

The repository focuses on *Chapter 4* — the experimental part of the thesis.

Each notebook is a standalone experiment. All start with a number matching the section of the written document. They contain the code and comments from the thesis. It is recommended to consult them in order.

- **4.1 Baseline**: I claim we can use Kendall tau rank correlation to track Elo convergence. This notebook presents values to expect in settings relevant to the thesis.
- **4.2 Elo Prediction**: I claim that a perfectly tuned ranking — from a *predictive* metric perspective — can overfit data even with proper training/validation. I build a synthetic example illustrating it.
- **4.3 The Snake Scheduler**: I propose a simple model for skill-based matchmaking. I run a simulation where I measure *game quality* computed by Elo, Glicko, TrueSkill, and OpenSkill.
- **4.4 Random Snake**: a conceptual benchmark test highlighting qualitative differences between SOTA rankings. (I am very proud of this setting.)
- **4.5 Convergence in the Snake Format**: an extension of 4.4 showing how the conceptual test translates to a more realistic scenario.

#### Remark
Texts are close to the ones in the thesis PDF. They have been slightly adjusted to make the notebooks self-readable but may contain references to other chapters not available in this repo.

#### Extension
Some notebooks include a section **Further Notes**, which contains insight not presented in the thesis nor to the expert panel during Chapter 5. These are not necessary to follow the experimentation but bring valuable context and elements to anyone exploring my work.

---

## Research Background & Motivation

My thesis started as a personal exploratory project. I wanted to verify and disprove certain frequent claims in the gaming community. I coded a first simulation prototype, then became more passionate about the project and started to investigate ranking algorithms and evaluation methodologies from the perspective of my experience in high-level competition.
During the literature review, the experimental protocol and evaluation techniques of SOTA modern rating systems caught my attention.

- One fundamental property of the Elo rating is systematically neglected or overlooked. Elo does not simply converge; it does not have a function that predicts game outcomes accurately. **Elo is a Markov process with a unique stationary distribution** (steady state). We know exactly what Elo does, which is a tremendous asset for reinforcement learning and unsupervised learning.
- The data structure and the interplay between a ranking learning from games and producing recommendations for future games is not a detail and can alter competitive results. High-level chess consists of double round-robin or Swiss rounds, and as a graph, contains many cycles. Professional tennis consists of single-elimination brackets with no cycle at all. **A cross-validation methodology in which a dataset is split in time for training and test sets produces the same distribution of data points**. You need to split the *distribution* of points to claim it generalizes.
- Skill-based matchmaking creates a pleasant gaming experience but produces irrelevant data for learning. **There is no information in an a priori balanced game** — at least according to Shannon’s theory. The expected-score baseline on such a dataset is a random predictor, yet no paper compares their system to it.

I formulated the **“Matchmaking Domain Overfitting Hypothesis”** and opted for simulation-based research. The rationale for it:

- Only Elo has a proven unique stationary distribution.
- Alternative systems have more parameters (typically ratings with a mean and a variance).
- Empirical research did not address the underlying data structure nor address the naïve baseline.

---

## Contribution

- An illustration of an empirically perfectly tuned Elo rating system that does not generalize to the entire feature space.
- A model for skill-based matchmaking-like competition formats.
- A conceptual test highlighting differences in SOTA ranking behaviour.
- A setting in which TrueSkill and OpenSkill need more than 600 gamess to correctly sort 8 players, proving that players can have a poor ranking experience despite playing at their level.

---

## Installation

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

---

## Addendum

- *3.4.2 Access The pakcage is available upon request from the author.*
This is no longer relevant. The [RSTT](https://github.com/Ematrion/rstt) package is now publicly available with *pip install rstt*. User and API [documentation](https://rstt.readthedocs.io/en/latest/) are available. Currently the package is under review by the [python open science](https://github.com/pyOpenSci/software-submission/issues/258) initiative.



<!-- 


<p align="center">
  <strong>Evaluation of Ranking & Matchmaking in Competiton</strong>
  <br>A Simulation and Humanist Approach<br>
  <em>Master Thesis</em>
  <br>David Bucher<br>
  January 2025<br>
  University of Fribourg
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17680159.svg)](https://doi.org/10.5281/zenodo.17680159)


---

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

---


## Research Background & Motivation

My thesis started as a personal exploratory project. I wanted to verify and disprove certain frequent claims in the Gaming community. I coded a first simulation prototype. Then, got more passionate by this project and stated to investigate ranking algorithms and evaluation methodolgies from the perspective of my experience in high level competition.
During literature review, the experimental protocol and evaluation techniques of SOTA modern ratings system got my attention.

- One fundamental property of the Elo rating is systematicaly neglected or overlooked. Elo does not simply converge, it does not have a functionn that predict games outcomes accuretly. Elo is a markov process with a unique stationary distribution, steady state. We known exactly what Elo does, which is a tremendous asset for reinforcement learning and unsupervised learning.
- The data strucutre and the interplay between a ranking learning from games, and producing recommandation for future games to play, is not a detail and can alter competitve results. High level chess consist of double round robin or swissround, and as a graph, contains many cycle. Professional tennis consist of single elimination bracket with no cycle at all. A cross validation methodology where a dataset is split in time for training and test set produces the same distribution of data point. Youn need to split the distribution of point to claim it generalize. 
- Skillbased matchmaking is a plesant gaming experience, but produce irrelevant data for learning. There is no information from an apriori balanced game - at least acording to Shannon's theory. The expected score baseline on such a data set is a random predictor, yet no paper compare their system to it.

I formulate the **'Matchmaking domain Overfitting Hypothesis'** and opted for simulation based research. The rational for it:
- Only Elo has a proven unique stationary distribution.
- Alternative system have more parameteres (typically ratings with a mean and a variance)
- Empirical research did not address the data underying strucutre nor adressed the naive baseline. 

---

## Contribution

- An illustration of an empirical perfectly tuned Elo rating system that does not generalized to the entire feature space.
- A model for skilled base matchmaking like format of competition
- A conceptual test highlighting differences in SOTA ranking behaviour
- A Setting in which TrueSkill and Openskill need more than 600 player to sort correctly 8 players. Proving that player can have an horribleranking experience despite playing at their level. 


---

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

---

-->