import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from Data_Acquisition.Data_loader import Get_Data


class SeperateIndependentFeature:
    """

    class Name  : SeperateIndependentFeature
    Description : This class is used to split the dataset in training and testing set.
    Written by  : Adityaraj Hemant Chaudhari
    Version     : 0.1
    Revision    : None

    """

    def x_y_feat(self):

        """

        Method_Name : x_y_feat
        Description : Splitting the dataset into dependent and independent features.
        Output      : DataFrame
        On Failure  : Raise Exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """
        try:
            self.x = Get_Data().acquire_data().drop("Type_Of_Kernel", axis=1)
            self.y = Get_Data().acquire_data()["Type_Of_Kernel"]
            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.25,
                                                                                    random_state=0)
            return self.x_train, self.x_test, self.y_train, self.y_test

        except Exception as e:
            print("The error is :- ", e)


s = SeperateIndependentFeature()
s.x_y_feat()

