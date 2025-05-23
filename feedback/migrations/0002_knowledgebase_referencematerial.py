# Generated by Django 5.0.6 on 2024-08-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('category', models.CharField(choices=[('general', 'General'), ('technical', 'Technical'), ('billing', 'Billing'), ('other', 'Other')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.CharField(choices=[('faq', 'FAQ'), ('instruction', 'Instruction'), ('guide', 'Guide'), ('other', 'Other')], max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
