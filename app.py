from flask import  session,abort,flash, Flask, render_template, redirect, url_for, render_template_string, Markup, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_mail import Message,Mail
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, login_url
from sqlalchemy import exc
import os
import re
import json
from datetime import timedelta, datetime
import load_anime_to_html
import generate_SGD
import random
import pickle

from animate_initalizing import remove_windows_key_word
import pandas as pd
import email_validator


def createFolder(directory):
    # create windows file
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['SECRET_KEY'] = 'aptxrga932#$mo!tu34we445th67#fr(*sa)su'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(hours=1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mail = Mail(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    # note the user id start with 1 here
    id = db.Column(db.Integer,  primary_key=True, )
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    iconUrl = db.Column(db.String(2048))

current_path = os.getcwd()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():

    session['next'] = request.url   # use to redirect user back to the pacge after they log in
    return redirect(url_for('login'))


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class VerifyEmailForm(FlaskForm):
    verificationCode = StringField('verification code', validators=[ Length(min=4, max=4)])

def generate_verification_code():
    password_length = 4
    possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    random_character_list = [random.choice(possible_characters) for i in range(password_length)]
    random_password = "".join(random_character_list)
    return random_password

def is_valid_email(form, field):
    if (re.fullmatch("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)", field.data) != None) == False:
        raise ValidationError("This is not an valid email address")

def exist_email(form, field):
    if isinstance(form, RegisterForm):
        if User.query.filter_by(email=field.data).first() != None:
            raise ValidationError("This email was registered already")
    elif isinstance(form, FogetPasswordForm):
        if User.query.filter_by(email=field.data).first() == None:
            raise ValidationError("This email is not currently registered in the system")

def get_id_by_email(form, field):
    if User.query.filter_by(email=field.data).first() == None:
        raise ValidationError("This email is not register in the system")

def exist_username(form, field):
    if User.query.filter_by(username=field.data).first() != None:
        raise ValidationError("This username was registered already")

def verify_password(form, field):
    if field.data == form.password.data:
        pass
    else:
        raise ValidationError("The password is not equal to each other")

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50), exist_email, is_valid_email])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15), exist_username])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    repassword = PasswordField('verify password', validators=[InputRequired(), Length(min=8, max=80), verify_password])

class SafequestionForm(FlaskForm):
    #email = StringField('Please enter the email you used to register', validators=[InputRequired(), Length(max=50), exist_email])
    favorite_anime = StringField('You favorite anime show', validators=[InputRequired(), Length( max=80)])
    favorite_animecharacter = StringField('You favorite anime character', validators=[InputRequired(), Length(max=80)])
    favorite_country = StringField("The country you wish to travel in the future", validators=[InputRequired(), Length(max=80)])

class SafequestionanswerForm(FlaskForm):
    email = StringField('Please enter the email you used to register', validators=[InputRequired(), Length(max=50), exist_email])
    favorite_anime = StringField('You favorite anime show', validators=[InputRequired(), Length( max=80)])
    favorite_animecharacter = StringField('You favorite anime character', validators=[InputRequired(), Length(max=80)])
    favorite_country = StringField("The country you wish to travel in the future", validators=[InputRequired(), Length(max=80)])

class FogetPasswordForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Email(message='Invalid email'), Length(max=50),exist_email, is_valid_email])

class ChangepasswordForm(FlaskForm):
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    repassword = PasswordField('verify password', validators=[InputRequired(), Length(min=8, max=80), verify_password])

def send_email_message(email:str, type:str):
    if type == "newuser":
        msg = Message('Verification code', sender="from@example.com", recipients=[email])
        msg.html = """
                           <b>Welcome to Anime Recommendation</b>
    
                           <p> You are reciving this email because we received an registration request on animerecommendation.
                           Here is your verification code:
                           <b>{}. 
                           Ps: Please ignore this message if your did not register the email at our website.</b></p>""".format(
            session['verificationcode'])
        mail.send(msg)
    elif type == 'olduser':
        # means he is trying to find password back
        msg = Message('Verification code', sender="from@example.com", recipients=[email])
        msg.html = """
                                   <b>Welcome to Anime Recommendation</b>

                                   <p> Hello dear user,
                                   Here is your verification code:
                                   
                                   {}. 
                                   Ps: Please ignore this message if your did not register the email at our website.</p>""".format(
            session['verificationcode'])
        mail.send(msg)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # html_message is the search result in html style
    if request.form["searchWord"] != "":
        searchResult = load_anime_to_html.generate_search_result(request.form["searchWord"])
        html_message = load_anime_to_html.write_to_html_form( searchResult )
    else:

        html_message = ""

    return render_template('search.html', html_message=Markup(html_message))



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                if "next" in session:

                    next_url = session["next"]  # gotten from login_manage.unauthorize_handler
                    session.pop('next', None)
                    return redirect(next_url)


                return redirect(url_for('dashboard'))


        flash('Invalid username or password')
        return render_template('login.html', form=form)
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['verificationcode'] = generate_verification_code()
        session['action'] = "verifyEmail"
        send_email_message(session['email'], "newuser")

        return redirect(url_for('confirmVerificationCode'))

    return render_template('signup.html', form=form)


