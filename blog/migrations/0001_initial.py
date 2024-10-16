# Generated by Django 5.1.2 on 2024-10-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('head0', models.TextField(default='')),
                ('head1', models.TextField(default='')),
                ('head2', models.TextField(default='')),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
