# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Model'

    studentId = fields.Char(string='Student ID', required=True)
    surname = fields.Char(string='Surname', required=True)
    firstname = fields.Char(string='First Name',required=True)
    midname = fields.Char(string='Middle Name')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], required=True, default='others')
    birthdate = fields.Date(string="Birthdate", required=True)
    birthplace = fields.Char(string = "Place of Birth")
    age = fields.Integer(string='Age', compute='_compute_age')
    photo = fields.Binary(string='Photo', attachment=True)

    em_contact = fields.One2many(comodel_name='school.emergency.contact', inverse_name='school_student_id', string='Emergency Contact')
    
    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                birth_date = fields.Date.from_string(record.birthdate)
                today = fields.Date.context_today(record)
                age = today.year - birth_date.year
                if (today.month, today.day) < (birth_date.month, birth_date.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0