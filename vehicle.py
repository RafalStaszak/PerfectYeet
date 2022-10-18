import numpy as np
import torch


class Vehicle:
    def __init__(self, m, max_v, max_a, ):
        self.m = m
        self.max_v = max_v
        self.max_a = max_a
