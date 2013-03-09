GOOGLEMAP_KEY='ABQIAAAAnfs7bKE82qgb3Zc2YyS-oBT2yXp_ZAY8_ufC3CFXhHIE1NvwkxSySz_REpPq-4WZA27OwgbtyR3VcA' # localhost
GOOGLEMAP_KEY='ABQIAAAAT5em2PdsvF3z5onQpCqv0RQKjFa1yJagLmzGcZ4UA6Ce9BDiWhSxvi4hSIQsWixy4LcFJtTrQTFuhg' # web2py.com

from plugin_rating_widget import RatingWidget

db.define_table('history',
Field('created_by',db.auth_user,default=auth.user_id,writable=False,readable=False),
Field('created_on','datetime',default=request.now,writable=False,readable=False),
Field('start_date','date'),
Field('end_date','date'),
Field('Title'),
Field('from_nickname',default=('%(first_name)s %(last_name)s' % auth.user) if auth.user else ''),
Field('from_location',requires=IS_NOT_EMPTY()),
Field('latitude','double',requires=IS_NOT_EMPTY()),
Field('longitude','double',requires=IS_NOT_EMPTY()),
Field('importance','integer'),
Field('image','upload'),
Field('comment','text'),
#Field('average','double',writable=False),
#Field('rating', 'integer',requires=IS_IN_SET(range(1, 6)))
)

#db.product.rating.widget = RatingWidget()