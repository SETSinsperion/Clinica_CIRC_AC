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
    _rec_name = 'relative'
    _description = 'Social-Economic Studies is a relevant medical record zone about patient\'s relatives.'

    relative = fields.Char(
        string="Name",
        help="Relative Name",
        required=True
    )
    job = fields.Char(
        string = 'Occupation',
        help = 'Job of the Relative.',
        required=True
    )
    salary = fields.Float(
        string = 'Salary',
        help = 'Amount earned per month.',
        required=True
    )
    studies = fields.Selection(
        selection=[
            ('na', 'No studies'),
            ('elementary', 'Elementary'),
            ('secondary', 'Secondary'),
            ('high', 'High School'),
            ('bachelor', 'Bachelor\'s degree'),
            ('postgraduate', 'Postgraduate')
        ],
        string = 'Studies',
        help = 'Academic history.',
        required=True
    )
    marital_status = fields.Selection(
        selection=[('sin', 'Single'), ('mar', 'Married'), ('wid', 'Widowed'), ('div', 'Divorced')],
        string='Marital Status',
        help='Marital Status.',
        required=True
    )
    another_details = fields.Char(
        string = 'Another Details',
        help = 'Any detail that does not take in count above-data.'
    )
    record_id = fields.Many2one(
        comodel_name="medical.record",
        string="Medical Record",
        help="Medical record.",
        required=True
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency', 
        compute='_compute_currency_id'
    )

    @api.multi
    def _compute_currency_id(self):
        try:
            main_company = self.sudo().env.ref('base.main_company')
        except ValueError:
            main_company = self.env['res.company'].sudo().search([], limit=1, order="id")
        for ses in self:
            ses.currency_id = self.env.user.company_id.sudo().currency_id.id or main_company.currency_id.id
     