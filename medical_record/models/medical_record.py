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


class MedicalRecord(models.Model):

    _name = 'medical.record'
    _description = 'Electronic version about medical records.'

    name = fields.Char(
        string = "Record Number",
        help="Record Number.",
        required=True
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Patient",
        help="Information about patient.",
        required=True
    )
    profile_image = fields.Binary(
        string = "Patient photo",
        attachment=True,
        help="Patient photo."
    )
    diagnosis = fields.Text(
        string = "Diagnosis",
        help="Diagnosis about the patient.",
        required=True
    )
    habit_ids = fields.One2many(
        comodel_name="medical.record.habit",
        inverse_name="record_id",
        string="Habits",
        help="Habit about the patient."
    )
    log_ids = fields.One2many(
        comodel_name="medical.record.log",
        inverse_name="record_id",
        string="Medical Logs",
        help="Medical Logs about the hospitals, "
             "clinics, medical centers, etcetera, "
             "that patient has passed."
    )
    background_ids = fields.One2many(
        comodel_name="medical.record.background",
        inverse_name="record_id",
        string="Backgrounds",
        help="Background about the patient."
    )

