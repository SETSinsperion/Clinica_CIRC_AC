# -*- coding: utf-8 -*-
##########################################################################
# Copyright (C) 2018 Insperion
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##########################################################################
#
# Developer(s)
# ------------
#
# - Daniel Eusebio García Muñoz (degm.insperion@gmail.com)
# 
##########################################################################
from odoo import api, fields, models, _

class MedicalRecordSocioEconomicStudy(models.Model):

    _name = 'medical.record.ses'

    name = fields.Char(
        string = "Socio-economic Studies"
        help='Socio-Economic Studies.',
        required=True
    )
    job = fields.Char(
        string = 'Occupation',
        help = 'Jobs.',
    )
    salary = fields.Float(
        string = 'Salary',
        help = 'Amount earned per month.',
    )
    studies = fields.Char(
        string = 'Studies',
        help = 'Academic history.'
    )
    marital_status = fields.Selection(
        [('sin', 'Single'), ('mar', 'Married'), ('wid', 'Widowed'), ('div', 'Divorced')],
        string='Marital Status',
        help='Marital Status.',
        required=True
    )
     number_people = fields.Integer(
        string = 'Number of people living at home.',
        help = 'Number of people living at home.'
    )
     