#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# In[2]:


import Tr_centrality_measure
import Graph_Entropy_measure
import Selection_Algorithm
import Constraint_Coefficient


# In[3]:


TC_table = pd.DataFrame(Tr_centrality_measure.TC_Rank, columns = ('nodes_TC','TC_i'))
PI_table = pd.DataFrame(Graph_Entropy_measure.PI_Rank, columns = ('nodes_PI','PI_i'))
CC_table = pd.DataFrame(Constraint_Coefficient.sorted_x, columns = ('nodes_CC','CC_i'))
#CC_table.nodes_cc = CC_table.nodes_cc + 1
Result_table = pd.concat([TC_table, PI_table, CC_table], axis=1, sort=False)

First_Five= pd.DataFrame(Result_table.loc[0:4])
First_Five.index = First_Five.index + 1


# In[4]:


#return the total power of node i.
def TPN(i):
    PI_i = Graph_Entropy_measure.PI_of(i)
    TC_i = Tr_centrality_measure.TC_of(i)
    CC_i = Constraint_Coefficient.CC_of(i)
    #Weight to normalize the measures
    n1=TC_i/TC_i+PI_i+CC_i
    n2=PI_i/TC_i+PI_i+CC_i
    n3=CC_i/TC_i+PI_i+CC_i
    #equation []
    TPN_i  = (n1*TC_i)+(n2*PI_i)+(n3*CC_i)    
    
    return TPN_i


# In[33]:


#loop total power of node all i
def loop_TPN():
    i=0
    nodes = list(pd.concat([First_Five['nodes_TC'], First_Five['nodes_PI'], First_Five['nodes_CC']]).unique())
    list_TPN=[]    
    for i in nodes:          
        TPN_ = TPN(i)
        i_TPN = [i, TPN_]
        list_TPN.append(i_TPN)  
            
    return  list_TPN


# In[34]:


#Ranking the total power of node i
def TPN_Ranking( val ):
      return val [1]

TPN_Rank = loop_TPN()
TPN_Rank.sort(key=lambda elem: elem[1])


# In[35]:


#return table containing the TPN values[TPN_table and Top_Five]
TPN_table = pd.DataFrame(TPN_Rank, columns = ('nodes_TPN','TPN_i'))
Top_Five = pd.DataFrame(TPN_table.loc[0:4])
Top_Five.index = Top_Five.index + 1
#print(Top_Five)
#TPN_table.to_csv('result/TPN_[]_network.csv')
#Top_Five.to_csv('result/TPN_[]_network.csv')


# In[54]:


#return table containing ALL the Measures
Propose_Result_table = pd.concat([TC_table, PI_table, CC_table, TPN_table], axis=1, sort=False)
Top_Five = pd.DataFrame(Propose_Result_table.loc[0:4])
Top_Five.index = Top_Five.index + 1
#convert column nodes_TPN to int
Top_Five.nodes_TPN= Top_Five.nodes_TPN.astype(int)
#print(Top_Five)
#Propose_Table.to_csv('result/Propose_Table_kc_network.csv')
#Top_Five.to_csv('result/Propose_Table_[]_network.csv')

