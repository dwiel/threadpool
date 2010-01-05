#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError
from django.core.handlers.wsgi import WSGIHandler

from optparse import make_option
try:
    from werkzeug import run_simple, DebuggedApplication
except ImportError, e: import_excpetion = e
else: import_excpetion = False

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '--ip', dest='ip', default="localhost", 
            help='IP to bind against, default=localhost'
        ),
        make_option(
            '--port', dest='port', default=8001, 
            help='port to bind against, default=8001'
        ),
    )
    help = 'Help text goes here'

    def handle(self, **options):
        if import_excpetion:
            print "Get werkzeug module form http://werkzeug.pocoo.org/download"
            raise import_excpetion
        run_simple(
            options["ip"], int(options["port"]), 
            DebuggedApplication(WSGIHandler(), True)
        )

