from django.db import models


# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', null=False, max_length=100)

    class Meta:
        db_table = 'aluno'
        managed = True

    def __str__(self):
        return self.nome

class Curso(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome_curso = models.CharField(db_column='tx_nome', null=False, max_length=40)

    class Meta:
        db_table = 'curso'
        managed = True

    def __str__(self):
        return self.nome_curso