# -*- coding: utf-8 -*-
# @Data : 2024-03-02

import math


class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x + self.y)

    def __bool__(self):
        return bool(abs(self))
    



    
        