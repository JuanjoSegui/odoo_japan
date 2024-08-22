# -*- coding: utf-8 -*-
# from odoo import http


# class OdooJapan(http.Controller):
#     @http.route('/odoo_japan/odoo_japan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_japan/odoo_japan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_japan.listing', {
#             'root': '/odoo_japan/odoo_japan',
#             'objects': http.request.env['odoo_japan.odoo_japan'].search([]),
#         })

#     @http.route('/odoo_japan/odoo_japan/objects/<model("odoo_japan.odoo_japan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_japan.object', {
#             'object': obj
#         })
