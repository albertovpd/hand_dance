import pickle5 as pickle


while True:
        try:
                with open('parrot.pkl', 'rb') as f:
                        areas = pickle.load(f)
                        print(areas,"area captured")
        except: 
                print("hey")

#lista
# try:
#         with open('parrot.pkl', 'rb') as f:
#                 areas = pickle.load(f)
#                 print(areas,"audio")
# except: 
#         print("hey")
