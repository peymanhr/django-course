from django.core.management.base import BaseCommand, CommandError

from ...models import Product

import logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):

    help = "Reset all prices to 0"

    def add_arguments(self, parser):
        parser.add_argument(
            '--price',
            type=int,
            help='Price amount'
        )

    def handle(self, *args, **options):
        products = Product.objects.all()
        for product in products:
            product.price = options["price"]
            product.save()
            msg = f"Set price to {options['price']} for {product.name}"
            self.stdout.write(self.style.SUCCESS(msg))
            logger.info(msg, extra={'user': 'admin'})
            