# -*- coding: utf-8 -*-
from plugin_rating_widget import RatingWidget

db = DAL('sqlite:memory:')
db.define_table('product',
    Field('created_by',default=auth.user_id,writable=False,readable=False),
    Field('event_id',db.history,default=db.history.id),
    Field('rating', 'integer',requires=IS_IN_SET(range(1, 6))),
    Field('average','double',writable=False))

################################ The core ######################################
# Inject the horizontal radio widget
db.product.rating.widget = RatingWidget()
################################################################################


def rating():
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select() 
    form = SQLFORM(db.product)
    if form.accepts(request.vars, session):
        session.flash = 'Your rating has been recorded'
        redirect(URL('rating')) 
    products = db(db.product.id>0).select() 
    return dict(form=form, postcards=postcards,products=products)
