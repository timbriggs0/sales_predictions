import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import pickle

from bokeh.plotting import figure, curdoc
from bokeh.models import Slider, ColumnDataSource, CDSView, IndexFilter, Plot, VBar
from bokeh.layouts import row, gridplot, layout #column
from bokeh.io import output_file, show, save
from bokeh.themes import Theme

df = pd.read_csv('sales_predictions_clean.csv')
source = ColumnDataSource(df)

