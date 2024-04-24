
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="doctor",
            options={"verbose_name": "Doctor", "verbose_name_plural": "Doctors"},
        ),
        migrations.AlterModelOptions(
            name="specialty",
            options={"verbose_name": "specialty", "verbose_name_plural": "specialties"},
        ),
        migrations.RemoveField(
            model_name="specialty",
            name="symptoms",
        ),
        migrations.AddField(
            model_name="specialty",
            name="disease",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
