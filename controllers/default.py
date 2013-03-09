def index():
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select()
    myusers = db(db.allowed.usrid>0).select()
    return dict(postcards=postcards,myusers=myusers)

@auth.requires_login() 
def edit_event():
    record = db.history(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.history, record, deletable=True,
                  upload=URL('download'))
    if auth.user_id != record.created_by.id :
        response.flash = 'Not enough privileges'
    else:
        if form.process().accepted:
            response.flash = 'form accepted'
        elif form.errors:
            response.flash = 'form has errors'
    return dict(form=form,record=record)
        

def space1():   
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select() 
    return dict(postcards=postcards)  

def space_time():   
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select() 
    return dict(postcards=postcards)
    

@auth.requires_login() 
def longitude1():
    lat="23.456768"
    longt="103.35976"
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()
        #db.postcard.longitude.default=request.vars.lonbox
        #db.postcard.latitude.default=longt
        #form.vars.latitude.default = 'fieldvalue'      
       # form= crud.create(db.postcard,next=URL(r=request))
        #form.vars.latitude.default = 'fieldvalue'
        form = SQLFORM(db.history)
        if form.process(session=None, formname='test').accepted:
            response.flash = 'form accepted'
        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill the form'
       
    else:
        form = None    
    postcards = db(db.history.id>0).select()
    return dict(postcards=postcards)
def user():
    """
    exposes:
    http://..../[app]/default/user/login 
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the
{{left_sidebar_enabled,right_sidebar_enabled=False,True}}
{{=form}} functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

def timeline1():
 form=SQLFORM(db.history)
 if form.process().accepted:
    response.flash = 'your data is uploaded'
 data = db(db.history).select()
 return dict(form=form, data=data)
 
 
 
def check():
 return dict()

def about():
 return dict()

def trial():
    return dict()

def trial_result():
    return dict()

@auth.requires_login() 
def rating():
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select() 
    history = db.history(request.vars.query) or redirect(URL('index'))
    db.product.event_id.default = history.id
    form = SQLFORM(db.product)
    if form.accepts(request.vars, session):
        response.flash = 'Your rating has been recorded'
        #redirect(URL('rating')) 
    products = db(db.product.event_id==history.id).select() 
    return dict(form=form, postcards=postcards,products=products)

def ratinp():
    if auth.user:
        postcard = db(db.history.created_by==-1).select().first()    
    postcards = db(db.history.id>0).select()
    history = db.history(request.vars.query) or redirect(URL('index')) 
    db.product.event_id.default = history.id
    form = SQLFORM(db.product)
    if form.accepts(request.vars, session):
        response.flash = 'Your rating has been recorded' 
        redirect(URL('rating')) 
    products = db(db.product.event_id==history.id).select()
    return dict(form=form, postcards=postcards,products=products)

#@auth.requires_membership("admin")
def account_control():
    grid = SQLFORM.grid(db.auth_user)
    return locals()

#@auth.requires_membership("admin")    
def manage():
#    grid = SQLFORM.smartgrid(db.auth_user)
    grid1 = SQLFORM.smartgrid(db.history) 
    return dict(grid1=grid1)