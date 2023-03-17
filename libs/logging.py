#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging


class Logging(logging.getLoggerClass()):
    def __init__(self, loglevel, file):
        self.logger = logging.getLogger()
        self.name = "LOG"
        self.disabled = False
        self.propagate = False
        self._cache = {}
        self.filters = []
        self.handlers = []
        self.setLevel(loglevel.upper())
        self.log_format = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        consolelog = logging.StreamHandler()
        consolelog.setFormatter(self.log_format)
        self.addHandler(consolelog)
        self.logger.info('Logging to console')
        if file is not None:
            self.logger.info('Logging to file: %s' % file)
            try:
                os.makedirs(os.path.dirname(file), exist_ok=True)
            except OSError as e:
                logging.error(e)
                os._exit(1)
            self.logfile = logging.FileHandler(file)
            self.logfile.setFormatter(self.log_format)
            self.addHandler(self.logfile)