@app.route('/verifycode', methods=['GET', 'POST'])
def confirmVerificationCode():
    form = VerifyEmailForm()
    #print(request.form)

    if form.validate_on_submit():

        if 'action' in session and session['action'] == "verifyEmail":

            if form.verificationCode.data == session['verificationcode']:
                hashed_password = generate_password_hash(session['password'], method='sha256')
                new_user = User(username=session['username'], email=session['email'], password=hashed_password, iconUrl="")
                try:

                    db.session.add(new_user)
                    db.session.commit()
                    # use id for each user folder name
                    user_folder = os.path.join(current_path, "user_data", str(new_user.id))

                    createFolder(user_folder)

                    # initalize user k, see more in modified&generate SGD
                    inital_value = {}
                    with open(os.path.join(os.getcwd(), "genres.json"), "r") as f:
                        genre = json.loads(f.read())
                    for x in genre:
                        inital_value[x] = 2.5
                    inital_value["bias"] = 0

                    """
                    with open(os.path.join(current_path, "user_data", str(new_user.id), "info.json"), "w") as file:
                        file.write(json.dumps(inital_value))
                    """

                    # a list of dictionary for each user genre (k)
                    if os.path.exists(os.path.join(current_path, "data_collection", "userGenres.pickle")) == False:
                        with open(os.path.join(current_path, "data_collection", "userGenres.pickle"),"wb") as f:
                            userGenres = []
                            userGenres.append(inital_value)
                            pickle.dump(userGenres, f)

                    else:
                        # means exist before
                        with open(os.path.join(current_path, "data_collection", "userGenres.pickle"),"rb") as f:
                            userGenres = pickle.load(f)
                        userGenres.append(inital_value)
                        with open(os.path.join(current_path, "data_collection", "userGenres.pickle"),"wb") as file:
                            pickle.dump(userGenres, file)
                    session.pop('action', None)
                    session.pop('password', None)
                    session.pop('username', None)
                    session.pop('email', None)
                    session.pop('verificationcode', None)

                    return redirect(url_for('login'))
                except exc.IntegrityError:
                    # means unknow error while trying to write back to the database
                    db.session.rollback()
                    return '<h1>Error</h1>'
            else:
                flash("incorrect verification code")
                return render_template("verificationcode.html", form=form)

        elif 'action' in session and session['action'] == "changepassword":
            if session['verificationcode'] == form.verificationCode.data:

                session.pop('verificationcode', None)
                
                return redirect(url_for('changepassword'))

            elif session['verificationcode'] != form.verificationCode.data:
                flash("incorrect verification code")
                return render_template("verificationcode.html", form=form)


        else:
            # means user inten
            abort(401)
    elif 'resend' in request.form:
        # user request to resend a new verification code
        # first change the verification code
        session['verificationcode'] = generate_verification_code()
        send_email_message(session['email'], "newuser")
        flash("The code was resend. Note: an email may take couple minutes in order to appear in your account")
        return render_template("verificationcode.html", form=form)

    else:
        return render_template("verificationcode.html", form=form)


@app.route('/forgetpassword', methods=['GET', 'POST'])
def forgetpassword():
    form = FogetPasswordForm()

    if form.validate_on_submit():
        session['action'] = 'changepassword'
        session['verificationcode'] = generate_verification_code()
        session['email'] = form.email.data
        send_email_message(form.email.data, 'olduser')
        # got to verify user through email
        return redirect(url_for('confirmVerificationCode'))
    else:
        return render_template('forgetpassword.html', form=form)

@app.route('/changepassword', methods=['GET', 'POST'])
def changepassword():
    form = ChangepasswordForm()

    if form.validate_on_submit():

        if 'action' in session and session['action'] == 'changepassword':
            user = User.query.filter_by(email=session['email']).first()
            user.password = generate_password_hash( form.password.data, method ="sha256")
            db.session.commit()
            session.pop('email', None)
            session.pop('action', None)

            return redirect(url_for('login'))
        else:
            return """<h2> You do not have access to this page</h2>"""

    else:
        return render_template('changepassword.html', form=form)


@app.route('/changeicon', methods=['GET', 'POST'])
@login_required
def changeIcon():
    # this icon is the user icon a their dashbroad

    if "iconUrl" in request.form:
        user = User.query.filter_by(id=current_user.id).first()
        user.iconUrl = request.form["iconUrl"]
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        abort(401) # means not found, might cause by manual enter url

