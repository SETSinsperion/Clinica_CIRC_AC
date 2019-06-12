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
from odoo.exceptions import ValidationError


class MedicalRecord(models.Model):

    _name = 'medical.record'
    _description = 'Electronic version about medical records.'
    _rec_name = 'number'
    # mail.thread = Basic Chatter integration.
    # mail.activity.mixin = Basic Activity integration for chatter.
    _inherit = ['mail.thread', 'mail.activity.mixin']


    @api.model
    def _default_number(self):
        aux_name = False
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_auto_numbering = literal_eval(get_param(
            'medical_record.auto_numbering', default='False'))
        if not aux_auto_numbering:
            aux_auto_numbering = False
        if aux_auto_numbering:
            auto_numbering_seq = self.env.user.company_id.seq_auto_numbering_id
            if auto_numbering_seq:
                aux_name = self.env['ir.sequence'].next_by_code(auto_numbering_seq.code)
            else:
                raise ValidationError(_("There isn't an auto-numbering sequence. Please request a Manager\n"
                    "to set it on Settings > Auto-Numbering Sequence."))
        return aux_name

    number = fields.Char(
        string = "Record Number",
        help="Record Number.",
        default=_default_number
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
        help="Backgrounds about the patient."
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
    calendar_event_ids = fields.One2many(
        comodel_name="calendar.event",
        inverse_name="record_id",
        string="Appointments",
        help="Appointments for patient on this record."
    )
    calendar_event_count = fields.Integer(
        string="Appointments Count",
        help="Appointments Count for patient on this record.",
        compute="_compute_calendar_event_count"
    )

    _sql_constraints = [
        # A patient CAN'T HAVE > 1 record
        ('partner_id_unique', 'unique(partner_id)', 'The partner has a medical record yet!'),
        ('number_unique', 'unique(number)', 'This number has been used in another medical record yet!')
    ]

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
        self.auto_numbering = True if aux_auto_numbering else False

    @api.depends('partner_id.name')
    def _compute_partner_initial_name(self):
        for record in self:
            record.partner_initial_name = record.partner_id.name[0].upper()

    @api.depends('calendar_event_ids')
    def _compute_calendar_event_count(self):
        for record in self:
            record.calendar_event_count = len(record.calendar_event_ids)

    @api.multi
    def do_open_record_events(self):
        action = {
            'name': _('Appointments'),
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'calendar,tree,form',
            'target': 'new',
            'domain': [('record_id', '=', self.id)],
        }
        return action

    @api.model
    def get_print_medical_record_name(self):
        return _('Medical Record %s%s%s') % (
            self.number if self.number else '',
            ' ' if self.number else '',
            self.partner_id.name
        )
