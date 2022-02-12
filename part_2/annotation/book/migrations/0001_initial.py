# Generated by Django 4.0.2 on 2022-02-12 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('author', models.CharField(max_length=80)),
                ('published_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookChapterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=80)),
                ('is_mcq_available', models.BooleanField(default=False)),
                ('num_of_topics', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookdata')),
            ],
        ),
    ]
