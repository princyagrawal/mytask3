# -*- coding: utf-8 -*-
from flectra import api, fields, models

class DieaseInfo(models.Model):
    _name="disease.info"

    name = fields.Selection([('T1D','Diabetes'),
                             ('MS','Skin Disease'),
                             ('UC','Heart Disease'),
                             ('lupus','Lupus'),
                             ('type-5','rheumatoid-arth'),
                             ('type-6','Allergies & Asthma'),
                             ('type-7','Celiac Disease'),
                             ('type-8','Relapsing Polychondritis'),
                             ('type-9','Liver Disease'),
                             ('type-10','Infectious Diseases'),
                             ],
                            string="Disease Name",)
    description = fields.Text(string="Disease description")
    image = fields.Binary(string="Symbol")

    doctor_ids = fields.Many2many("doctor.info","disease_doctor_rel","disease_id", "doctor_id" ,string="doctor")
