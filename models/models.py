# -*- coding: utf-8 -*-

from odoo import models, fields, api


class compras_japon(models.Model):
    _name = 'compras.japon'
    _description = 'Módulo para mi compras en Japón'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio_compra = fields.Integer()
    precio_venta = fields.Integer()
    gastos_envio = fields.Float()
    descripcion = fields.Text()
    vendido = fields.Boolean(default=False)
    fecha = fields.Date()
    etiqueta = fields.Binary(attachment=True)
    envio_ids = fields.Many2one('envios.japon', string='Envio')



    # @api.depends('coste_envio')
    # def _gastos_envio(self):
    #     for record in self:
    #         record.id_wallapop = float(record.coste_envio) / len(self.id_wallapop)

    def generate_report(self):
        return self.env.ref('odoo_japan.report_wallapop_image').report_action(self)

class envios_japon(models.Model):
    _name = 'envios.japon'
    _description = 'Módulo para mis envios de Japón'

    nombre = fields.Char()
    id_wallapop = fields.One2many('compras.japon', 'envio_ids', string='Ids Wallapop')
    seguimiento = fields.Char()
    coste_envio = fields.Float()
    url = fields.Char()
    fecha = fields.Date()
    etiqueta = fields.Binary(attachment=True)

class ventas_espana(models.Model):
    _name = 'ventas.espana'
    _description = 'Módulo para mis ventas de España'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio = fields.Integer()
    vendido = fields.Boolean()
    fecha = fields.Date()
    etiqueta = fields.Binary(attachment=True)
    descripcion = fields.Text()

