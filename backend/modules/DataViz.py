# Types of data viz
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import plotly.express as px


class vizualize:
    def __init__(self):
        pass

    # Overview #
    def histo(self, col):
        # histograms
        plt.hist(col, bins=5, alpha=0.5, label=col.name)
        plt.xlabel(col.name)
        plt.ylabel("frequency")
        plt.title(f"Histogram of {col.name}")
        plt.legend()
        plt.show()

    def boxplt(self, col):
        # box plot
        plt.boxplot(col)
        plt.xlabel(col.name)
        plt.ylabel("values")
        plt.title(f"Boxplot of {col.name}")
        plt.show()

    def barchrt(self, col):
        # bar charts
        col.value_counts().plot(kind="bar")
        plt.xlabel(col.name)
        plt.ylabel("frequency")
        plt.title(f"Bar chart of {col.name}")
        plt.show()

    def piechrt(self, col):
        # Pie charts
        col.value_counts().plot(kind="pie")
        plt.xlabel(col.name)
        plt.ylabel("frequency")
        plt.title(f"Pie chart of {col.name}")
        plt.show()

    # Data Distribution

    def densityplots(self, col):
        # density plots
        col.plot.density(color="green")
        plt.xlabel(col.name)
        plt.ylabel("density")
        plt.title(f"Density plot of {col.name}")
        plt.show()

    def violinplots(self, col):
        # violin plots
        plt.violinplot(col)
        plt.xlabel(col.name)
        plt.ylabel("values")
        plt.title(f"Violin plot of {col.name}")
        plt.show()

    def ridgeplots(self, col):
        # ridge plots
        # for categorical data features
        pass

    # missing data vizualizations
    def heatmaps_na(self, df):
        # heatmaps for missing data
        missing_corr = df.isna().corr()

        sns.heatmap(missing_corr, annot=True, cmap="coolwarm", cbar=True)
        plt.xlabel("columns")
        plt.ylabel("rows")
        plt.title("Correlation of missing data")
        plt.show()

    def missingness_matrix(self, df):
        # missingness matrix
        msno.matrix(df)
        plt.title("Missingness Matrix")
        plt.show()

    def barplots_na(self, df):
        # barplots for na counts
        missing_counts = df.isna().sum()
        missing_counts.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Missing Values per column")
        plt.xlabel("columns")
        plt.ylabel("missing values count")
        plt.xticks(rotation=0)
        plt.show()

    # vizualization for relationships
    def scatterplt(self, col1, col2):
        # scatter plots
        plt.scatter(col1, col2)
        plt.xlabel(col1.name)
        plt.ylabel(col2.name)
        plt.title(f"Scatter plot of {col1.name} vs {col2.name}")
        plt.show()

    def bubblechrts(self, col1, col2, col3):
        # bubble charts
        fig = px.scatter(x=col1, y=col2, size=col3)
        fig.show()

    def pairplots(self, df):
        # pair plots
        sns.pairplot(df)
        plt.show()
        # will add more support for the user to choose the plotting variables

    # categorical data relationship vizualization
    def barplts_cat(self, col1, col2):
        # Bar Plot: Compare categories of one variable with another
        sns.barplot(x=col1, y=col2, ci=None, palette="viridis")
        plt.xlabel(col1.name)
        plt.ylabel(col2.name)
        plt.title(f"Bar plot of {col1.name} vs {col2.name}")
        plt.show()

    def cnt_plts(self, col):
        # Count Plot: Frequency distribution of categorical variables
        sns.countplot(x=col)
        plt.xlabel(col.name)
        plt.ylabel("count")
        plt.title(f"Count plot of {col.name}")
        plt.show()

    def stacked_brplts(self, df, col1, col2):
        # stacked bar charts
        # Stacked Bar Chart: Show proportions of categories within a larger category
        stacked_data = df.groupby([col1.name, col2.name]).size().unstack(fill_value=0)
        stacked_data.plot(kind="bar", stacked=True, figsize=(10, 7), colormap="tab20")
        plt.title("Sales Split by Product Category and Region", fontsize=16)
        plt.xlabel(col1.name, fontsize=12)
        plt.ylabel(col2.name, fontsize=12)
        plt.legend(title="Product Category")
        plt.tight_layout()
        plt.show()

    # multivariate distribution vizualization
    def heatmaps_mul(self, df):
        # heatmaps
        # plt.figure(figsize=(8, 6))
        # correlation_matrix = df[['Sales', 'Profit', 'Cost']].corr()
        # sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        # plt.title('Correlation Heatmap of Numerical Variables', fontsize=16)
        # plt.show()
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu")
        plt.title("Correlation Heatmap")
        plt.show()

    def facetgrids(self, df, col1, col2, col3):
        # facet grids
        # sns.set(style="whitegrid")
        # g = sns.FacetGrid(df, col="col1", hue="col2", height=4, aspect=1)
        # g.map(sns.histplot, "col3", kde=True, alpha=0.7).add_legend()
        # g.fig.subplots_adjust(top=0.9)
        # g.fig.suptitle('Distribution of col3 by col1 Across col2', fontsize=16)
        # plt.show()

        grids = sns.FacetGrid(df, row=col1.name, col=col2.name)
        grids.map(plt.scatter, col1.name, col2.name, edgecolor="w")
        grids.add_legend()
        plt.show()

    def plots_3d(self, col1, col2, col3):
        # 3d plots
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(col1, col2, col3, c="blue", marker="o", s=100)
        ax.set_title(
            f"3d Plot : {col1.name} vs. {col2.name} vs {col3.name}", fontsize=16
        )
        ax.set_xlabel(col1.name, fontsize=12)
        ax.set_ylabel(col2.name, fontsize=12)
        ax.set_zlabel(col3.name, fontsize=12)
        plt.show()

    # time series vizualization
    def line_chrts(self, col1, col2):
        # line charts
        plt.figure(figsize=(10, 6))
        plt.plot(col1, col2, marker="o", linestyle="-", color="blue")
        plt.title(f"f{col2.name} vs {col1.name}", fontsize=16)
        plt.xlabel(col1.name, fontsize=12)
        plt.ylabel(col2.name, fontsize=12)
        plt.grid()
        plt.show()

    def area_chrts(self, col1, col2):
        # area charts
        plt.figure(figsize=(10, 6))
        plt.fill_between(col1, col2, color="skyblue", alpha=0.4)
        plt.plot(col1, col2, marker="o", color="blue")
        plt.title(f"{col2.name} vs {col1.name}", fontsize=16)
        plt.xlabel(col1.name, fontsize=12)
        plt.ylabel(col2.name, fontsize=12)
        plt.grid()
        plt.show()

    def heatmps_ts(self, df, col1, col2, col3):
        # heatmaps
        cols_pivot = pd.pivot(
            data=df, index=col1.name, columns=col2.name, values=col3.name
        )
        plt.figure(figsize=(12, 8))
        sns.heatmap(cols_pivot, cmap="YlGnBu", annot=False)
        plt.xlabel(col2.name, fontsize=12)
        plt.ylabel(col1.name, fontsize=12)
        plt.title(f"{col3.name} HeatMap ({col1.name} vs {col2.name})", fontsize=16)
        plt.show()

    def lag_plots(self, col1):
        # lag plots
        plt.figure(figsize=(6, 6))
        pd.plotting.lag_plot(col1, lag=1)
        plt.title(f"Lag Plot: {col1.name}", fontsize=16)
        plt.xlabel(f"{col1.name} (t)", fontsize=12)
        plt.ylabel(f"{col1.name} (t+1)", fontsize=12)
        plt.grid()
        plt.show()

    # outlier vizualization

    def outlier_boxplots(self, col1):
        # boxplots
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=col1, color="skyblue")
        plt.title(f"Boxplot of {col1.name}", fontsize=16)
        plt.xlabel(col1.name, fontsize=12)
        plt.show()

    def outlier_scatterplots(self, col1):
        # scatter plots
        plt.figure(figsize=(8, 6))
        plt.scatter(df.index, col1, color="blue", alpha=0.7)
        plt.axhline(
            col1.mean() + 2 * col1.std(),
            color="red",
            linestyle="--",
            label="Upper Threshold",
        )
        plt.axhline(
            col1.mean() - 2 * col1.std(),
            color="red",
            linestyle="--",
            label="Lower Threshold",
        )
        plt.title("Scatter Plot with Threshold", fontsize=16)
        plt.xlabel("Index", fontsize=12)
        plt.ylabel(col1.name, fontsize=12)
        plt.legend()
        plt.show()

    def outlier_zscore_viz(self, col1):
        z_scores = (col1 - col1.mean()) / col1
        plt.figure(figsize=(8, 6))
        plt.hist(z_scores, bins=10, color="lightblue", edgecolor="black")
        plt.axvline(2, color="red", linestyle="--", label="Outlier Threshold")
        plt.axvline(-2, color="red", linestyle="--")
        plt.title("Z-Score Histogram", fontsize=16)
        plt.xlabel("Z-Score", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.legend()
        plt.show()

    def outlier_iqrplots(self, df, col1):
        # z-score / IQR vizualization
        Q1 = col1.quantile(0.25)
        Q3 = col1.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        plt.figure(figsize=(8, 6))
        plt.scatter(df.index, col1, color="blue", alpha=0.7)
        plt.axhline(upper_bound, color="orange", linestyle="--", label="Upper Bound")
        plt.axhline(lower_bound, color="green", linestyle="--", label="Lower Bound")
        plt.title("IQR Method for Outlier Detection", fontsize=16)
        plt.xlabel("Index", fontsize=12)
        plt.ylabel(col1.name, fontsize=12)
        plt.legend()
        plt.show()

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
