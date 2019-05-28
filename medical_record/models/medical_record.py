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

from ast import literal_eval

from odoo import api, fields, models, _


class MedicalRecord(models.Model):

    _name = 'medical.record'
    _description = 'Electronic version about medical records.'
    # mail.thread = Basic Chatter integration.
    # mail.activity.mixin = Basic Activity integration for chatter.
    _inherit = ['mail.thread', 'mail.activity.mixin']


    @api.model
    def _default_name(self):
        aux_name = False
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_auto_numbering = literal_eval(get_param(
            'medical_record.auto_numbering', default='False'))
        if not aux_auto_numbering:
            aux_auto_numbering = False
        if aux_auto_numbering:
            aux_name = self.env['ir.sequence'].next_by_code('medical.record.number')
        return aux_name

    name = fields.Char(
        string = "Record Number",
        help="Record Number.",
        default=_default_name
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Patient",
        help="Information about patient.",
        required=True
    )
    partner_email = fields.Char(
        related="partner_id.email"
    )
    partner_phone = fields.Char(
        related="partner_id.phone"
    )
    partner_mobile = fields.Char(
        related="partner_id.mobile"
    )
    partner_initial_name = fields.Char(
        string="Initial",
        help="Partner's name initial, example Tony = T.",
        compute="_compute_partner_initial_name",
        store=True
    )
    profile_image = fields.Binary(
        string="Patient photo",
        help="Patient photo.",
        related="partner_id.image"
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
    ses_ids = fields.One2many(
        comodel_name="medical.record.ses",
        inverse_name="record_id",
        string="SES",
        help="Social-Economic Studies about the patient."
    )
    group_ses = fields.Boolean(
        compute="_compute_group_ses"
    )
    auto_numbering = fields.Boolean(
        compute="_compute_auto_numbering"
    )

    @api.model
    def _compute_group_ses(self):
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_group_ses = literal_eval(get_param(
            'medical_record.group_group_ses', default='False'))
        if not aux_group_ses:
            aux_group_ses = False
        self.group_ses = aux_group_ses

    @api.model
    def _compute_auto_numbering(self):
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_auto_numbering = literal_eval(get_param(
            'medical_record.auto_numbering', default='False'))
        if not aux_auto_numbering:
            aux_auto_numbering = False
        self.auto_numbering = aux_auto_numbering

    @api.depends('partner_id.name')
    def _compute_partner_initial_name(self):
        for record in self:
            record.partner_initial_name = record.partner_id.name[0]
