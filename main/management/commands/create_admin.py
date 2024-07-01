from django.core.management.base import BaseCommand
from main.models import CustomUser

class Command(BaseCommand):
    help = 'Creates the admin user'
    def handle(self, *args, **options):
        if not CustomUser.objects.filter(username='thomas').exists():
            CustomUser.objects.create_superuser('thomas', 'thomas.n@compfest.id', 'Admin123', 
              first_name='Thomas', last_name='N', 
              phone_number='08123456789', role='admin')
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))