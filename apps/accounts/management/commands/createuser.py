import logging

from django.core.management.base import BaseCommand

from accounts.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            required=True,
        )
        parser.add_argument(
            '--name',
            required=False,
        )
        parser.add_argument(
            '--password',
            default=None,
        )
        parser.add_argument(
            '--is-superuser',
            action="store_true",
        )
        parser.add_argument(
            '--is-staff',
            action="store_true",
        )
        # is_active is True by default
        parser.add_argument(
            '--is-not-active',
            action="store_false",
            dest='is_active'
        )

    def handle(self, **options):
        user = User(
            name=options['name'],
            email=options['email'],
            is_superuser=options['is_superuser'],
            is_staff=options['is_staff'] or options['is_superuser'],
            is_active=options['is_active'],
        )
        # if password is not specified, then username is used.
        password = options['password'] or 'default'
        user.set_password(password)
        user.save()
        logger.info('User "%(name)s" was created successfully.', options)
