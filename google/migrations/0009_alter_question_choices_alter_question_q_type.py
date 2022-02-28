# Generated by Django 4.0.2 on 2022-02-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0008_alter_question_choices_alter_question_q_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(related_name='choices', to='google.Choices', verbose_name='پاسخ ها'),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(3, 'چندگزینه ای'), (0, 'کوتاه'), (2, 'انتخابی'), (1, 'پاراگراف')], default=0, verbose_name='نوع سوال'),
        ),
    ]