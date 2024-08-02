# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Program(models.Model):
    _name = 'school.student.programs'
    _description = 'Student Programs'

    programid = fields.Integer(string='Program ID')
    programname = fields.Integer(string='Program')