from rest_framework.response import Response
from ..serializer import *
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from ..models import *
from ..untils.response import BaseResponse
from django.db.models import Q,F
ret=BaseResponse()

class CourseView(ViewSetMixin, APIView):  # 必须先继承ViewSerMixin
    def list(self, request, *args, **kwargs):


        try:
            course_all = Course.objects.all()
            ser = CourseSerializer(instance=course_all, many=True)
            ret.data = ser.data
        except:
            ret.code = 1001
            ret.error = "数据错误"
        return Response(ret.dict)

    def retrieve(self, request, *args, **kwargs):

        try:
            pk = kwargs.get("id")
            print(pk)
            course_obj = CourseDetail.objects.filter(course_id=pk).first()
            print(course_obj)
            ser = CourDetailSerializer(instance=course_obj, many=False)
            print(ser.data)
            ret.data = ser.data
        except:
            ret.code = 1001
            ret.error = "数据错误"
        return Response(ret.dict)


class test(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        # obj = Course.objects.get(id=1)  # 获取到python基础
        # print(obj.price_policy.all())
        obj=CourseDetail.objects.filter(course_id=1).first()
        # queryset=obj.course.coursechapters.all()#反向查询 从详情页到章节表
        # for obj in queryset:
        #     print(obj.name,obj.summary)

        #反向查询到课时目录
        queryset=obj.course.coursechapters.all()
        for row in queryset:
            for i in row.coursesections.all():
                print(i.name,i.order,i.section_type)

        return Response("ok")


class ArticleView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        try:
            queryset=Article.objects.all()
            ser=ArticleSerializers(instance=queryset,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code=1001
            ret.error="数据错误"
        return Response(ret.dict)
    def retrieve(self,request,*args,**kwargs):
        print(kwargs.get("id"))
        try:
            pk=kwargs.get("id")
            obj=Article.objects.filter(id=pk).first()
            ser=ArticleDetailSerializers(instance=obj,many=False)
            ret.data=ser.data
        except Exception as e:
            ret.code=1001
            ret.error="数据错误"
        return Response(ret.dict)
class ArticleViewAgree(ViewSetMixin,APIView):
    def post(self,request,*args,**kwargs):
        try:
            pk=request.data.get("id")
            Article.objects.first(id=pk).update(agree_num=F("agree_num")+1)
            obj=Article.objects.filter(id=pk).first()

            ret.data=obj.agree_num
        except Exception as e:
            ret.code=1001
            ret.error="数据错误"
        return Response(ret.dict)