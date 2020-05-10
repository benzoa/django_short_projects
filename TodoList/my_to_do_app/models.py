from django.db import models

# Table은 class로 표현
class Todo(models.Model):
    # 자료형 : CharField, 최대 길이를 255로 제한
    content = models.CharField(max_length = 255)
    isDone = models.BooleanField(default = False)
