# Generated by Django 3.2.23 on 2023-11-29 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbycentre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hobbycentre.question'),
            preserve_default=False,
        ),
    ]