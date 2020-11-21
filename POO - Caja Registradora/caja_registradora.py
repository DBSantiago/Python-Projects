# -*- coding: utf-8 -*-
import unittest

class CajaRegistradora(object):
    def __init__(self):
        self.compra = Compra()

    def agregar_producto(self, codigo):
        producto = Producto(parent=self)
        return producto.agregar_producto(codigo)

    def calcular_subtotal(self):
        for unidades, precio in self.compra.pedido:
            self.compra.subtotal += unidades * precio
        return self.compra.subtotal 

    def finalizar_compra(self):
        return self.compra.finalizar_compra()

    def calcular_total(self):
        #Los precios de los artículos son sumados al subtotal con el descuento ya hecho
        #Por lo tanto el total == subtotal
        return self.calcular_subtotal()

    def calcular_vuelto(self, pago_cliente):
        return pago_cliente - self.compra.subtotal


class Producto(object):
    def __init__(self,parent):
        self.parent = parent
        self.lista = ListaPrecio()

    def agregar_producto(self,codigo):
        self.codigo = codigo
        self.precio = self.lista.obtener_precio(self.codigo)
        self.parent.compra.pedido[codigo] = self.precio


class ListaPrecio(object):
    def __init__(self):
        self.lista_precio = {
            105406: 65.0,
            105812: 57.0,
            108408: 42.5,
            102050: 78.0,
            107620: 120.0,
            190416: 64.5
        }
    def obtener_precio(self,codigo, descuento=0):
        if descuento == 0:
            return self.lista_precio[codigo]
        else:
            return self.lista_precio[codigo] * (100 - descuento) / 100

class Compra(object):
    def __init__(self):
        self.pedido = {}
        self.subtotal = 0

    def finalizar_compra(self):
        return 'Compra finalizada.'



class CajaRegistradoraTest(unittest.TestCase):
    def prueba_agregar_producto(self):
        self.caja = CajaRegistradora()
        self.caja.agregar_producto(105406)
        self.assertEqual(65.0,self.caja.compra.subtotal)

    def prueba_calcular_total(self):
        self.caja = CajaRegistradora()
        self.caja.agregar_producto(105406)
        self.caja.agregar_producto(107620)
        self.assertEqual(185.0,self.caja.compra.subtotal)

    def prueba_calcular_vuelto(self):
        self.caja = CajaRegistradora()
        self.caja.agregar_producto(105406)
        self.caja.agregar_producto(107620)
        self.assertEqual(15,self.caja.calcular_vuelto(200))

    def prueba_finalizar_compra(self):
        self.caja = CajaRegistradora()
        self.assertEqual('Compra finalizada.',self.caja.finalizar_compra())

if __name__ == '__main__':
    unittest.main()
