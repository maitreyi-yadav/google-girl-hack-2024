
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_doctor_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='days_available',
            field=models.TextField(default='never', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='time_available',
            field=models.TextField(default='never', max_length=255),
            preserve_default=False,
        ),
    ]
