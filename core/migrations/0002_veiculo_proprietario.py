# Generated by Django 2.1.2 on 2018-10-13 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='proprietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
            preserve_default=False,
        ),
    ]
