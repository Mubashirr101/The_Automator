import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly as ply

# import bokeh
# import altair
# import missingno


class vizualize:
    def __init__(self, df):
        self.data = df

    def overview():
        # histograms
        # box/whisker plots
        # bar charts
        # Pie charts
        pass

    def data_distribution():
        # density plots
        # violin plots
        # ridge plots
        pass

    def missing_data_viz():
        # heatmaps
        # missingness matrix
        # barplots for na counts
        pass

    def relationship_viz():
        # scatter plots
        # bubble charts
        # pair plots
        pass

    def categorical_data_rel_viz():
        # barplots
        # count plts
        # stacked bar charts
        pass

    def multivariate_dist_viz():
        # heatmaps
        # facet grids
        # 3d plots
        pass

    def time_series_viz():
        # line charts
        # area charts
        # heatmaps
        # lag plots
        pass

    def outlier_viz():
        # boxplots
        # scatter plots
        # z-score / IQR vizualization
        pass

    def geo_data_viz():
        # choropleth maps
        # bubble maps
        # heatmaps on maps
        pass

    def adv_viz():
        # parallel coordinate plots
        # radial charts (spider/radar charts)
        # word counts
        # sankey diagrams
        pass

    def ml_viz():
        # feature imp plots
        # residual plots
        # ROC curve
        # Conf Matrix
        pass
