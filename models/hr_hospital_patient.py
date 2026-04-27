from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"

    name = fields.Char(string="Patient Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    phone = fields.Char(string="Phone")
    doctor_id = fields.Many2one(
        comodel_name="hospital.doctor",
        string="Observing Doctor",
    )
    active = fields.Boolean(default=True)
