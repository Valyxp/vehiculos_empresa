from gestion_vehiculos.models import Vehiculo, Chofer, RegistroContabilidad


def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(
        patente=patente, marca=marca, modelo=modelo, year=year
    )
    return vehiculo


def crear_chofer(rut, nombre, apellido):
    chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido)
    return chofer


def crear_registro_contable(fecha_compra, valor, vehiculo):
    registro = RegistroContabilidad.objects.create(
        fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo
    )
    return registro


def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()


def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()


def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()


def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = True
    vehiculo.save()


def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)


def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)


def asignar_chofer_a_vehiculo(rut, patente):
    chofer = obtener_chofer(rut)
    vehiculo = obtener_vehiculo(patente)
    chofer.vehiculo = vehiculo
    chofer.save()


def imprimir_datos_vehiculos():
    return list(Vehiculo.objects.filter(activo=True))
