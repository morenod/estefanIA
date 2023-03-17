#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot


class TelegramBot:
    def __init__(self, logger, ia, usernames, token):
        self.logger = logger
        self.ia = ia
        self.usernames = usernames
        self.logger.info("Initializing Telegram Bot...")
        self.bot = telebot.TeleBot(token)

        @self.bot.message_handler(commands=['help'])
        def _send_welcome(message):
            if self._is_authorized(message):
                welcome_message = '''
  /estefania    Ask something to EstefanIA
  /photofania   Ask EstefanIA to generate a picture about any topic
  /help         This help
  '''
                self.bot.reply_to(message, welcome_message)

        @self.bot.message_handler(commands=['estefania'])
        def _send_info(message):
            if self._is_authorized(message):
                ask = message.text.replace('/estefania', '')
                if ask == "":
                    self.bot.reply_to(message, "/estefania requires content")
                elif len(ask) > 200:
                    self.bot.reply_to(message, "Ask is too long")
                else:
                    answer = self.ia.ask_ia(ask)
                    self.bot.reply_to(message, answer)

        @self.bot.message_handler(commands=['photofania'])
        def _send_photo(message):
            if self._is_authorized(message):
                ask = message.text.replace('/photofania', '')
                if ask == "":
                    self.bot.reply_to(message, "/photofania requires content")
                elif len(ask) > 200:
                    self.bot.reply_to(message, "Ask is too long")
                else:
                    image = self.ia.generate_image(ask)
                    self.bot.send_photo(message.chat.id, image)

        self.logger.info("Starting polling messages...")
        self.bot.polling()

    def _is_authorized(self, message):
        if str(message.from_user.id) not in self.usernames:
            self.bot.reply_to(message, "You are not authorized to talk to Estefania, reporting")
            return False
        else:
            return True
