import pickle
dulist = ['com', 'info', 'smart', 'secu']
f = open('pickle.file', 'wb')
pickle.dump(dulist, f)
f.close()