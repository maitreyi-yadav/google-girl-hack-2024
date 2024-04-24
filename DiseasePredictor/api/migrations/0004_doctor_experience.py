
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_specialty_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(default=5, max_length=255),
            preserve_default=False,
        ),
    ]
