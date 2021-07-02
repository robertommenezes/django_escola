from django.db import models


# Create your models here.

class EstadoCivil(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descricao = models.CharField(db_column='tx_descricao', max_length=40, null=False, blank=False, unique=True)

    class Meta:
        db_table = 'estado_civil'
        managed = True

    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = ('M', 'Masculino')
        FEMININO = ('F', 'Feminino')

    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(
        db_column='tx_nome',
        null=False,
        max_length=100
    )
    sexo = models.CharField(
        db_column='cs_sexo',
        max_length=1,
        null=True,
        blank=True,
        choices=Sexo.choices
    )
    cursos = models.ManyToManyField(
        to='Curso',
        through='CursoAluno'
    )
    estado_civil = models.ForeignKey(
        to='EstadoCivil',
        on_delete=models.DO_NOTHING,
        db_column='id_estado_civil',
        null=True,
        blank=True,
        related_name='alunos'
    )

    class Meta:
        db_table = 'aluno'
        managed = True

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome_curso = models.CharField(
        db_column='tx_nome',
        null=False,
        max_length=40
    )
    alunos = models.ManyToManyField(
        to='Aluno',
        through='CursoAluno'
    )

    class Meta:
        db_table = 'curso'
        managed = True

    def __str__(self):
        return self.nome_curso


class CursoAluno(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )

    id_aluno = models.ForeignKey(
        to='Aluno',
        on_delete=models.DO_NOTHING,
        db_column='id_aluno',
        null=False,
        blank=False
    )
    id_curso = models.ForeignKey(
        to='Curso',
        on_delete=models.DO_NOTHING,
        db_column='id_curso',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'curso_aluno'
        managed = True
        index_together = [
            ('id_aluno', 'id_curso')
        ]
