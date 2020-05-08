#!/usr/bin/env python3
""" populating and updating purbeurre DB from openfoodfacts API."""

from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError


class Command(BaseCommand):
    help = 'Update DB from OFF API'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(self.style.SUCCESS('DB successfully updated'))