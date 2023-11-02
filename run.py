import dill
import tempfile
import test_module


file = tempfile.TemporaryFile()
dill._dill.StockPickler(file).save(test_module.test_function)
# OR
dill._dill.StockPickler(file).save(test_module.test)
# OR
import pickle
pickle._Pickler(file).save(test_module.test_function)

print('Success!')
