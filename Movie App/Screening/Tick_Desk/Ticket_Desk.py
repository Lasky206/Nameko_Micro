from flask import Flask, render_template
from nameko.standalone.rpc import ClusterRpcProxy
import os

config = {
    'AMQP_URI': 'amqp://guest:guest@localhost:5672'
    # 'AMQP_URI': 'pyamqp://guest:guest@localhost'
}

app = Flask(__name__)


@app.route('/')
def home():
    with ClusterRpcProxy(config) as cluster_rpc:
        movies = cluster_rpc.show_time_service.get('Die Hard')
    return render_template(
        './home.html',
        value=movies,
    )


if __name__ == '__main__':
    app.run(debug=True)
