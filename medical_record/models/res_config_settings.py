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

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'

    group_group_ses = fields.Boolean(
        string="Is SES required?",
        implied_group='medical_record.group_ses',
        help="Social-Economic Studies required for your Records, otherwise won't be at them."
    )
    auto_numbering = fields.Boolean(
        string="Auto-Numbering for Records",
        help="Records will have auto-numbering (see <i>medical_record_number</i> sequence)."
    )

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        # we store the repr of the values, since the value of the parameter is a required string
        set_param('medical_record.group_group_ses', repr(self.group_group_ses))
        set_param('medical_record.auto_numbering', repr(self.auto_numbering))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_group_group_ses = literal_eval(get_param(
            'medical_record.group_group_ses', default='False'))
        aux_auto_numbering = literal_eval(get_param(
            'medical_record.auto_numbering', default='False'))
        if not aux_group_group_ses:
            aux_group_group_ses = False
        if not aux_auto_numbering:
            aux_auto_numbering = False
        # the value of the parameter is a nonempty string
        res.update(
            group_group_ses=aux_group_group_ses,
            auto_numbering=aux_auto_numbering,
        )
        return res
