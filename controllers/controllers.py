# material_management/controllers/controllers.py
from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/material', auth='user', type='json')
    def list_materials(self, material_type=None):
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        materials = request.env['material'].search(domain)
        return materials.read(['code', 'name', 'material_type', 'buy_price', 'supplier_id'])

    @http.route('/material/<int:material_id>', auth='user', methods=['POST'], type='json')
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if material.exists():
            material.write(kwargs)
        return {'status': 'success'}

    @http.route('/material/<int:material_id>/delete', auth='user', methods=['POST'], type='json')
    def delete_material(self, material_id):
        material = request.env['material'].browse(material_id)
        if material.exists():
            material.unlink()
        return {'status': 'success'}
