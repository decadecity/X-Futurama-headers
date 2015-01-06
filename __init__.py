# -*- coding: utf-8 -*-
from . import futurama

"""Django middleware to add the quote."""

class AddQuote():

    def process_response(self, request, response):
        quote = futurama.get_header()
        response[quote[0]] = quote[1]
        return response
