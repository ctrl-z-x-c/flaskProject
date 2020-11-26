from flask import Blueprint,session,request
sess =Blueprint('sess',__name__,url_prefix='/sess/')

@sess.route('/set/',methods=['GET', 'POST'])
def set():
    if request.method=='POST':
        pass
    else:
        session.permanent=True
        session['name']='who are you'
        return 'session was setted'

@sess.route('/get/')
def get():
    return session.get('name','who are you?')

@sess.route('/del/')
def delete():
    session.clear()
    return 'session is deleted'