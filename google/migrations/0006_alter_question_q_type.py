# Generated by Django 4.0.2 on 2022-02-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0005_form_creator_alter_question_q_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(3, 'انتخابی'), (0, 'کوتاه'), (2, 'چندگزینه ای'), (1, 'پاراگراف')], default=0, verbose_name='نوع سوال'),
        ),
    ]