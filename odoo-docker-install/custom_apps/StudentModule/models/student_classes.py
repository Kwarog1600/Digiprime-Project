# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student.programs'
    _description = 'Student Program List'

    programid = fields.Integer(string='ID')
    programname = fields.Char(string='Program Name')