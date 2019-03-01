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
{
    'name' : 'Medical Records',
    'author': 'INSPERION',
    'version' : '1.0',
    'summary': 'Medical Records for CIRC A.C Clinic',
    'sequence': 100,
    'description': """
INSPERION | Medical Records
===========================

Medical Records for CIRC A.C Clinic
-----------------------------------

    """,
    'category': 'Sales Management',
    'website': 'https://www.facebook.com/InsperionInYourWorld/',
    'depends' : [
        'base',
        'web',
        'contacts',
        'hr'
    ],
    'data': [
        'security/medical_record_security.xml',
        'security/ir.model.access.csv',
        'views/web_assets.xml',
        'views/medical_record_views.xml',
        'views/medical_record_actions.xml',
        'views/medical_record_menus.xml'
    ],
    'demo': [
        'data/medical_record_data.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}