# Generated by Django 4.0.4 on 2023-04-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=100)),
                ('page_de_garde', models.ImageField(default='', null=True, upload_to='image_stories')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='story_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', models.ImageField(default='', upload_to='files_stories')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story_pub.story')),
            ],
        ),
    ]
