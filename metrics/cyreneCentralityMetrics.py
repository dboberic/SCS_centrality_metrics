#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 23:24:33 2021

@author: danijelab
"""

import networkx as nx
import collections
import numpy as np

class GraphMetrics:
    
    def __init__(self, edges, metric):
        self.edges = edges
        self.metric = metric
    
    def createGraph(self):
        graphtype = nx.DiGraph()
        G = nx.parse_edgelist(self.edges,create_using=graphtype,nodetype=str,data=(('weight', float),))
        edges = G.edges()
        dict={}
        for e in edges:
            dict[e] = 0
            for n1 in G.nodes():
                for n2 in G.nodes():
                    if n1==n2:
                        continue
                    else:
                        for path in nx.all_simple_paths(G, source=n1, target=n2):
                            for i in range(0,len(path)):
                                try:
                                    temp = (path[i], path[i+1])
                                    dict[temp] += 1
                                except:
                                    print()
        NG = nx.DiGraph()
        for i in dict:
            NG.add_edge(i[0], i[1], weight=dict.get(i))
        g_distance_dict = {(e1, e2): 1 / weight for e1, e2, weight in NG.edges(data='weight')}
        nx.set_edge_attributes(NG, g_distance_dict, 'distance')
        NG = NG.to_directed()    
        return NG
    
    def sortDictionary(self,res):
        sorted_x = sorted(res.items(), key=lambda kv: kv[1],reverse=True)
        sorted_dict = collections.OrderedDict(sorted_x)
        return sorted_dict
    
    def transform(self,res):
        resultList = []
        for k in res:
            newJson = {}
            newJson['assetId'] = k
            newJson['metric'] = res[k]
            resultList.append(newJson)
        return resultList;  
    
    def run(self):
        G = self.createGraph();
 
        if self.metric == 'PR':
            calculatedMetric=nx.pagerank(G)
            resultDict = self.sortDictionary(calculatedMetric)
            res = self.transform(resultDict)
            #with open('pageRankMetricCyrene.json', 'w') as outfile:
            #   json.dump(res, outfile)
            return res
        if self.metric == 'CL':
            calculatedMetric=nx.closeness_centrality(G,distance='weight')
            resultDict = self.sortDictionary(calculatedMetric)
            res = self.transform(resultDict)
            return res
        if self.metric == 'BT':
            calculatedMetric=nx.betweenness_centrality(G,normalized=False, weight='weight')
            resultDict = self.sortDictionary(calculatedMetric)
            res = self.transform(resultDict)
            return res
        if self.metric == 'EG':
            calculatedMetric = nx.eigenvector_centrality (G, max_iter=1000,weight='weight')
            resultDict = self.sortDictionary(calculatedMetric)
            res = self.transform(resultDict)
            return res
        if (self.metric == 'HITH') or (self.metric == 'HITA'):
            calculatedMetric = nx.hits(G,normalized=False)
            if self.metric == 'HITH':
                resultDict = self.sortDictionary(calculatedMetric[0])
                res = self.transform(resultDict)
                return res
            if self.metric == 'HITA':
                resultDictAuth = self.sortDictionary(calculatedMetric[1])
                res = self.transform(resultDictAuth)
                return res
                

    