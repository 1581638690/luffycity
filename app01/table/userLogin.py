import uuid
from ..models import *
from ..serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from ..untils.response import BaseResponse

ret=BaseResponse()
class LoginView(APIView):
    """
    用户登录模块
    """
    def post(self,request,*args,**kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            username=request.data.get("username")
            password=request.data.get("password")
            users=Auth.objects.filter(username=username,password=password).first()
            if users:
                token=str(uuid.uuid4())
                AuthToken.objects.update_or_create(auth=users,defaults={"token":token})
                ret.token=token
        except Exception as e:
            ret.code=1001
            ret.error="账号密码错误"
        return Response(ret.dict)

