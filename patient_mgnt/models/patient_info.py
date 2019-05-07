# -*- coding: utf-8 -*-

from flectra import api, fields, models
from flectra.exceptions import ValidationError

class PatientInfo(models.Model):
    _name = "patient.info"

    @api.depends("doctor_id")
    def _calculate_store_data(self):
        print("---------------patient / name, ID /----------------", self.name, self.doctor_id)

        self.appoint_date = self.doctor_id.appoint_date
        self.state = self.doctor_id.state

    name = fields.Char(string="Patient Name",required=True)
    pat_code = fields.Integer(string="Patient id",required=True)
    pat_gender = fields.Selection([('male', 'MALE'),
                                   ('female', 'FEMALE')], string="Gender")
    pat_weight = fields.Float(string="Patient Weight")
    pat_address = fields.Text(string="Patient Address")
    pat_mobile = fields.Char(string="Patient Mobile Number")

    appoint_date = fields.Date(string="Appointment", compute="_calculate_store_data", store=True)
    disease = fields.Many2one("disease.info", string="select disease")
    #doctor_line = fields.One2many("doctor.info","patient_id", string="Patient Name")
    doctor_id = fields.Many2one("doctor.info", string="Approved ")

    @api.constrains('pat_mobile')
    def check_pat_mobile(self):
        if len(self.pat_mobile) > 10 or len(self.pat_mobile) < 10:
            raise ValidationError("Mobile no invalid")

    _sql_constraints = [
        ('name_uniq', 'unique (pat_mobile)', "The mobile number of the patient should be unique!")
    ]

    state = fields.Selection([('sc', 'success'),
                                    ('pn', 'pending'),
                                    ('rj', 'rejected')], string="status")


