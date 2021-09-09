from sklearn.model_selection import RandomizedSearchCV
from Model_building.ml_model import access_train_test_data
from sklearn import metrics

class ParameterTuning:

    """

    Class_Name : ParameterTuning
    Description: This Class is used to perform hyperparamter tuning on the Random Forest model.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.a = access_train_test_data()

    def model_access(self):

        """

        Method Name : model_access
        Description : This method is used to access the training and testing data as well as machine learning model built.
        output      : DataFrame
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """
        try:
            self.val = self.a.data_access()
            self.model = self.a.rfc_model()
        except Exception as e:
            raise e

    def setting_parameters(self):

        """

        Method Name : setting_parameters
        Description : This method is used to choose the best parameters and assigning it with set of values which can help our model to give better results.
        output      : None
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """
        try:
            self.param_grid = {
                'n_estimators': [x for x in range(10,3000,100)],
                'criterion': ['gini','entropy'],
                'max_features': ['auto','log2',None],
                'min_samples_leaf': [int(x) for x in range(1,100,1)],
                'min_samples_split': [x for x in range(2,100,1)],
                'max_depth': [x for x in range(1,53,1)]
            }
        except Exception as e:
            raise e

    def model_tuning(self):

        """

        Method Name : model_tuning
        Description : This method is used to perform hyperparameter tuning using the set of values .
        output      : Acc.Scores
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """
        try:
            self.rf_randomcv = RandomizedSearchCV(estimator=self.a.rfc,param_distributions=self.param_grid,n_iter=200,cv=3,n_jobs=-1,random_state=100,verbose=True)
            self.rf_randomcv.fit(self.a.x_train, self.a.y_train)

            self.rf_best = self.rf_randomcv.best_estimator_
            print(self.rf_best)
            y_pre = self.rf_best.predict(self.a.x_test)

            print(metrics.accuracy_score(self.a.y_test, y_pre))
            print(self.rf_best.score(self.a.x_train,self.a.y_train))
        except Exception as e:
            raise e

p = ParameterTuning()
p.model_access()
p.setting_parameters()
p.model_tuning()






















