# material_management/tests/test_material.py
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material']
        self.Supplier = self.env['res.partner'].create({'name': 'Test Supplier', 'supplier_rank': 1})

    def test_material_price_validation(self):
        """Test to ensure material buy price is >= 100"""
        with self.assertRaises(ValidationError):
            self.Material.create({
                'code': 'MAT001',
                'name': 'Test Material',
                'material_type': 'fabric',
                'buy_price': 50,
                'supplier_id': self.Supplier.id
            })

    def test_create_material(self):
        """Test to create a valid material"""
        material = self.Material.create({
            'code': 'MAT002',
            'name': 'New Material',
            'material_type': 'jeans',
            'buy_price': 150,
            'supplier_id': self.Supplier.id
        })
        self.assertTrue(material.id)
