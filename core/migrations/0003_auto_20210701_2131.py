# Generated by Django 3.2.5 on 2021-07-02 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cursoaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(db_column='tx_descricao', max_length=40, unique=True)),
            ],
            options={
                'db_table': 'estado_civil',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='cursos',
            field=models.ManyToManyField(through='core.CursoAluno', to='core.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='cs_sexo', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(through='core.CursoAluno', to='core.Aluno'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='estado_civil',
            field=models.ForeignKey(blank=True, db_column='id_estado_civil', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='alunos', to='core.estadocivil'),
        ),
    ]
