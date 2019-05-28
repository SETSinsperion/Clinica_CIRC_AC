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
from odoo.exceptions import UserError


class ResPartner(models.Model):

    _inherit = 'res.partner'

    age = fields.Float(
        string="Age",
        help="Partner's age. For more specific data, try to fill years & months\n"
             "(digits to the right of the decimal point).",
        digits=(5,2)
    )

    @api.onchange('age')
    def _onchange_age(self):
        scale = int(('%s' % self.age).split('.')[1])
        if scale > 11:
            # If the user typed .12, it means that age should increase +1
            if scale == 12:
                self.age = round(self.age) + 1
            else:
                raise UserError(_('There are 12 months in a single year, please type a valid age\n(you typed %s months).') % scale)
