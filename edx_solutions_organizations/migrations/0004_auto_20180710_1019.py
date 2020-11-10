from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_solutions_organizations', '0003_auto_20180702_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='attributes',
            field=models.CharField(default='{}', max_length=512),
        ),
    ]
