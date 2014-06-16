# encoding: utf-8
from django.core.management.base import BaseCommand

from smsbank.apps.hive.utils.scanner import Scanner


class Command(BaseCommand):

    help = 'Scan network and update devices database'

    def handle(self, *args, **options):
        """
        Scan network for devices and create/update corresponding DB entries
        """
        Scanner().scan(persist=True)
