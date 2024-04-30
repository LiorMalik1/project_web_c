from flask import render_template, Blueprint, session, request, jsonify, redirect


import db_connector

# Home_Page blueprint definition
homePage = Blueprint(
    'homePage',
    __name__,
    static_folder='static',
    static_url_path='/homePage',
    template_folder='templates'
)

@homePage.route('/')
@homePage.route('/homePage')
def index():
    # got here from pressing logout
    if request.args.get('logout') or session.get('user') is None:
        # 'log out the user'
        session.clear()

    if "user" in session:
        # user is logged in: user & businesses data exists in seesions
        user = session.get('user')
        username = user["username"]
    else:
        # user is not logged in: user & businesses data dosen't exists in seesions
        session["businesses"] = db_connector.get_all_businesses()
        username = None

    return render_template('homePage.html', username=username)
