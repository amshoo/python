
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()
#fh=open("DataSet/usair.txt", 'rb')
#G = nx.read_weighted_edgelist(fh,nodetype=None, encoding='utf-8')
#fh.close()


H = nx.convert_node_labels_to_integers(G, first_label=0, ordering="default", label_attribute = None)

def drw_graph():
    nx.draw(H, data=True)
    draw = plt.show()
    return draw