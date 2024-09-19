

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='url',
            name='custom_url',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='url',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
