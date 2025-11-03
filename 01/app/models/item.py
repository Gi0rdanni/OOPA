from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class Item:
    description: str
    quantity: int
    id: Optional[int] = None