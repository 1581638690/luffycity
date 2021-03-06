from django.middleware.common import MiddlewareMixin
class CORSMIDDLEware(MiddlewareMixin):
    def process_response(self,request,response):
        response["Access-Control-Allow-Origin"]="*"
        if request.method=="OPTIONS":
            response["Access-Control-Allow-Headers"]="Content-Type"
            response["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETES"
        return response