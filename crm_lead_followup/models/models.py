# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime

class CRMLeadFollowUP(models.Model):
    _name = 'crm_lead.follow_up'

    name = fields.Char(string="Name", required=1)


class CRMLeadCust(models.Model):
    _inherit = 'crm.lead'

    first_follow_up = fields.Many2one(comodel_name="crm_lead.follow_up", string="Follow up 1", tracking=True)
    second_follow_up = fields.Many2one(comodel_name="crm_lead.follow_up", string="Follow up 2", tracking=True)
    third_follow_up = fields.Many2one(comodel_name="crm_lead.follow_up", string="Follow up 3", tracking=True)
    first_follow_up_date = fields.Datetime(string="Follow up Date 1", tracking=True, readonly=1)
    second_follow_up_date = fields.Datetime(string="Follow up Date 2", tracking=True, readonly=1)
    third_follow_up_date = fields.Datetime(string="Follow up Date 3", tracking=True, readonly=1)
    follow_upstate = fields.Selection(string="Follow Up State", selection=[('processing', 'جاري المتابعة'), ('done', 'تم')], tracking=True)

    @api.constrains('first_follow_up')
    def check_first_follow_up(self):
        for rec in self:
            if rec.first_follow_up:
                rec.first_follow_up_date = datetime.now()
                rec.follow_upstate = 'processing'

    @api.constrains('second_follow_up')
    def check_second_follow_up(self):
        for rec in self:
            if rec.second_follow_up:
                rec.second_follow_up_date = datetime.now()
                rec.follow_upstate = 'processing'

    @api.constrains('third_follow_up')
    def check_third_follow_up(self):
        for rec in self:
            if rec.third_follow_up:
                rec.third_follow_up_date = datetime.now()
                rec.follow_upstate = 'processing'

