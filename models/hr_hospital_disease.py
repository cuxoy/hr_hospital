from odoo import fields, models


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _description = "Disease"

    name = fields.Char(string="Disease Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
