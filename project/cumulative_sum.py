#!/usr/bin/env python
import numpy as np


def cumulative_sum(n):
    """Compute the cumulative sum from 1 to n."""
    return np.sum(np.arange(1, n+1))


def main():
    print(cumulative_sum(5))


if __name__ == '__main__':
    main()
