from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class CourseSerializer(ModelSerializer):
    sub_category = serializers.CharField(source="sub_category.name")
    course_type = serializers.CharField(source="get_course_type_display")
    level = serializers.CharField(source="get_level_display")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Course
        fields = ["name", "course_img", "sub_category", "course_type", "degree_course", "brief", "level", "pub_date",
                  "period", "order", "attachment_path", "status", "template_id"]


class CourDetailSerializer(ModelSerializer):
    course_name = serializers.CharField(source="course.name")
    level = serializers.CharField(source="course.get_level_display")
    price_policy = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()
    sections=serializers.SerializerMethodField()
    class Meta:
        model = CourseDetail
        fields = ["level", "hours", "course_name", "course_slogan", "video_brief_link", "why_study",
                  "what_to_study_brief", "career_improvement", "prerequisite", "price_policy", "chapter","sections"]

    def get_price_policy(self, obj):
        queryset = obj.course.price_policy.all()
        return [{"price": row.price, "valid_period": row.valid_period} for row in queryset]

    def get_chapter(self, obj):
        queryset = obj.course.coursechapters.all()
        return [{"id":row.id,"chapter": row.chapter, "name": row.name, "summary": row.summary, "pub_date": row.pub_date} for row in
                queryset]
    def get_sections(self,obj):
        queryset=obj.course.coursechapters.all()
        return [{"chapter_id":row_obj.chapter_id,"name":row_obj.name,"order":row_obj.order,"section_type":row_obj.section_type,"video_time":row_obj.video_time,"pub_date":row_obj.pub_date,"free_trail":row_obj.free_trail} for row in queryset for row_obj in row.coursesections.all()]

class ArticleSerializers(ModelSerializer):
    article_type=serializers.CharField(source="get_article_type_display")
    source=serializers.CharField(source="source.name")
    position=serializers.CharField(source="get_position_display")
    class Meta:
        model=Article
        fields=["title", "source", "article_type", 'head_img', 'brief', 'pub_date', 'comment_num', 'agree_num',
                  'view_num', 'collect_num', 'position']

class ArticleDetailSerializers(ModelSerializer):
    class Meta:
        model=Article
        fields=['title', 'pub_date', 'agree_num', 'view_num', 'collect_num', 'comment_num', 'source', 'content',
                  'head_img']