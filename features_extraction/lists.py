import sys
import os
import pandas as pd
import numpy as np
from cetd import CETD
import itertools
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 100)

from dom_mapper import DOM_Mapper






class Lists(DOM_Mapper):
    
    def __init__(self):
        
        
        
        pass
    
# =============================================================================
#     def vectorize(self, node):
#             
#         vect = self.reduce(node, fun1 = self.__init_vectorize, fun2 = self.__vectorize)
#         return vect
#     
#         pass
#     
#     
#     def __init_vectorize(self, node):
#         
#         vect = []
#         vect.append(node['LISTS']['relative'].values())
#         return vect
#     
#         pass
#     
#     def __vectorize(self, val, childval):
#         val += childval
#         return val
#     
#         pass
# =============================================================================
    
    
    def vectorize(self, node):
        
        arr = self.toArray(['LISTS'])
        mapped = list(map(lambda x : list(x[0]['adjust'].values()), arr))
        return np.array()
        
        pass
    
    def original(self):
        
        self.map(self.DOM, fun1 = self.__init_original)
        
        pass
    
    
    def __init_original(self, node):
        
        node['bounds']['centerX'] = node['bounds']['width']/2
        node['bounds']['centerY'] = node['bounds']['height']/2
        
        return node
        
        pass
    
    
    
    def absolute(self, node):
        
        self.map(
                node, 
                fun1 = self.__init_absolute, 
                fun3 = self.__absolute, 
                fun4 = self.__end_absolute
                )
        
        pass
    
    
    def __init_absolute(self, node):
        
        node['LISTS'] = {}
        node['LISTS']['absolute'] = {}
        node['LISTS']['absolute']['width'] = node['bounds']['width']
        node['LISTS']['absolute']['height'] = node['bounds']['height']
        node['LISTS']['absolute']['area'] = node['bounds']['width']*node['bounds']['height']
#        node['LISTS']['absolute']['top'] = node['bounds']['top']
#        node['LISTS']['absolute']['bottom'] = node['bounds']['bottom']
#        node['LISTS']['absolute']['left'] = node['bounds']['left']
#        node['LISTS']['absolute']['right'] = node['bounds']['right']
#        node['LISTS']['absolute']['x'] = node['bounds']['x']
#        node['LISTS']['absolute']['y'] = node['bounds']['y']
        
        
        node['LISTS']['absolute']['font-size'] = node['style']['font-size']
        
        return node
        
        pass
    
    
    def __absolute(self, parent, child):
        
        parent['LISTS']['absolute']['width'] += child['LISTS']['absolute']['width']
        parent['LISTS']['absolute']['height'] += child['LISTS']['absolute']['height']
        parent['LISTS']['absolute']['area'] += child['LISTS']['absolute']['area']
#        parent['LISTS']['absolute']['top'] += child['LISTS']['absolute']['top']
#        parent['LISTS']['absolute']['bottom'] += child['LISTS']['absolute']['bottom']
#        parent['LISTS']['absolute']['left'] += child['LISTS']['absolute']['left']
#        parent['LISTS']['absolute']['right'] += child['LISTS']['absolute']['right']
#        parent['LISTS']['absolute']['x'] += child['LISTS']['absolute']['x']
#        parent['LISTS']['absolute']['y'] += child['LISTS']['absolute']['y']
        
        
        parent['LISTS']['absolute']['font-size'] += child['LISTS']['absolute']['font-size']
        
        
        return parent, child
        
        pass
    
    
    def __end_absolute(self, node):
        
# =============================================================================
#         node['LISTS']['absolute']['width'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['height'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['area'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['top'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['bottom'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['left'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['right'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['x'] /= (len(node['children']) + 1)
#         node['LISTS']['absolute']['y'] /= (len(node['children']) + 1)
# =============================================================================
        
        return node
        
        pass
    
    
    
    def relative(self, node):
        
        self.map(
                self.DOM,
                fun2 = self.__relative
                 )
        
        pass
    
    
    
    def __relative(self, parent, child):
        
        child['LISTS']['relative'] = {}
        child['LISTS']['relative']['width'] = child['LISTS']['absolute']['width'] / parent['LISTS']['absolute']['width'] if  parent['LISTS']['absolute']['width'] != 0 else 1
        child['LISTS']['relative']['height'] = child['LISTS']['absolute']['height'] / parent['LISTS']['absolute']['height'] if  parent['LISTS']['absolute']['height'] != 0 else 1
        child['LISTS']['relative']['area'] = child['LISTS']['absolute']['area'] / parent['LISTS']['absolute']['area'] if  parent['LISTS']['absolute']['area'] != 0 else 1
