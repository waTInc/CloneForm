# Generated by Django 4.0.2 on 2022-02-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0003_rename_choice_choices_text_alter_question_q_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.IntegerField(choices=[(0, 'چندگزینه ای'), (2, 'کوتاه'), (1, 'پاراگراف'), (3, 'انتخابی')], default=0, verbose_name='نوع سوال'),
        ),
    ]