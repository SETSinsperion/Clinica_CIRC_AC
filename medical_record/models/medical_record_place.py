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

class MedicalRecordPlace(models.Model):

    _name = "medical.record.place"
    _description = "Places in medical records are clinics, hospitals, mdical centers, etc."

    name = fields.Char(
        string="Name",
        help="Name of the medical place.",
        required=True
    )
    street = fields.Char(
        string="Street",
        help="Stree.t",
        required=True
    )
    street2 = fields.Char(
        string="Reference Street",
        help="Reference Street."
    )
    ext_number = fields.Char(
        string="Ext. Number",
        help="External Number of the place.",
        required=True
    )
    int_number = fields.Char(
        string="Int. Number",
        help="Internal Number of the place."
    )
    city = fields.Char()
    state_id = fields.Many2one(
        comodel_name="res.country.state",
        string='State',
        ondelete='restrict'
    )
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        ondelete='restrict'
    )
    phone = fields.Char(
        string="Phone",
        help="Phone Number of the place."
    )
    email = fields.Char(
        string="Email",
        help="General email for contact of the place."
    )
    website = fields.Char(
        string="Website",
        help="Website of the place."
    )
    social_mediums_info = fields.Text (
        string="Social Media",
        help="social Media information for contact (if any)."
    )
