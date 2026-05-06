from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["hospital.medic.info"]
    _description = "Patient"

    name = fields.Char(string="Patient Name", required=True)
    phone = fields.Char(string="Phone")
    personal_doctor_id = fields.Many2one(
        comodel_name="hospital.doctor",
        string="Personal Doctor",
    )
    doctor_history_ids = fields.One2many(
        comodel_name="hospital.doctor.history",
        inverse_name="patient_id",
        string="Personal Doctor History",
    )
    insurance_policy_number = fields.Char(
        string="Insurance Policy Number",
        size=20,
    )
    active = fields.Boolean(default=True)