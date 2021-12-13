# -*- coding: utf-8 -*-
# from odoo import http


# class AbcXSicurezzalab(http.Controller):
#     @http.route('/abc_x_sicurezzalab/abc_x_sicurezzalab/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_x_sicurezzalab/abc_x_sicurezzalab/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_x_sicurezzalab.listing', {
#             'root': '/abc_x_sicurezzalab/abc_x_sicurezzalab',
#             'objects': http.request.env['abc_x_sicurezzalab.abc_x_sicurezzalab'].search([]),
#         })

#     @http.route('/abc_x_sicurezzalab/abc_x_sicurezzalab/objects/<model("abc_x_sicurezzalab.abc_x_sicurezzalab"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_x_sicurezzalab.object', {
#             'object': obj
#         })
