# Generated by Django 3.2.12 on 2022-05-20 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0002_auth_authtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': '16. 文章来源',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.TextField(max_length=1024)),
                ('disagree_number', models.IntegerField(default=0, verbose_name='踩')),
                ('agree_number', models.IntegerField(default=0, verbose_name='赞同数')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.auth', verbose_name='会员名')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='类型')),
                ('p_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.comment', verbose_name='父级评论')),
            ],
            options={
                'verbose_name_plural': '19. 通用评论表',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='标题')),
                ('article_type', models.SmallIntegerField(choices=[(0, '资讯'), (1, '视频')], default=0)),
                ('brief', models.TextField(max_length=512, verbose_name='摘要')),
                ('head_img', models.CharField(max_length=255)),
                ('content', models.TextField(verbose_name='文章正文')),
                ('pub_date', models.DateTimeField(verbose_name='上架日期')),
                ('offline_date', models.DateTimeField(verbose_name='下架日期')),
                ('status', models.SmallIntegerField(choices=[(0, '在线'), (1, '下线')], default=0, verbose_name='状态')),
                ('order', models.SmallIntegerField(default=0, help_text='文章想置顶，可以把数字调大，不要超过1000', verbose_name='权重')),
                ('vid', models.CharField(blank=True, help_text='文章类型是视频, 则需要添加视频VID', max_length=128, null=True, verbose_name='视频VID')),
                ('comment_num', models.SmallIntegerField(default=0, verbose_name='评论数')),
                ('agree_num', models.SmallIntegerField(default=0, verbose_name='点赞数')),
                ('view_num', models.SmallIntegerField(default=0, verbose_name='观看数')),
                ('collect_num', models.SmallIntegerField(default=0, verbose_name='收藏数')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('position', models.SmallIntegerField(choices=[(0, '信息流'), (1, 'banner大图'), (2, 'banner小图')], default=0, verbose_name='位置')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.articlesource', verbose_name='来源')),
            ],
            options={
                'verbose_name_plural': '17. 文章',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.auth')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name_plural': '18. 通用收藏表',
                'unique_together': {('content_type', 'object_id', 'account')},
            },
        ),
    ]
