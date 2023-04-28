from flask import Flask, render_template


class Workout(Flask):
    def __init__(self):
        super().__init__(__name__)


        @self.route('/')
        def index():
            return render_template('index.html')

        @self.route('/register')
        def register():
            return render_template('register.html')
def main():
    app = Workout()
    app.run()


if __name__ == '__main__':
    main()

