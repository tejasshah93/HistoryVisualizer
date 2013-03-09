# coding: utf8
from plugin_rating_widget import RatingWidget

db.define_table('product',
    Field('created_by',default=auth.user_id,writable=False,readable=False),
	Field('event_id',db.history,default=db.history.id,writable=False,readable=False),
    Field('rating', 'integer',requires=IS_IN_SET(range(1, 6))),
    Field('average','double',writable=False,readable=False))

################################ The core ######################################
# Inject the horizontal radio widget
db.product.rating.widget = RatingWidget()
################################################################################
