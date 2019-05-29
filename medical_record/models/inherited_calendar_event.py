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


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    record_id = fields.Many2one(
        comodel_name="medical.record",
        string="Medical Record",
        help="Medical record."
    )

    @api.onchange('partner_ids')
    def _onchange_partner_ids(self):
        for partner in self.partner_ids:
            aux_record_id = self.env['medical.record'].search([
                ('partner_id', '=', partner.id)
            ])
            if aux_record_id:
                self.record_id = aux_record_id
                break
