{
    'name': 'Student Module',
    'version': '14.0',
    'summary': "Manage school students and courses",
    'description': """
        A module to manage students and courses in a school.
    """,
    'sequence' : '1',
    'author': 'Digiprime Charyd',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    
    'data' : [
        'security/ir.model.access.csv',
        'views/school_student.xml',
        'report/report_details_template.xml',
        'report/student_report.xml'
    ],

    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}