#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import threading
from libs.telegrambot import TelegramBot
from libs.arguments import Arguments
from libs.logging import Logging
from libs.openai import OpenAI

if __name__ == "__main__":
    parameters = Arguments(os.environ)
    logger = Logging(parameters['log_level'], parameters['log_file'])
    ia = OpenAI(logger, parameters['openai_org'], parameters['openai_token'], parameters['openai_model'])
    polling = threading.Thread(target=TelegramBot(logger, ia, parameters['allowed_users'], parameters['bot_token']))
    polling.daemon = True
    polling.start()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            break
