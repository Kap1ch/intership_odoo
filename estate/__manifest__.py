{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Your Name',
    'category': 'Real Estate',
    'description': """
    A module for managing real estate properties.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_views_type.xml',
        'views/estate_property_views_tag.xml',
        'views/estate_property_views_offer.xml',
        'views/estate_menus.xml',
        'views/estate_property_actions.xml',

    ],
    'installable': True,
    'application': True,
}
