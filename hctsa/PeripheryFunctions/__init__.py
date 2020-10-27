"""
# coding=utf-8
# MIT License
#
# Copyright (c) 2020 ClarkLabUVA
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

Highly Comparative Time-Series Analysis ("hctsa") defines a collection of functions/tools that can be used to analyze
time-series data.
"""

from hctsa.PeripheryFunctions.BF_Binarize import BF_Binarize
from hctsa.PeripheryFunctions.BF_buffer import BF_buffer
from hctsa.PeripheryFunctions.BF_embed import BF_embed
from hctsa.PeripheryFunctions.BF_iszscored import BF_iszscored
from hctsa.PeripheryFunctions.BF_makeBuffer import BF_makeBuffer
from hctsa.PeripheryFunctions.BF_ResetSeed import BF_ResetSeed
from hctsa.PeripheryFunctions.BF_sgnchange import BF_sgnchange
from hctsa.PeripheryFunctions.RM_histogram2 import RM_histogram2
from hctsa.PeripheryFunctions.RM_information import RM_information
from hctsa.PeripheryFunctions.SB_CoarseGrain import SB_CoarseGrain
from hctsa.PeripheryFunctions.wentropy import wentropy
from hctsa.PeripheryFunctions.ZG_hmm import ZG_hmm
from hctsa.PeripheryFunctions.ZG_hmm_cl import ZG_hmm_cl
from hctsa.PeripheryFunctions.ZG_rdiv import ZG_rdiv
from hctsa.PeripheryFunctions.ZG_rprod import ZG_rprod
from hctsa.PeripheryFunctions.ZG_rsum import ZG_rsum
