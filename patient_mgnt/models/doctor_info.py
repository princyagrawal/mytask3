# -*- coding: utf-8 -*-

from flectra import api, fields, models
from flectra.exceptions import ValidationError

class DoctorInfo(models.Model):
    _name = "doctor.info"

    name = fields.Char(string="Doctor Name",required=True)
    doc_code = fields.Integer(string="Doctor id",required=True)
    doc_gender = fields.Selection([('male', 'MALE'),
                                   ('female', 'FEMALE')], string="Gender")
    doc_address = fields.Text(string="Doctor Address")
    doc_mobile = fields.Char(string="Doctor Mobile Number")
    appoint_date = fields.Date(string="Doctor available on", required=True)

    patient_line = fields.One2many("patient.info","doctor_id",string="Approved")

    disease_ids = fields.Many2many("disease.info", "disease_doctor_rel", "doctor_id", "disease_id",
                                   string="specialist in")

    @api.constrains('doc_mobile')
    def check_doc_mobile(self):
        if len(self.doc_mobile) > 10 or len(self.doc_mobile) < 10:
            raise ValidationError("Mobile no invalid")

    @api.onchange("patient_id")
    def onchange_store_data(self):
        print("---------------patient / name, ID /----------------", self.name, self.patient_id)

    state = fields.Selection([('sc', 'success'),
                                   ('pn', 'pending'),
                                   ('rj', 'rejected')], string="status", default="sc")

    def state_pending(self):
        self.state = "pn"

    def state_rejected(self):
        self.state = 'rj'

    def state_confirm(self):
        self.state   = 'sc'


