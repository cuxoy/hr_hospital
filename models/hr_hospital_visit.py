from odoo import fields, models


class HospitalVisit(models.Model):
    _name = "hospital.visit"
    _description = "Patient Visit"

    name = fields.Char(string="Visit Reference", required=True)
    patient_id = fields.Many2one(
        comodel_name="hospital.patient",
        string="Patient",
        required=True,
    )
    doctor_id = fields.Many2one(
        comodel_name="hospital.doctor",
        string="Doctor",
        required=True,
    )
    disease_id = fields.Many2one(
        comodel_name="hospital.disease",
        string="Disease",
    )
    visit_date = fields.Datetime(string="Visit Date", default=fields.Datetime.now)
    notes = fields.Text(string="Notes")
