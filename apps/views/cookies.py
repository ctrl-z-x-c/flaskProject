from flask import Blueprint,request,make_response,url_for,session
import requests



cookie = Blueprint('cookie',__name__,url_prefix='/cookie/')


@cookie.route('/get')
def get():
    print( request.cookies.get('user_pwd'))
    print(session)
    print( request.cookies.get('name'))
    # return  request.cookies.get('name','i am cookie')
    return  request.cookies.get('user_pwd','没有cookie')


@cookie.route('/set', methods=['GET', 'POST'])
def set():
    if request.method=='POST':
        data = dict(request.form)
        resp = make_response('cookie已设置')
        resp.set_cookie('user_pwd', data['name']+'123', max_age=30)
        requests.post('http://127.0.0.1:5000/sess/set',json={'user_pwd':data['name']+'123'})
        # return url_for()



    else:
        print(request.cookies.get('name'))
        resp=make_response('cookie已设置')
        resp.set_cookie('name','i am xxx',max_age=10)
        print(resp)
        print(request.cookies.get('name'))

        return resp


@cookie.route('/del')
def delete():
    resp=make_response('cookie已删除')
    resp.delete_cookie('name')
    return resp