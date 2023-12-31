import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            # phone = Phone(name=phone['name'], image=phone['image'], price=phone['price'], release_date=phone['release_date'], lte_exists=phone['lte_exists'])
            # phone.save()
            Phone.objects.create(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=create_slug(phone['name']),
            )

        print(f'данные успешно загружены в базу данных')

def create_slug(text: str) -> str:
    text = text.lower().replace(' ', '_').replace('&', '_and_')
    return text