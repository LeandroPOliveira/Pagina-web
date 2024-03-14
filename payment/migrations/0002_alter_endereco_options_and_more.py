# Generated by Django 4.2.3 on 2024-03-14 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name_plural': 'Endereço Entrega'},
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_zipcode',
            new_name='cep_envio',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_city',
            new_name='cidade_envio',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_email',
            new_name='email_envio',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_address1',
            new_name='endereco_envio',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_address2',
            new_name='endereco_envio2',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_state',
            new_name='estado_envio',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='shipping_country',
            new_name='pais_envio',
        ),
    ]
