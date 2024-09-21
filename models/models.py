# -*- coding: utf-8 -*-

from odoo import models, fields, api


class compras_japon(models.Model):
    _name = 'compras.japon'
    _description = 'Módulo para mi compras en Japón'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio_compra = fields.Integer(placeholder="Precio en Yenes")
    precio_venta = fields.Integer(placeholder="Precio en Euros")
    gastos_envio = fields.Float(compute="_compute_gastos_envio", store=True, string="Gastos de Envío")
    estado = fields.Selection([('nuevo', 'Nuevo'),('en_buen_estado','En buen estado'),('en_estado_adeptable','En estado aceptable')])
    otros = fields.Char()
    vendido = fields.Boolean(default=False)
    enviado = fields.Boolean(default=False)
    fecha = fields.Date()
    etiqueta = fields.Binary(attachment=True)
    envio_ids = fields.Many2one('envios.japon', string='Envio')
    consola= fields.Selection([
        ('ps5', 'PlayStation 5'),
        ('ps4', 'PlayStation 4'),
        ('ps3', 'PlayStation 3'),
        ('ps2', 'PlayStation 2'),
        ('ps1', 'PlayStation'),
        ('psp', 'PlayStation Portable'),
        ('ps_vita', 'PlayStation Vita'),
        ('xbox_series', 'Xbox Series'),
        ('xbox_one', 'Xbox One'),
        ('xbox_360', 'Xbox 360'),
        ('nintendo_switch', 'Nintendo Switch'),
        ('nintendo_wii_u', 'Nintendo Wii U'),
        ('nintendo_wii', 'Nintendo Wii'),
        ('nintendo_ds', 'Nintendo DS'),
        ('nintendo_3ds', 'Nintendo 3DS'),
        ('nintendo_gamecube', 'Nintendo GameCube'),
        ('nintendo_nes', 'Nintendo Entertainment System (NES)'),
        ('nintendo_snes', 'Super Nintendo Entertainment System (SNES)'),
        ('nintendo_64', 'Nintendo 64'),
        ('nintendo_gameboy', 'Nintendo Game Boy'),
        ('nintendo_gameboy_advance', 'Nintendo Game Boy Advance'),
        ('nintendo_ds', 'Nintendo DS'),
        ('nintendo_3ds', 'Nintendo 3DS'),
        ('sega_megadrive', 'Sega Megadrive'),
        ('sega_mastersystem', 'Sega Master System'),
        ('sega_gamegear', 'Sega GameGear'),
        ('sega_saturn', 'Sega Saturn'),
        ('sega_dreamcast', 'Sega Dreamcast'),
        ('atari_2600', 'Atari 2600'),
        ('atari_5200', 'Atari 5200'),
        ('atari_7800', 'Atari 7800'),
        ('pc', 'PC'),
        ('other', 'Other')
    ], string='Consola', help="Selecciona la consola de videojuegos.")
    descripcion = fields.Text("Descripción", compute="_compute_descripcion", store=True)

    @api.depends('nombre', 'consola', 'estado', 'otros')
    def _compute_descripcion(self):
        for record in self:
            if record.nombre and record.consola:
                consola_dict = dict(self._fields['consola'].selection)
                estado_dict = dict(self._fields['estado'].selection)
                consola = consola_dict.get(record.consola, record.consola)
                estado = estado_dict.get(record.estado, record.estado)
                otros_text = f"\n{record.otros}" if record.otros else ""
                record.descripcion = f"Juego japonés {record.nombre} para {consola} \n{estado}{otros_text}\nPrecio no negociable \nNo hago entregas en mano/Solo envíos"
            else:
                record.descripcion = "Información incompleta"

    @api.depends('envio_ids')
    def _compute_gastos_envio(self):
        """Calcula los gastos de envío en función del coste del envío y el número de IDs asociadas."""
        for record in self:
            if record.envio_ids and record.envio_ids.coste_envio:
                total_ids = len(record.envio_ids.id_wallapop)
                if total_ids > 0:
                    record.gastos_envio = record.envio_ids.coste_envio / total_ids
                else:
                    record.gastos_envio = 0
            else:
                record.gastos_envio = 0

    def generate_report(self):
        report_action = self.env.ref('odoo_japan.report_wallapop_image_action').report_action(self)
        # Cambiar el nombre del archivo PDF
        report_action['report_file'] = 'Etiqueta_%s' % self.id_wallapop
        return report_action


