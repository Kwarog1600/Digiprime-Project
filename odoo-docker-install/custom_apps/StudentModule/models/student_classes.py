# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student.programs'
    _description = 'Student Program List'

    subjectid = fields.Char(string='ID')
    subjecttitle = fields.Char(string='Subject Title')
    units = fields.Integer(string='Units')
    instructor = fields.Char(string='Instructor')
