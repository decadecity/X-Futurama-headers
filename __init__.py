# -*- coding: utf-8 -*-
import futurama
import logging


class AddQuote():

    def process_response(self, request, response):
        quote = futurama.get_header()
        response[quote[0]] = quote[1]
        return response
