import pickle5 as pickle



for area in list(range(100)):
    #print('load',area)
    with open('parrot.pkl', 'wb') as f:
        pickle.dump(area,f)


#lista
# import pickle5 as pickle

# areas=[1,2,3,45,6,5,6,7]

# for area in list(range(10000)):
#     with open('parrot.pkl', 'wb') as f:
#             pickle.dump(areas,f)
