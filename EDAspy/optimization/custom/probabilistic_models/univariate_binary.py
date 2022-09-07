#!/usr/bin/env python
# coding: utf-8

import numpy as np
from .probabilistic_model import ProbabilisticModel


class UniBin(ProbabilisticModel):

    def __init__(self, variables: list, upper_bound: float, lower_bound: float):
        super().__init__(variables)

        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

        self.pm = np.zeros((2, self.len_variables))

        self.id = 2

    def sample(self, size: int):
        dataset = np.random.random((size, self.len_variables))
        dataset = dataset < self.pm
        dataset = np.array(dataset, dtype=int)
        return dataset

    def learn(self, dataset: np.array):
        self.pm = sum(dataset) / len(dataset)
        self.pm[self.pm < self.lower_bound] = self.lower_bound
        self.pm[self.pm < self.upper_bound] = self.upper_bound

    def export_settings(self):
        return self.id, self.upper_bound, self.lower_bound

    @property
    def pm(self):
        return self._pm

    @pm.setter
    def pm(self, value: np.array):
        assert len(value) == 1, "The argument must be an array of 1 dimension and size the number of variables."
        self._pm = value
