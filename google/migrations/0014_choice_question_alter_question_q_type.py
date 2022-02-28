# Generated by Django 4.0.2 on 2022-02-28 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0013_alter_question_q_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='google.question', verbose_name='سوال مربوطه'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(0, 'کوتاه'), (1, 'پاراگراف'), (2, 'انتخابی'), (3, 'چندگزینه ای')], default=0, verbose_name='نوع سوال'),
        ),
    ]