class envios_japon(models.Model):
    _name = 'envios.japon'
    _description = 'Módulo para mis envios de Japón'

    nombre = fields.Char()
    id_wallapop = fields.One2many('compras.japon', 'envio_ids', string='Ids Wallapop')
    seguimiento = fields.Char()
    coste_envio = fields.Float(string="Coste de Envío")
    url = fields.Char()
    fecha = fields.Date()
    etiqueta = fields.Binary(attachment=True)

    @api.onchange('coste_envio', 'id_wallapop')
    def _onchange_coste_envio(self):
        """Recalcula los gastos de envío en cada compra asociada cuando se cambian los IDs o el coste de envío."""
        for envio in self:
            for compra in envio.id_wallapop:
                compra._compute_gastos_envio()

class ventas_espana(models.Model):
    _name = 'ventas.espana'
    _description = 'Módulo para mis ventas de España'

    id_wallapop = fields.Integer()
    nombre = fields.Char()
    precio = fields.Integer()
    estado = fields.Selection([('nuevo', 'Nuevo'),('en_buen_estado','En buen estado'),('en_estado_adeptable','En estado aceptable')])
    otros = fields.Char()
    consola= fields.Selection([
        ('ps5', 'PlayStation 5'),
        ('ps4', 'PlayStation 4'),
        ('ps3', 'PlayStation 3'),
        ('ps2', 'PlayStation 2'),
        ('ps1', 'PlayStation'),
        ('psp', 'PlayStation Portable'),
        ('ps_vita', 'PlayStation Vita'),
        ('xbox_series', 'Xbox Series'),
        ('xbox_one', 'Xbox One'),
        ('xbox_360', 'Xbox 360'),
        ('nintendo_switch', 'Nintendo Switch'),
        ('nintendo_wii_u', 'Nintendo Wii U'),
        ('nintendo_wii', 'Nintendo Wii'),
        ('nintendo_ds', 'Nintendo DS'),
        ('nintendo_3ds', 'Nintendo 3DS'),
        ('nintendo_gamecube', 'Nintendo GameCube'),
        ('nintendo_nes', 'Nintendo Entertainment System (NES)'),
        ('nintendo_snes', 'Super Nintendo Entertainment System (SNES)'),
        ('nintendo_64', 'Nintendo 64'),
        ('nintendo_gameboy', 'Nintendo Game Boy'),
        ('nintendo_gameboy_advance', 'Nintendo Game Boy Advance'),
        ('nintendo_ds', 'Nintendo DS'),
        ('nintendo_3ds', 'Nintendo 3DS'),
        ('sega_megadrive', 'Sega Megadrive'),
        ('sega_mastersystem', 'Sega Master System'),
        ('sega_gamegear', 'Sega GameGear'),
        ('sega_saturn', 'Sega Saturn'),
        ('sega_dreamcast', 'Sega Dreamcast'),
        ('atari_2600', 'Atari 2600'),
        ('atari_5200', 'Atari 5200'),
        ('atari_7800', 'Atari 7800'),
        ('pc', 'PC'),
        ('other', 'Other')
    ], string='Consola', help="Selecciona la consola de videojuegos.")
    descripcion = fields.Text("Descripción", compute="_compute_descripcion", store=True)


    @api.depends('nombre', 'consola', 'estado', 'otros')
    def _compute_descripcion(self):
        for record in self:
            if record.nombre and record.consola:
                consola_dict = dict(self._fields['consola'].selection)
                estado_dict = dict(self._fields['estado'].selection)
                consola = consola_dict.get(record.consola, record.consola)
                estado = estado_dict.get(record.estado, record.estado)
                otros_text = f"\n{record.otros}" if record.otros else ""
                record.descripcion = f"Juego japonés {record.nombre} para {consola} \n{estado}{otros_text}\nPrecio no negociable \nNo hago entregas en mano/Solo envíos"
            else:
                record.descripcion = "Información incompleta"
