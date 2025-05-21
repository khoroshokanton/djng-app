from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Создание новых продуктов
    """

    def handle(self, *args, **options):
        self.stdout.write("Создание продукта")

        products_names = ["Laptop", "Descyop", "Smartphone"]

        for produc_name in products_names:
            product, created = Product.objects.get_or_create(name=produc_name)

            self.stdout.write(self.style.SUCCESS(f"Продукт {produc_name} создан"))

        self.stdout.write(self.style.SUCCESS("Продукты созданы"))
