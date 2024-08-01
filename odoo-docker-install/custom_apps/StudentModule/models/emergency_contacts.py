from odoo import models, fields

class EmergencyContact(models.Model):
    _name = 'school.emergency.contact'
    _description = 'Emergency Contact'

    name = fields.Char(string='Name', required=True)
    relationship = fields.Selection([
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('others', 'Others')
    ], required=True, default='others', string = "Relationship")
    phone = fields.Char(string='Phone Number', required=True)
    school_student_id = fields.Many2one(comodel_name='school.student', string='Student', ondelete='cascade')
    