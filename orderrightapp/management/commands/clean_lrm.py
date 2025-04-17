from django.core.management.base import BaseCommand
from orderrightapp.models import Products

class Command(BaseCommand):
    help = "Clean invisible LRM characters (\\u200e) from model fields"

    def handle(self, *args, **kwargs):
        count = 0
        for obj in Products.objects.all():
            if obj.description and '\u200e' in obj.description:
                obj.description = obj.description.replace('\u200e', '')
                obj.save()
                count += 1
        self.stdout.write(self.style.SUCCESS(f"Cleaned {count} objects."))
