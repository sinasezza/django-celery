import os
from django.core.management.utils import get_random_secret_key
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Generates a random secret key for Django"

    def handle(self, *args, **options):
        # Generate a random secret key
        secret_key = get_random_secret_key()

        # Print the generated secret key to the console
        self.stdout.write(f"Generated Secret Key: {secret_key}")

        # Alternatively, you can save the secret key to a file
        # with open("secret_key.txt", "w") as f:
        #     f.write(secret_key)

        # You can also set the generated secret key as an environment variable
        # os.environ["DJANGO_SECRET_KEY"] = secret_key
