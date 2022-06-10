from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import os
from django.conf import settings
from django.http import HttpResponse



def fileList(request):
    documents = models.Document.objects.all()

    return render(request, "upload-file.html", context = {
        "files": documents
    })

class DocumentView(APIView):
    documents = models.Document.objects.all()

    def get(self, request, id):
        result = {}
        try:
            doc_obj = models.Document.objects.get(id=id)
            path = doc_obj.uploadedFile.url
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = base_path + path
            # import pdb; pdb.set_trace()
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(),content_type="application/octet-stream")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

        except:
            #使用Response回應
            result["msg"] = '錯誤，無此檔案'
            return Response(result, status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        result = {}
        aaa = request.FILES

        if not aaa:
            result['msg'] = '沒有檔案，上傳失敗'
            return Response(result, status.HTTP_400_BAD_REQUEST)

        else:
            uploadedFile = request.FILES["uploadedFile"]
            document = models.Document(uploadedFile = uploadedFile)
            document.save()
            result['msg'] = '上傳成功'
            return Response(result,status.HTTP_200_OK)




