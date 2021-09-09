from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from Data_Splitting.train_test_split import SeperateIndependentFeature


class access_train_test_data:

    """

    Class_Name : access_train_test_data
    Description: This class is used to access training and testing data and then using this data to train the Machine Learning Model
    Written by : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def data_access(self):

        """

        Method_Name : data_access
        Description : This method is used to access the training and testing data
        Output      : Dataframe
        On_Failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """
        try:
            self.x_train,self.x_test,self.y_train,self.y_test = SeperateIndependentFeature().x_y_feat()
        except Exception as e:
            return e

    def rfc_model(self):

        """

        Method_Name : rfc_model
        Description : Using Random Forest Algorithm to build a model based on training data
        Output      : Model Accuracy
        On_Failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """
        try:
            self.rfc = RandomForestClassifier()
            self.rfc.fit(self.x_train,self.y_train)
            self.y_pred = self.rfc.predict(self.x_test)
            print(metrics.accuracy_score(self.y_test,self.y_pred))
        except Exception as e:
            return e

a = access_train_test_data()
a.data_access()
a.rfc_model()
