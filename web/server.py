from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import socket
from parse.schedule_parser import ScheduleParser

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        match_list = '<h3>User: ' + session['username'] + '</h3>'
        for x in range(1, 10):
            sp = ScheduleParser(x)
            for m in sp.get_matches():
                team_one_btn = '<button class="team-one-btn" type="button">' + m.team_one.name + '</button>'
                team_two_btn = '<button class="team-two-btn" type="button">' + m.team_two.name + '</button>'
                match_list += '<div id="' + 'match-' + str(m.match_id) + '" class="match-btn-group">' + str(m.match_id)\
                              + ': ' + team_one_btn + 'vs' + team_two_btn + '</div>'

        return render_template('index.html') + match_list + '<a href="/logout">Logout</a>'


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'].lower() == 'backman' and request.form['username'].lower() == 'pontus':
        session['username'] = request.form['username']
        session['logged_in'] = True
        return home()
    else:
        flash('wrong password!')
        return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


# TODO Implement leaderboard!
@app.route('/leaderboard')
def leaderboard():
    return 'Leaderboard: #1 Pontus'


if __name__ == '__main__':
    app.secret_key = os.urandom(16)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    app.run(host=s.getsockname()[0])
    s.close()
