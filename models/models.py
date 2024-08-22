# -*- coding: utf-8 -*-

from odoo import models, fields, api


class compras_japan(models.Model):
    _name = 'compras.japan'
    _description = 'Módulo para mi compras en Japón'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio = fields.Integer()
    gastos_envio = fields.Float(compute="_gastos_envio", store=True)
    description = fields.Text()
    vendido = fields.Boolean()
    fecha = fields.Date()
    etiqueta = fields.image()

    @api.depends('coste_envio')
    def _gastos_envio(self):
        for record in self:
            record.id_wallapop = float(record.coste_envio) / len(self.id_wallapop)

class envios_japon(models.Model):
    _name = 'envios.japon'
    _description = 'Módulo para mis envios de Japón'

    id_wallapop = fields.Integer()
    seguimiento = fields.char()
    coste_envio = fields.Float()
    url = fields.url()
    fecha = fields.Date()
    etiqueta = fields.image()

class ventas_espana(models.Model):
    _name = 'ventas.espana'
    _description = 'Módulo para mis ventas de España'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio = fields.Integer()
    vendido = fields.Boolean()
    fecha = fields.Date()
    etiqueta = fields.image()
