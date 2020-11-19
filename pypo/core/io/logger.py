import logging

class Logger(object):

    def __init__(self):
        self._debug = False

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, state):
        self._debug = state