from flask import *
from flask_mysqldb import MySQL

class Workout(Flask):
    def __init__(self):
        self.app = Flask(__name__)
        super().__init__(__name__)

        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'pkonnoth'
        self.app.config['MYSQL_PASSWORD'] = '12345'
        self.app.config['MYSQL_DB'] = 'workout'

        self.mysql = MySQL(self.app)

        @self.route('/')
        def index():
            cur = self.mysql.connection.cursor()
            cur.execute("SELECT * FROM workout.users")
            users = cur.fetchall()
            cur.close()
            return render_template('index.html', users=users)

        @self.route('/login')
        def login():
            return render_template('index.html')

        @self.route('/register')
        def register():
            return render_template('register.html')

if __name__ == '__main__':
    app = Workout()
    app.run()
