from workoutapp import Workout
from flask_mysqldb import MySQL

class MySqlFunctions:
    def(__init__)(self):
        self.mysql = MySQL()
        self.mysql.init_app(self)

