import pickle
from Model_building.ml_model import access_train_test_data
from Hyperparameter_tuning.parameter_tuning import ParameterTuning

a = access_train_test_data()
p = ParameterTuning()

p.model_access()
p.setting_parameters()
p.model_tuning()

pickle.dump(p.rf_best,open('model.pkl','wb'))
print("Success")