#        child['LISTS']['relative']['top'] = child['LISTS']['absolute']['top'] / parent['LISTS']['absolute']['top'] if  parent['LISTS']['absolute']['top'] != 0 else 1
#        child['LISTS']['relative']['bottom'] = child['LISTS']['absolute']['bottom'] / parent['LISTS']['absolute']['bottom'] if  parent['LISTS']['absolute']['bottom'] != 0 else 1
#        child['LISTS']['relative']['left'] = child['LISTS']['absolute']['left'] / parent['LISTS']['absolute']['left'] if  parent['LISTS']['absolute']['left'] != 0 else 1
#        child['LISTS']['relative']['right'] = child['LISTS']['absolute']['right'] / parent['LISTS']['absolute']['right'] if  parent['LISTS']['absolute']['right'] != 0 else 1
#        child['LISTS']['relative']['x'] = child['LISTS']['absolute']['x'] / parent['LISTS']['absolute']['x'] if  parent['LISTS']['absolute']['x'] != 0 else 1
#        child['LISTS']['relative']['y'] = child['LISTS']['absolute']['y'] / parent['LISTS']['absolute']['y'] if  parent['LISTS']['absolute']['y'] != 0 else 1
#        child['LISTS']['relative']['centerX'] = child['LISTS']['absolute']['centerX'] / parent['LISTS']['absolute']['centerX'] if  parent['LISTS']['absolute']['centerX'] != 0 else 1
#        child['LISTS']['relative']['centerY'] = child['LISTS']['absolute']['centerY'] / parent['LISTS']['absolute']['centerY'] if  parent['LISTS']['absolute']['centerY'] != 0 else 1
        
        child['LISTS']['relative']['font-size'] = child['LISTS']['absolute']['font-size'] / parent['LISTS']['absolute']['font-size'] if  parent['LISTS']['absolute']['font-size'] != 0 else 1

        child['LISTS']['relative']['tagsCount'] = child['tagsCount'] / parent['tagsCount'] if  parent['tagsCount'] != 0 else 1
        
        return parent, child
    
        pass
    
    
    
    def adjust(self, node):
        
        self.map(
                node, 
                fun1 = self.__init_adjust, 
                fun2 = self.__adjust, 
                fun4 = self.__end_adjust
                )
        
        pass
    
    
    def __init_adjust(self, node):
        
        nbr_children = len(node['children'])
        expected_vect = np.full(nbr_children, float(1/float(nbr_children)) if nbr_children !=0 else 0)
        
        node['LISTS']['adjust'] = {}
        node['LISTS']['adjust']['expected_vect'] = expected_vect
        node['LISTS']['adjust']['width'] = []
        node['LISTS']['adjust']['height'] = []
        node['LISTS']['adjust']['area'] = []
        node['LISTS']['adjust']['font-size'] = []
        node['LISTS']['adjust']['tagsCount'] = []
            
        return node
        
        pass
    
    
    def __adjust(self, parent, child):
        
        
        parent['LISTS']['adjust']['width'].append(child['LISTS']['relative']['width'])
        parent['LISTS']['adjust']['height'].append(child['LISTS']['relative']['height'])
        parent['LISTS']['adjust']['area'].append(child['LISTS']['relative']['area'])
        parent['LISTS']['adjust']['font-size'].append(child['LISTS']['relative']['font-size'])
        parent['LISTS']['adjust']['tagsCount'].append(child['LISTS']['relative']['tagsCount'])
        
        return parent, child
        
        pass
    
    
    def __end_adjust(self, node):
        
        if node['LISTS']['adjust']['expected_vect'].shape[0] != 0:
            node['LISTS']['adjust']['width'] = cosine_similarity([node['LISTS']['adjust']['width']], [node['LISTS']['adjust']['expected_vect']])[0][0]
            node['LISTS']['adjust']['height'] = cosine_similarity([node['LISTS']['adjust']['height']], [node['LISTS']['adjust']['expected_vect']])[0][0]
            node['LISTS']['adjust']['area'] = cosine_similarity([node['LISTS']['adjust']['area']], [node['LISTS']['adjust']['expected_vect']])[0][0]
            node['LISTS']['adjust']['font-size'] = cosine_similarity([node['LISTS']['adjust']['font-size']], [node['LISTS']['adjust']['expected_vect']])[0][0]
            node['LISTS']['adjust']['tagsCount'] = cosine_similarity([node['LISTS']['adjust']['tagsCount']], [node['LISTS']['adjust']['expected_vect']])[0][0]
        else:
            
            node['LISTS']['adjust']['width'] = 0
            node['LISTS']['adjust']['height'] = 0
            node['LISTS']['adjust']['area'] = 0
            node['LISTS']['adjust']['font-size'] = 0
            node['LISTS']['adjust']['tagsCount'] = 0
            
            pass
            
        return node
        
        pass
    
    
    
    
    def markAll(self, xpaths, labels):
        
        for xpath in range(len(xpaths)):
            
            node = self.xpath_based_node_search(self.DOM, xpaths[xpath])
            node['mark'] = str(labels[xpath])
            node['LISTS']={}
            
            pass
                
        
        pass
    
    
    def remove(self, node):
        
        self.map(node, fun1 = self.__remove)
        pass
    
    
    def __remove(self, node):
        
        if len(node['children']) < 5:
            node['mark'] = "-1"
        
        return node
        pass
            
    
    pass





if __name__ == '__main__':
    
    lists = Lists()
#    cetd = CETD()
    lists.retrieve_DOM_tree(os.path.realpath('../datasets/extracted_data/0000.json'))
#    cetd.count_tags(lists.DOM)
#    lists.absolute(lists.DOM)
#    lists.relative(lists.DOM)
#    lists.adjust(lists.DOM)
#    features = ['xpath','LISTS.adjust.width', 'LISTS.adjust.height', 'LISTS.adjust.area', 'LISTS.adjust.font-size', 'LISTS.adjust.tagsCount']
#    arr = lists.flatten(lists.DOM, features = features)
#    arr = np.array(arr)
#    xpaths = arr[:,0]
#    X= arr[:,1:]
    
    
#    lists.DOM['LISTS']['relative'] = {}
#    vect = lists.vectorize(node = lists.DOM)
#    print(vect.shape)
    
#    tsne = TSNE(n_components=2).fit_transform(X)
#    km = KMeans(n_clusters = 2)
#    results = km.fit(X)
#    
#    plt.scatter(tsne[:,0], tsne[:,1], c = results.labels_)
#    lists.markAll(xpaths, results.labels_)
    
    # heuristic based method :
    lists.remove(lists.DOM)
    
    
    lists.update_DOM_tree()
    
    pass