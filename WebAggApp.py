import matplotlib.pyplot as plt
import threading

def setup():
    from matplotlib.backends.backend_webagg import WebAggApplication
    from tornado.ioloop import IOLoop
    plt.show = lambda: None
    plt.switch_backend('webagg')
    plt.ion()
    app = WebAggApplication()
    app.listen(8080, address='0.0.0.0')
    t = threading.Thread(target=IOLoop.instance().start)
    t.daemon = True
    t.start()
setup()
