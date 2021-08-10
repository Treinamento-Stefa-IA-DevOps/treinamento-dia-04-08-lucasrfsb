import pickle 
import inspect 
 
with open('Titanic.pkl', 'rb') as fid:
    unpickler = pickle.Unpickler(fid)
    obj = unpickler.load()

print(type(obj))
print(dir(obj))
print(inspect.getsource(obj.predict))
##check_input = True and _validate_X_predict sorts input
