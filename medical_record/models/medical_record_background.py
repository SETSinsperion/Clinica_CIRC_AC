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
# - Sergio Ernesto Tostado Sánchez (sets.insperion@gmail.com)
# 
##########################################################################

from odoo import api, fields, models, _


class MedicalRecordBackground(models.Model):

    _name = 'medical.record.background'
    _rec_name = 'summary'
    _description = 'Medicals Backgrounds, both pathological and hereditary.'

    summary = fields.Char(
        string='Summary',
        help='Background summary.',
        required=True
    )
    description = fields.Text(
        string='Background Description',
        help='Background description of the patient.',
        required=True
    )
    type = fields.Selection(
        [('patho', 'Pathological'), ('hered', 'Hereditary')],
        string='Type',
        help='Background type.',
        required=True
    )

    # # Atomics
    # Integer
    # Float
    # Date
    # Datetime
    # Selection
    # Char
    # Text
    # Binary
    # Html

    # # Relationals
    # Many2one
    # One2many
    # Many2many

    # # Definition Arguments
    # string='Field name'
    # help='Help'
    # required=True | False
    # compute='method'
    # default='method'
    # ****************
    # comodel_name='model'
    # inverse_name='this_field_model'
