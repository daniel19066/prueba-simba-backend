# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clientes(models.Model):
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EMPRESA')  # Field name made lowercase.
    id_cliente = models.AutoField(db_column='ID_CLIENTE', primary_key=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='CLIENTE')  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=250, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    paginaweb = models.CharField(db_column='PAGINAWEB', max_length=450, db_collation='Modern_Spanish_CI_AS',default="")  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='FECHA_CREACION')  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'CLIENTES'
        unique_together = (('empresa', 'cliente'),)


class DetFactura(models.Model):
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EMPRESA')  # Field name made lowercase.
    id_factura = models.OneToOneField('MaeFactura', models.DO_NOTHING, db_column='ID_FACTURA', primary_key=True)  # Field name made lowercase. The composite primary key (ID_FACTURA, CONSECUTIVO) found, that is not supported. The first column is selected.
    consecutivo = models.IntegerField(db_column='CONSECUTIVO')  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_PRODUCTO' )  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=20, decimal_places=2)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=20, decimal_places=2)  # Field name made lowercase.
    sub_total = models.DecimalField(db_column='SUB_TOTAL', max_digits=20, decimal_places=2)  # Field name made lowercase.

    
    class Meta:
        managed = False
        db_table = 'DET_FACTURA'
        unique_together = (('id_factura', 'consecutivo'),)


class Empresa(models.Model):
    empresa = models.IntegerField(db_column='EMPRESA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'EMPRESA'


class MaeFactura(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EMPRESA')  # Field name made lowercase.
    id_factura = models.AutoField(db_column='ID_FACTURA', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='NUMERO')  # Field name made lowercase.
    fecha_factura = models.DateTimeField(db_column='FECHA_FACTURA')  # Field name made lowercase.
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ID_CLIENTE')  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=300, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=20, decimal_places=2)  # Field name made lowercase.
    fecha_auditoria = models.DateTimeField(db_column='FECHA_AUDITORIA')  # Field name made lowercase.

    
    class Meta:
        managed = False
        db_table = 'MAE_FACTURA'


class Productos(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EMPRESA' )  # Field name made lowercase.
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='PRODUCTO', max_length=30, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fotoproducto = models.CharField(db_column='FOTOPRODUCTO', max_length=250, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fecha_creacion = models.DateTimeField(db_column='FECHA_CREACION')  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'PRODUCTOS'
        unique_together = (('empresa', 'producto'),)



