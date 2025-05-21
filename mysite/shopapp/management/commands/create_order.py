from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Order


class Command(BaseCommand):
    """
    Создание новых заказов
    """

    def handle(self, *args, **options):
        self.stdout.write("Начало создания заказов")

        try:
            user = User.objects.get(username="admin")
            order, created = Order.objects.get_or_create(
                delivery_address="Moscow", promocode="test", user=user
            )

            self.stdout.write(
                self.style.SUCCESS(f"Создание заказа {order.id} завершено")
            )

        except BaseException as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при создании заказа: {e}"))
