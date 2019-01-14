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

class MedicalRecordLog(models.Model):

    _name = "medical.record.log"
    _description = "Logs are records that have in count place, medical employees and another data about patient's medical situation."
    
    name = fields.Char(
        string="Summary",
        help="Brief description about the entry in the history.",
        required=True
    )
    details = fields.Char(
        string="Details",
        help="Details about the entry in the history."
    )
    start_datetime = fields.Datetime(
        string="Start of the stay",
        help="Start of the stay in medical place.",
        required=True
    )
    end_datetime = fields.Datetime(
        string="End of the stay",
        help="End of the stay in medical place.",
        required=True
    )
    medical_employee = fields.Char(
        string="Medical Employee",
        help="Medical Employee"
    )
    place_id = fields.Many2one(
        comodel_name="medical.record.place",
        string="Place",
        help="Place where stayed the patience.",
        required=True
    )
    log_type_id = fields.Many2one(
        comodel_name="medical.record.log.type",
        string="Log Type",
        help="Log Type (example: Medical appointment, Surgical operation, Therapy).",
        required=True
    )
    record_id = fields.Many2one(
        comodel_name="medical.record",
        string="Medical Record",
        help="Medical record.",
        required=True
    )
