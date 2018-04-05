#!/usr/bin/python
# -*- coding: UTF-8 -*-
# some problems? remember to write a blog

from . import player
from . import window
class PlayGame():
    def __init__(self):
        self._pnum = 0
        self._players = dict()

    def play(self):
