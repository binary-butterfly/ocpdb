# encoding: utf-8

from time import sleep
from flask_failsafe import failsafe


@failsafe
def create_app():
    from webapp import launch
    return launch()


if __name__ == "__main__":
    sleep(10)
    create_app().run(debug=True, host='0.0.0.0', use_reloader=True)
