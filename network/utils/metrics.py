from dataclasses import dataclass
from typing import Optional

@dataclass
class EpochMetrics:
    loss: float
    accuracy: Optional[float] = None
    ciou: Optional[float] = None
