

from ast import literal_eval

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'

    require_ses = fields.Boolean(
        string="Is SES required?",
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
        set_param('medical_record.require_ses', repr(self.require_ses))
        set_param('medical_record.auto_numbering', repr(self.auto_numbering))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param =  self.env['ir.config_parameter'].sudo().get_param
        aux_require_ses = literal_eval(get_param(
            'medical_record.require_ses', default='False'))
        aux_auto_numbering = literal_eval(get_param(
            'medical_record.auto_numbering', default='False'))
        if not aux_require_ses:
            aux_auto_numbering = False
        if not aux_auto_numbering:
            aux_auto_numbering = False        
        # the value of the parameter is a nonempty string
        res.update(
            require_ses=aux_require_ses,
            auto_numbering=aux_auto_numbering,
        )
        return res
