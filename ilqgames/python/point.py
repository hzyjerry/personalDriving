"""
BSD 3-Clause License

Copyright (c) 2019, HJ Reachability Group
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Author(s): David Fridovich-Keil ( dfk@eecs.berkeley.edu )
"""
################################################################################
#
# Point class for 2D points.
#
################################################################################

import numpy as np
import torch

class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Point(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return Point(self.x * rhs, self.y * rhs)

    def __rmul__(self, lhs):
        return Point(self.x * lhs, self.y * lhs)

    def __imul__(self, rhs):
        self.x *= rhs
        self.y *= rhs
        return Point(self.x, self.y)

    def __truediv__(self, rhs):
        return Point(self.x / rhs, self.y / rhs)

    def __idiv__(self, rhs):
        self.x /= rhs
        self.y /= rhs
        return Point(self.x, self.y)

    def norm_squared(self):
        return self.x**2 + self.y**2

    def norm(self):
        if isinstance(self.x, torch.Tensor):
            return torch.sqrt(self.norm_squared())

        return np.sqrt(self.norm_squared())
