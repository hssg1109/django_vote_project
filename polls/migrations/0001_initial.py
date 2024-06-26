# Generated by Django 5.0.3 on 2024-04-19 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('pollId', models.AutoField(auto_created=True, db_column='pollId', primary_key=True, serialize=False)),
                ('questionText', models.CharField(db_column='questionText', max_length=200,blank=True)),
                ('pollImage', models.ImageField(blank=True, db_column='pollImage', max_length=50, upload_to='image/%Y/%m/%d')),
                ('expireDate', models.DateField(db_column='expireDate', null=True,blank=True)),
                ('secretPoll', models.BooleanField(db_column='secretPoll', default=True, null=True)),
                ('total', models.IntegerField(blank=True, default=0)),
                ('userId', models.ForeignKey(db_column='userId', null='True', on_delete=django.db.models.deletion.DO_NOTHING, related_name='polls', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('choiceId', models.AutoField(auto_created=True, db_column='choiceId', primary_key=True, serialize=False)),
                ('choiceText', models.CharField(db_column='choiceText', max_length=100)),
                ('count', models.IntegerField(blank=True, default=0)),
                ('pollId', models.ForeignKey(db_column='pollId', on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='polls.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='polls.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='polls.poll')),
                ('voter', models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='vote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('poll', 'voter'), name='unique_voter_for_questions'),
        ),
    ]
