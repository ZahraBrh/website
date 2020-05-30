# Generated by Django 3.0.5 on 2020-05-28 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articl',
            name='auteurs',
            field=models.ManyToManyField(null=True, through='firstpage.Ecrit', to='firstpage.Auteur'),
        ),
        migrations.AddField(
            model_name='auteur',
            name='articls',
            field=models.ManyToManyField(null=True, through='firstpage.Ecrit', to='firstpage.Articl'),
        ),
        migrations.AddField(
            model_name='ecrit',
            name='articlEcrit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='firstpage.Articl'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articl',
            name='nbd_cit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='adresse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='numTel',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ecrit',
            name='auteurEcrit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstpage.Auteur'),
        ),
        migrations.AlterField(
            model_name='ecrit',
            name='ordreAuteur',
            field=models.IntegerField(),
        ),
    ]