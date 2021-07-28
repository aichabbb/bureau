# -*- coding: utf-8 -*-


{
    'name': "ia_site ",

    'summary': """  """,

    'description': """ """,

    'author': "itadvisor",
    'website': "http://www.itadvisor.ma",

    'category': 'Uncategorized',
    'version': '12.0.0.0.1',
    'depends': ['base', 'website','website_sale'],

    # any module necessary for this one to work correctly
    # 'depends': ['base', 'contacts', 'hr'],

    # always loaded
    'data': [

        'views/snippet.xml',
        'views/produit.xml',
        # 'static/scss/main.scss'


    ],
    'qweb': ['static/src/xml/*.xml'],

    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}
