import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class historical_tree():
    def __init__(self, main_person : str, persons : len) -> None:
        self.main_person = main_person
        self.persons = persons
    
    def get_persons(self):
        print(self.persons)
        
    def view(self):
        for i in range(len(self.persons)):
            G, pos = self.create_graph(self.main_person, self.persons[i])
            nx.draw(G, pos = pos)
            plt.show()
            
    def create_graph(self, main_person :str , persons : set):
        G = nx.Graph()
        for p in persons:
            G.add_edge(main_person, p)
        
        pos = {
            n: (i, 0) for i, n in enumerate(G.nodes)
        }
        
        for i, n in enumerate(G.nodes):
            print(i, n)
        return G, pos
        
        