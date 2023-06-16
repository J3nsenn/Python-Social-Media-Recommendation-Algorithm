
# Write your algorithm in this function. 
# Except for import statements, all other code must be within the recommendFriendPair function or additional helper functions
from collections import defaultdict #Imports the library to use a defaultdictionary
def recommendFriendPair(given_network): 
    network = given_network.network
    N = given_network.N
    E = given_network.E
    
    max_mutual_friend_count = 0 # Assigns a variabl by this name to 0
    neighbor_dict = defaultdict(set) #Creates an empty default dictionary Object of this name
    
    for u in range(N):
        for v in range(u+1, N): # 
            if network[u][v] == 1: #Condition to include only connected nodes (friends)in this dictionary
                neighbor_dict[u].add(v) # u as a user and adds v as a set to the dictionary
                neighbor_dict[v].add(u) # v as a user and adds u as a set to the dictionary
    
    best_pair = None # Assigns empty value to this variable
    for u in range(N):
        for v in range(u+1, N):
            if network[u][v] == 0: #Condition to exclude users that are already friends
                mutual_friends = neighbor_dict[u] & neighbor_dict[v] #Obtains number of mututal friends based on the intersection of sets for u and v
                mutual_friend_count = len(mutual_friends) # Obtains integer value from length functon of dictionary object
                if mutual_friend_count > max_mutual_friend_count: 
                    max_mutual_friend_count = mutual_friend_count # Constantly reassigns the max mutual friends for a pair to a new one if the previous condition is met
                    best_pair = (u,v) # Best pair is returned when mutual_friend_count is no longer > max_mutual_friend_count
                    
    return best_pair

# Write your algorithm in this function. 
# Except for import statements, all other code must be within the recommendFriendPair function or additional helper functions
from collections import defaultdict # O(1) Operation
def recommendFriendPair(given_network): # O(1) Operation
    network = given_network.network # O(1) Operation
    N = given_network.N # O(1) Operation
    E = given_network.E # O(1) Operation
    
    max_mutual_friend_count = 0 # O(1) Operation
    neighbor_dict = defaultdict(set) # O(1) Operation
    
    for u in range(N):
        for v in range(u+1, N): # O(n^2) Operation due to nested for loops for values u and v
            if network[u][v] == 1: #O(1) Operation
                neighbor_dict[u].add(v) #O(1) Operation
                neighbor_dict[v].add(u) #O(1) Operation
    
    best_pair = None #O(1) Operation
    for u in range(N):
        for v in range(u+1, N): #O(n^2) Operation, nested for loops 
            if network[u][v] == 0:  #O(1) Operation
                mutual_friends = neighbor_dict[u] & neighbor_dict[v] #O(1) Operation
                mutual_friend_count = len(mutual_friends) #O(1) Operation
                if mutual_friend_count > max_mutual_friend_count: #O(1) Operation
                    max_mutual_friend_count = mutual_friend_count #O(1) Operation
                    best_pair = (u,v) #O(1) Operation
                    
    return best_pair #O(1) Operation


#PseudoCode

def recommendFriendPair(given_network):
    network = given_network.network
    N = No of edges of network 
    E = No of edges of network

    Create variable to store the maximum number of mutual friends
    Create empty default dictionary object to store an adjacency list of nodes in this graph

    for node u in range (N):
        for node v in range (N, excluding u):
            if u and v in this network are friends:
                attach wefwefwef

    Create a variable to store the best recommended pair
    for node u in range (N):
        for node v in range (N, excluding u):
            if u and v are not friends:
                then the mutual friends for v and u is the intersection between the sets of xxxxxxxxxxx
                obtain the nunmber of mutual friends using the lenth function of the set containing mututal friends for v and u
                if the number of mutual friends > current maximum number of mutual friends:
                    reassign the maximum number of mututal friends to this value to obtain the highest number of mutual friends in the for loops
                    assign best pair to the nodes (u,v)
    
    return the best pair 

