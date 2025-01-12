# Types of data viz
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import plotly.express as px

class vizualize:
    def __init__(self):
      pass
    # Overview #
    def histo(self,col):
        # histograms
        plt.hist(col,bins=5,alpha=0.5,label=col.name)
        plt.xlabel(col.name)
        plt.ylabel('frequency')
        plt.title(f'Histogram of {col.name}')
        plt.legend()
        plt.show()

    def boxplt(self,col):
        # box plot
        plt.boxplot(col)
        plt.xlabel(col.name)
        plt.ylabel('values')
        plt.title(f'Boxplot of {col.name}')
        plt.show()

    def barchrt(self,col):
        # bar charts
        col.value_counts().plot(kind='bar')
        plt.xlabel(col.name)
        plt.ylabel('frequency')
        plt.title(f'Bar chart of {col.name}')
        plt.show()

    def piechrt(self,col):
        # Pie charts
        col.value_counts().plot(kind='pie')
        plt.xlabel(col.name)
        plt.ylabel('frequency')
        plt.title(f'Pie chart of {col.name}')
        plt.show()


    # Data Distribution

    def densityplots(self,col):
        # density plots
        col.plot.density(color='green')
        plt.xlabel(col.name)
        plt.ylabel('density')
        plt.title(f'Density plot of {col.name}')
        plt.show()

    def violinplots(self,col):
        # violin plots
        plt.violinplot(col)
        plt.xlabel(col.name)
        plt.ylabel('values')
        plt.title(f'Violin plot of {col.name}')
        plt.show()

    def ridgeplots(self,col):
        # ridge plots
        # for categorical data features
        pass


    # missing data vizualizations
    def heatmaps_na(self,df):
        # heatmaps for missing data
        missing_corr = df.isna().corr()

        sns.heatmap(missing_corr,annot=True, cmap='coolwarm',cbar=True)
        plt.xlabel('columns')
        plt.ylabel('rows')
        plt.title('Correlation of missing data')
        plt.show()


    def missingness_matrix(self,df):
        # missingness matrix
        msno.matrix(df)
        plt.title('Missingness Matrix')
        plt.show()



    def barplots_na(self,df):
        # barplots for na counts
        missing_counts = df.isna().sum()
        missing_counts.plot(kind='bar',color='skyblue',edgecolor='black')
        plt.title('Missing Values per column')
        plt.xlabel('columns')
        plt.ylabel('missing values count')
        plt.xticks(rotation=0)
        plt.show()



  # vizualization for relationships
    def scatterplt(self,col1,col2):
        # scatter plots
        plt.scatter(col1,col2)
        plt.xlabel(col1.name)
        plt.ylabel(col2.name)
        plt.title(f'Scatter plot of {col1.name} vs {col2.name}')
        plt.show()

    def bubblechrts(self,col1,col2,col3):
        # bubble charts
        fig = px.scatter(x=col1, y=col2, size=col3)
        fig.show()


    def pairplots(self,df):
        # pair plots
        sns.pairplot(df)
        plt.show()
        # will add more support for the user to choose the plotting variables

    # categorical data relationship vizualization
    def barplts_cat(self,col1,col2):
        # Bar Plot: Compare categories of one variable with another
        sns.barplot(x=col1,y=col2,ci=None,palette='viridis')
        plt.xlabel(col1.name)
        plt.ylabel(col2.name)
        plt.title(f'Bar plot of {col1.name} vs {col2.name}')
        plt.show()
        
    def cnt_plts(self,col):
        # Count Plot: Frequency distribution of categorical variables
        sns.countplot(x=col)
        plt.xlabel(col.name)
        plt.ylabel('count')
        plt.title(f'Count plot of {col.name}')
        plt.show()
        
    def stacked_brplts(self,df,col1,col2):
        # stacked bar charts
        # Stacked Bar Chart: Show proportions of categories within a larger category
        stacked_data = df.groupby([col1.name,col2.name]).size().unstack(fill_value=0)
        stacked_data.plot(kind='bar', stacked=True, figsize=(10, 7), colormap='tab20')
        plt.title('Sales Split by Product Category and Region', fontsize=16)
        plt.xlabel(col1.name, fontsize=12)
        plt.ylabel(col2.name, fontsize=12)
        plt.legend(title='Product Category')
        plt.tight_layout()
        plt.show()

    # multivariate distribution vizualization
    def heatmaps_mul(self,df):
        # heatmaps
        sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='YlGnBu')
        plt.title('Correlation Heatmap')
        plt.show()
        
    def facetgrids():
        # facet grids
        pass
    def plots_3d():
        # 3d plots
        pass


    # time series vizualization
    def line_chrts():
        # line charts
        pass
    def area_chrts():
        # area charts
        pass
    def heatmps():
        # heatmaps
        pass
    def lag_plots():
        # lag plots
        pass

    # outlier vizualization

    def outlier_boxplots():
        # boxplots
        pass
    def outlier_violinplots():
        # violin plots
        pass
    def outlier_scatterplots():
        # scatter plots
        pass
    def outlier_iqrplots():
        # z-score / IQR vizualization
        pass

    # geographic data vizualization
    def choropleth_mps():
        # choropleth maps
        pass
    def bubble_mps():
        # bubble maps
        pass
    def heatmaps_mps():
        # heatmaps on maps
        pass

    # advanced data viz
    def prll_coord_plts():
        # parallel coordinate plots
        pass
    def rad_chrts():
        # radial charts (spider/radar charts)
        pass
    def word_cnts():
        # word counts
        pass
    def sankey_diagrams():
        # sankey diagrams
        pass
  # Machine Learning data viz
    def feat_imp_plts():
        # feature imp plots
        pass
    def resid_plts():
        # residual plots
        pass
    def roc_curves():
        # ROC curve
        pass
    def conf_mat():
        # Conf Matrix
        pass
