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
        'data/data.xml',
        'views/school_student.xml'
    ],

    'auto_install': False,
    'application': False,
    'assets': {
        
    }
}