# Generated by Django 3.1.1 on 2020-09-23 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0007_auto_20200921_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity_sold', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='detalle_pedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommapp.pedido'),
        ),
        migrations.AlterField(
            model_name='detalle_pedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommapp.producto'),
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ManyToManyField(through='ecommapp.InvoiceDetail', to='ecommapp.producto')),
            ],
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_invoice', to='ecommapp.invoices'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_product', to='ecommapp.producto'),
        ),
    ]
