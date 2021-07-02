from django.contrib import admin
from core import models


# Register your models here.

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    pass
