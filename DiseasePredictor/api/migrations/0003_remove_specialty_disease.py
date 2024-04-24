
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230303_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='disease',
        ),
    ]
