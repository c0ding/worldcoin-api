#!/usr/bin/env python
# -*- coding: utf-8 -*-

#                        __    __           _     
#   _      ______  _____/ /___/ /________  (_)___ 
#  | | /| / / __ \/ ___/ / __  / ___/ __ \/ / __ \
#  | |/ |/ / /_/ / /  / / /_/ / /__/ /_/ / / / / /
#  |__/|__/\____/_/  /_/\__,_/\___/\____/_/_/ /_/


__title__   = 'worldcoin'
__version__ = '0.1'
__author__  = "@c0ding"
__license__ = "Apache v2.0 License"

from . import utils
from .api import (
    get_difficulty, get_block_count, get_total_wdc
)