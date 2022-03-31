# Generated by Django 4.0.3 on 2022-03-30 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_alter_user_email_alter_user_first_name_and_more'),
        ('api', '0002_alter_issue_assignee_alter_issue_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contribution',
            field=models.ManyToManyField(through='api.Contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_issue', to=settings.AUTH_USER_MODEL),
        ),
    ]