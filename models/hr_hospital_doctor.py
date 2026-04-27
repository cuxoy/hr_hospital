from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"

    name = fields.Char(string="Doctor Name", required=True)
    phone = fields.Char(string="Phone")
    specialty = fields.Char(string="Specialty")
    active = fields.Boolean(default=True)
