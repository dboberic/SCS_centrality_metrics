from flask import Flask, request,jsonify
from metrics import cyreneCentralityMetrics as scm

app = Flask(__name__)


@app.route('/centrality_metrics/<metric>', methods=['POST'])
def getMetric(metric):
    edges_list = request.json['Edges']
    edges = [str(edges_list[i]['Child']) + " " + str(edges_list[i]['Parent']) + " " + "1" for i in
             range(0, len(edges_list))]
    cyrene = scm.GraphMetrics(edges, metric)
    res = cyrene.run()
    return jsonify(res)


if __name__ == '__main__':
    app.run()
