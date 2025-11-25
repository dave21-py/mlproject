import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer # For handling missing values
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        logging.info("Entered the data transformation method")
        try:
            numerical_features = ["writing score","reading score"]
            categorical_features =   [
                "gender",
                "race/ethnicity", 
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")), # mode
                    ("one hot encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical columns standard scaling completed")
            logging.info("Categorical columns encoding completed")


            # Now we combine the numerical and categorical pipelines into a single ColumnTransformer object
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_features),
                    ("cat_pipeline", cat_pipeline, categorical_features)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_transformation(self, train_data_file_path, test_data_file_path):
        logging.info("Entered the data transformation method")
        try:
            train_df = pd.read_csv(train_data_file_path)
            test_df = pd.read_csv(test_data_file_path)
            logging.info("Train/Test completed")
            preprocessor_obj = self.get_data_transformer_object()
            target_column_name = "math score"
            numerical_features = ["reading score","writing score"]
            # For train data,
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]
            # Now for test data,
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object on training and testing data")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logging.info("Saved the preprocessing object")

            # Lets save the pkl file
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
             
        except Exception as e:
            raise CustomException(e, sys)
