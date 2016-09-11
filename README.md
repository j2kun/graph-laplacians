# What's up with Graph Laplacians?

Code and data used in the guest post "What's up with Graph Laplacians?" on
Samantha Davies's blog [With High Probability](https://samidavies.wordpress.com).

## Requirements

Python 3, numpy, and matplotlib

If you have `git` and `python3` installed, this will download the code and install the remaining dependencies.

```
git clone https://github.com/j2kun/graph-laplacians
cd graph-laplacians
pip3 install -r requirements.txt
```

## Running

Run `python3 laplacian.py` to recreate the first sparsest-cut example.

Run `python3 second_eigenvalue_plot.py` to recreate the plot of the second eigenvalue.

Run `python3 sparsest_cut_test.py` to recreate the plot of the sparsest-cut accuracy test.