@app.route('/dashboard')
@login_required
def dashboard():
    iconUrl = User.query.filter_by(id=current_user.id).first().iconUrl
    return render_template('dashboard.html', name=current_user.username, iconUrl=iconUrl)


# dynamic route
@app.route('/encyclopedia/')
@app.route('/encyclopedia/<type>')
def encyclopedia_type(type=""):
    if type == 'other':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_other_list_panda())
    elif type == 'a':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_a_list_panda())
    elif type == 'b':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_b_list_panda())
    elif type == 'c':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_c_list_panda())
    elif type == 'd':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_d_list_panda())
    elif type == 'e':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_e_list_panda())
    elif type == 'f':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_f_list_panda())
    elif type == 'g':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_g_list_panda())
    elif type == 'h':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_h_list_panda())
    elif type == 'i':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_i_list_panda())
    elif type == 'j':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_j_list_panda())
    elif type == 'k':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_k_list_panda())
    elif type == 'l':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_l_list_panda())
    elif type == 'm':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_m_list_panda())
    elif type == 'n':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_n_list_panda())
    elif type == 'o':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_o_list_panda())
    elif type == 'p':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_p_list_panda())
    elif type == 'q':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_q_list_panda())
    elif type == 'r':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_r_list_panda())
    elif type == 's':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_s_list_panda())
    elif type == 't':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_t_list_panda())
    elif type == 'u':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_u_list_panda())
    elif type == 'v':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_v_list_panda())
    elif type == 'w':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_w_list_panda())
    elif type == 'x':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_x_list_panda())
    elif type == 'y':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_y_list_panda())
    elif type == 'z':
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.return_z_list_panda())
    elif type == "":
        return render_template('encyclopedia.html', html_message="")
    else:
        print("accessed")
        abort(404)

    return render_template('encyclopedia.html', html_message=Markup(html_message))
    return render_template('encyclopedia_template.html', html_message=Markup(html_message))


# dynamic route
@app.route('/genre/<type>')
def genre_type(type):

    with open(os.path.join(os.getcwd(), "genres.json")) as f:
        genres = json.loads(f.read())
    if type in genres:
        html_message = load_anime_to_html.write_to_html_form(load_anime_to_html.generate_genre_search_result(type))
        return render_template('encyclopedia.html', html_message=Markup(html_message))
    else:
        abort(404)


    #return render_template('encyclopedia_template.html', html_message=Markup(html_message))




@app.route('/viewdetail/<id>', methods=['POST', 'GET'])
@login_required
def view(id):

    #category = (request.form.get('filecategory'))
    #showname = (request.form.get('showname'))

    # getting the id of this anime from the html
    if id.isdigit() == False:
        # check to see if the id is a integer
        # it might not be a integer, if user input a improper dynamic url
        return abort(404)
    elif os.path.exists(os.path.join(os.getcwd(), "anime_data", str(id))) == False:
        abort(404)
    else:
        animeId = int(id)


    if "ratingScore" in request.form:
        # when the user just gave a rating
        #print(request.form.get("ratingScore"), request.form.get("comment"))
        userId = current_user.id
        ratingScore = request.form.get("ratingScore")
        comment = request.form.get("comment")
        now = datetime.now()
        time = now.strftime("%m/%d/%Y")
        load_anime_to_html.update_userRating(userId, animeId, ratingScore, comment, time)

    path = load_anime_to_html.load_viewdetail_file(animeId)
    #print(current_user.id)
    if path == "error":
        # this happens when the id is not exist in the file
        return abort(404)
    else:
        title, image, otherTitle, genre, plot, rating, episode, vintage, openingTheme, endingTheme, types = load_anime_to_html.write_to_detailview_htmlform(path, current_user.id, animeId)


    return render_template("detailview.html", title=Markup(title),
                           types = Markup(types),
                            image=Markup(image),
                            alternative_title=Markup(otherTitle),
                            genre=Markup(genre),
                            plot=Markup(plot),
                            rating=Markup(rating),
                            episode=Markup(episode),
                            vintage=Markup(vintage),
                            opening_theme=Markup(openingTheme),
                            ending_theme=Markup(endingTheme))




@app.route('/recommendation', methods=['POST', 'GET'])
@login_required
def personalize_recommendation():
    userId = current_user.id
    SGDcarousel, averageRatingCarousel = load_anime_to_html.generate_recommend_carousel(
        generate_SGD.apply_SGD(userId))

    return render_template("recommendation.html", carousel_SGD=Markup(SGDcarousel), carousel_averageRating=Markup(averageRatingCarousel))



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(debug=True)
