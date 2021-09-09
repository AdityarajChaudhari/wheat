import pandas as pd
import numpy as np
from Data_Acquisition.Data_loader import Get_Data


class DataInfo:


    """

    This class is used to figure out size and shape and overall info of data we loaded previously
    written by : Adityaraj Hemant Chaudhari
    version    : 0.1
    revisions  : None

    """

    def get_shape(self):

        """

        Method_Name : get_shape()
        Description : This method is used to get the shape of the dataset loaded previously
        output      : 2-D array
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """
        try:
            self.shape = Get_Data().acquire_data().shape
            print(self.shape)
        except Exception as e :
            print("The error is :- ",e)
            raise e

    def get_info(self):

        """

        Method_Name : get_info()
        Description : This method is used to find the info i.e data type of columns,check null values , values present in column,etc.
        output      : Pandas DataFrame
        on failure  : raise Exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """
        try :
            self.info = Get_Data().acquire_data().info()
            print(self.info)
        except Exception as e:
            print("The error is :- ",e)
            raise e

    def get_size(self):

        """

        Method Name : get_size()
        Description : This method is used to find overall size of the dataset loaded.
        output      : Integer Value
        on Failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None


        """
        try:
            self.size = Get_Data().acquire_data().size
            print(self.size)
        except Exception as e:
            print("error is :- ",e)



