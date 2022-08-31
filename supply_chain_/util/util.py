import logging
from forest_cover.exception import forest_cover_exception
import yaml
import os,sys
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
import scipy.cluster.hierarchy as sch
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as  np
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from imblearn.combine import SMOTETomek
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from forest_cover.constant import LOGISTICS_PARAMS_TUNING,CURRENT_TIME_STAMP,SVC_PARAMS_TUNING,DECISION_TREE_TUNING,RANDOM_FOREST_TUNING,GD_TUNING


def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise forest_cover_exception(e,sys) from e