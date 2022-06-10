from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "api"

urlpatterns = [
    # path("", views.uploadFile, name = "uploadFile"),
    path("", views.fileList, name = "fileList"),
    path("api/", views.DocumentView.as_view()),
    path("api/<int:id>/", views.DocumentView.as_view())
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )


# urlpatterns = [
# ...
# re_path('^api/v1/testcase/\d+/attachment$', testcase_attachment_views.TestcaseAttachmentAPIView.as_view()), # 給測驗用例添加附件
# re_path('^api/v1/testcase/\d+/attachment/\d+$', testcase_attachment_views.TestcaseAttachmentAPIView.as_view()), # 洗掉、下載測驗用例關聯的附件
