#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import openai
import requests
from PIL import Image
from io import BytesIO


class OpenAI:
    def __init__(self, logger, org, token, model):
        self.logger = logger
        self.logger.info("Initializing OpenAI API...")
        self.openai = openai
        self.openai.organization = org
        self.openai.api_key = token
        self.model_engine = ""
        self.models = self.openai.Model.list()
        for i in self.models.data:
            if i.id == model:
                self.logger.info("Found model %s" % model)
                self.model_engine = model
        if self.model_engine == "":
            self.logger.error("Model %s not found, exiting..." % model)
            os._exit(1)

    def ask_ia(self, message):
        completion = self.openai.ChatCompletion.create(model=self.model_engine, messages=[{"role": "user", "content": message}])
        return completion.choices[0].message.content

    def generate_image(self, message):
        response = requests.get(self.openai.Image.create(prompt=message, n=1, size="256x256")["data"][0]["url"])
        return Image.open(BytesIO(response.content))
