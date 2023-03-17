#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


class Arguments(argparse.ArgumentParser):
    def __init__(self, environment):
        self.parser = argparse.ArgumentParser(description="OpenAI Telegram Bot")
        self.parser.add_argument('--bot-token', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_TELEGRAM_TOKEN",
                                 help="Telegram Bot Token. Talk to @botfarther to get it")
        self.parser.add_argument('--allowed-users', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_TELEGRAM_USERNAMES",
                                 help="List of telegram userids (not usernames) authorized to talk to the bot")

        self.parser.add_argument('--log-level', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_LOG_LEVEL", default='INFO')
        self.parser.add_argument('--log-file', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_LOG_FILE", required=False)

        self.parser.add_argument('--openai-org', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_OPENAI_ORG")
        self.parser.add_argument('--openai-token', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_OPENAI_TOKEN")
        self.parser.add_argument('--openai-model', action=EnvDefault, env=environment, envvar="ESTEFANIA_BOT_OPENAI_MODEL")

        self.parameters = vars(self.parser.parse_args())

    def __getitem__(self, item):
        return self.parameters[item]


class EnvDefault(argparse.Action):
    def __init__(self, env, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in env:
                default = env[envvar]
        if required and default:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
