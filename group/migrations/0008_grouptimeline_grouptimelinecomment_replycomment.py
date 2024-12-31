# Generated by Django 5.1.3 on 2024-12-25 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_alter_pl_graph_sharing_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTimeline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('GroupTitle', models.CharField(max_length=100)),
                ('GroupMessage', models.TextField()),
                ('GroupSkill', models.CharField(max_length=100)),
                ('GroupState', models.CharField(max_length=100)),
                ('GroupPhoto', models.ImageField(blank=True, null=True, upload_to='group_photos/')),
                ('GroupVideo', models.FileField(blank=True, null=True, upload_to='group_videos/')),
                ('Groupcreated_at', models.DateTimeField(auto_now_add=True)),
                ('CreatorFK_id', models.IntegerField()),
                ('GroupFK_id', models.IntegerField()),
            ],
            options={
                'db_table': 'grouptimeline',
            },
        ),
        migrations.CreateModel(
            name='GroupTimelineComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('GrpMessage', models.TextField()),
                ('GrpPictures', models.FileField(blank=True, null=True, upload_to='group_comment_pictures/')),
                ('GrpVideo', models.FileField(blank=True, null=True, upload_to='group_comment_videos/')),
                ('GrpCommenterFK_id', models.IntegerField()),
                ('GrpFeedFK_id', models.IntegerField()),
            ],
            options={
                'db_table': 'grouptimelinecomment',
            },
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=8000)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='reply_comment_images')),
                ('commenter_id', models.IntegerField()),
                ('comment_id', models.IntegerField()),
                ('feed_id', models.IntegerField()),
            ],
        ),
    ]
