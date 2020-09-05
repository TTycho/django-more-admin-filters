# Generated by Django 2.2.16 on 2020-09-05 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropdown_lte3', models.IntegerField()),
                ('dropdown_gt3', models.IntegerField()),
                ('multiselect', models.IntegerField()),
                ('multiselect_dropdown', models.IntegerField()),
                ('choices_dropdown', models.CharField(blank=True, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'), ('6', 'six'), ('7', 'seven'), ('8', 'eight'), ('9', 'nine')], max_length=255)),
                ('c_models', models.ManyToManyField(to='testapp.ModelC')),
                ('multiselect_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiselect_related_reverse', to='testapp.ModelB')),
                ('multiselect_related_dropdown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiselect_related_dropdown_reverse', to='testapp.ModelB')),
                ('related_dropdown', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_dropdown_reverse', to='testapp.ModelB')),
            ],
        ),
    ]
