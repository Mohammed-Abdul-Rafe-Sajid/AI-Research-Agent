"""Evaluation metrics utilities."""
from typing import List


def precision(relevant: List[int], retrieved: List[int]) -> float:
    """Dummy precision computation where lists contain ids."""
    if not retrieved:
        return 0.0
    return len(set(relevant) & set(retrieved)) / len(retrieved)
