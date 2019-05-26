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

class MedicalRecordHabit(models.Model):

    _name = 'medical.record.habit'
    _description = 'Habits that patients have to complete medical records, both alimentary, physical and hobbies.'

    name = fields.Char(
        string = "Habit",
        help='Habits of the patient.',
        required=True
    )
    description = fields.Text(
        string='Details',
        help='Habit description of the patient.',
    )
    type = fields.Selection(
        [('ali', 'Alimentary'), ('phy', 'Physical Activities'), ('hobb', 'Hobbies')],
        string='Type',
        help='Habit type.',
        required=True
    )
    record_id = fields.Many2one(
        comodel_name="medical.record",
        string="Medical Record",
        help="Medical record.",
        required=True
    )

    @api.model
    def getFormattedTextField(self, textField):
        return textField.replace("\n", "<br/>")

    @api.model
    def getSelectionValue(self, selection_name, selection_key):
        return dict(self._fields[selection_name].selection)[selection_key]
    