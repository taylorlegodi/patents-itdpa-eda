# Patents ITDPA: Exploratory Data Analysis

Exploratory data analysis of patent activity, scholarly publications and estimated investment across six countries: China, Germany, India, South Africa, Sweden and the United States.

## Overview

This project examines how innovation output and investment compare between large and small research economies. Part 1 focuses on cleaning the data and summarising each country's distribution with descriptive statistics (count, mean, median, standard deviation, min, max, quartiles and IQR).

## Key observations

- Estimated investment varies enormously between countries. The United States has a median above 100,000, while South Africa's median is around 150.
- India and Sweden show high standard deviations relative to their medians, which points to skewed distributions with a few very large values.
- Using the median and IQR alongside the mean gives a more reliable picture than the mean alone.

## Project structure

```
cat/                 Raw source files (companies, patents, publications)
clean/               Cleaned datasets produced by the notebook
EDA Part 1.ipynb     Main exploratory analysis notebook
main.py              Entry point
pyproject.toml       Project metadata and dependencies
uv.lock              Locked dependency versions
```

## Getting started

1. Clone the repository:

```
git clone https://github.com/taylorlegodi/patents-itdpa-eda.git
cd patents-itdpa-eda
```

2. Install dependencies with [uv](https://docs.astral.sh/uv/):

```
uv sync
```

3. Open `EDA Part 1.ipynb` in VS Code or Jupyter and run all cells.

## Tools

Python 3.14, pandas, Jupyter and uv.

## Data sources

Add the source of each dataset here, along with any licence or usage terms.

## Author

Lethabo Legodi
GitHub: [taylorlegodi](https://github.com/taylorlegodi)    
