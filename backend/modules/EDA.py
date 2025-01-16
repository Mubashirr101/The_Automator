from verstack import NaNImputer
import pandas as pd


class descriptive_stats:

    def __init__(self):
        pass

    def central_tendency(self, df):
        # Measures of Central Tendency (per column): MEAN,MEDIAN,MODE
        ct_stats = {"mean": {}, "median": {}, "mode": {}}
        # 10% -> high cardinality threshold for mode
        mode_threshold = 0.1 * len(df)
        for col in df.columns:
            # mean and median
            if pd.api.types.is_numeric_dtype(df[col]):
                ct_stats["mean"][col] = df[col].mean()
                ct_stats["median"][col] = df[col].median()
            else:
                ct_stats["mean"][col] = "Non-Numeric"
                ct_stats["median"][col] = "Non-Numeric"

            # mode
            if df[col].nunique() > mode_threshold:
                ct_stats["mode"][col] = "No Mode - High Cardinality"
            elif pd.api.types.is_datetime64_any_dtype(df[col]):
                ct_stats["mode"][
                    col
                ] = f"Earliest: {df[col].min()}, Latest: {df[col].max()}"
            elif df[col].nunique() == len(df[col]):
                ct_stats["mode"][col] = "No Mode - Unique Values"
            else:
                ct_stats["mode"][col] = df[col].mode().tolist()
        return ct_stats

    def variability(self, df):
        # Measures of Variablility (Dispersion): Range,Variance,SD,IQR,MAD,CV
        # Range
        var_stats = {
            "Range": {},
            "Variance": {},
            "Standard Deviation": {},
            "IQR": {},
            "Mean Absolute Deviation": {},
            "Coeff. of Variance": {},
        }
        for i in df.select_dtypes(include="number").columns:
            var_stats["Range"][i] = df[i].max() - df[i].min()  # range
            var_stats["Variance"][i] = df[i].var()  # variance
            var_stats["Standard Deviation"][i] = df[i].std()  # SD
            var_stats["IQR"][i] = df[i].quantile(0.75) - df[i].quantile(0.25)  # IQR
            var_stats["Mean Absolute Deviation"][i] = abs(
                df[i] - df[i].mean()
            ).mean()  # MAD
            var_stats["Coeff. of Variance"][i] = df[i].std() / df[i].mean()  # CV

        return var_stats

    def distribution(self, df):
        # Measures of Distribution :
        # Skewness & Kurtosis
        distr_metric = {
            "Skewness": {},
            "Kurtosis": {},
            "Pos_Neg_Skew": {},
            "Heavy_Light_Tail": {},
            "Quantiles": {},
            "Deciles": {},
        }
        for i in df.select_dtypes(include="number").columns:
            distr_metric["Skewness"][i] = df[i].skew()
            distr_metric["Kurtosis"][i] = df[i].kurtosis()
            distr_metric["Quantiles"][i] = df[i].quantile([0.25, 0.5, 0.75]).tolist()
            distr_metric["Deciles"][i] = (
                df[i]
                .quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
                .tolist()
            )

        # check for positively/negatively/zero skewed
        for i in distr_metric["Skewness"].keys():
            if distr_metric["Skewness"][i] > 0:
                distr_metric["Pos_Neg_Skew"][i] = 1
            elif distr_metric["Skewness"][i] < 0:
                distr_metric["Pos_Neg_Skew"][i] = 2
            else:
                distr_metric["Pos_Neg_Skew"][i] = 0

        # Heavy/Light tails classification
        # 1 = Heavy Tails (Leptokurtic)
        # 0 = Normal Tails (Mesokurtic),
        # -1 = Light Tails (Platykurtic)
        for i in distr_metric["Kurtosis"].keys():
            if distr_metric["Kurtosis"][i] > 3:
                distr_metric["Heavy_Light_Tail"][i] = 1  # Heavy Tails
            elif distr_metric["Kurtosis"][i] < 3:
                distr_metric["Heavy_Light_Tail"][i] = -1  # Light Tails
            else:
                distr_metric["Heavy_Light_Tail"][i] = 0  # Normal Tails

        return distr_metric

    def shapeNspread(self, df):
        # Measures of shape & spread: Min/Max,5-numsum(min,q1,median,q3,max)
        shapenspread = df.describe()
        return shapenspread

    def relationships_mvar(self, df):
        # Measures of Relationship : Corr Coeff, CoV,CrossTab
        # Correlation Coefficient (Pearson,Spearman,kendall) & Covariance & Cross Tabulation (for categorical features only)
        relationships = {"Correlation_coeff": {}, "Covariance": {}, "Crosstab": {}}
        for col1 in df.select_dtypes(include="number").columns:
            for col2 in df.select_dtypes(include="number").columns:
                if col1 != col2:
                    relationships["Correlation_coeff"][(col1, col2)] = {
                        "Pearson": df[col1].corr(df[col2], method="pearson"),
                        "Spearman": df[col1].corr(df[col2], method="spearman"),
                        "Kendall": df[col1].corr(df[col2], method="kendall"),
                    }
                    relationships["Covariance"][(col1, col2)] = df[col1].cov(df[col2])
                    relationships["Crosstab"][(col1, col2)] = pd.crosstab(
                        df[col1], df[col2]
                    )
        return relationships

    def freq_analysis(self, df):
        # Frequency Analysis: Counts,Proportions/percentages,CF
        freq_stats = {"Counts": {}, "proportions": {}, "cumulative_freq": {}}

        # Counts: Frequency of each category/value data | hehe meoww! :3
        # Proportions/percentages : The relative freq of categorical data
        for col in df.select_dtypes(exclude="number").columns:
            freq_stats["Counts"][col] = df[col].value_counts().to_dict()
            freq_stats["proportions"][col] = (
                df[col].value_counts(normalize=True) * 100
            ).to_dict()

        # Cumulative Frequency
        for col in df.select_dtypes(include="number").columns:
            sorted_data = df[col].value_counts().sort_index()
            freq_stats["cumulative_freq"][col] = sorted_data.cumsum().to_dict()

        return freq_stats

    def dataset_desc(self, df):
        ds_desc = {
            "dimensions": {},
            "datatypes": {},
            "missing_values": {},
            "unique_values": {},
            "duplicate_values": {},
        }
        # Dimensions

        ds_desc["dimensions"]["Rows"] = df.shape[0]
        ds_desc["dimensions"]["Cols"] = df.shape[1]

        # Datatypes, Missing Values,Unique Values & Duplicate Values
        for col in df.columns:
            ds_desc["datatypes"][col] = df[col].dtype
            ds_desc["missing_values"][col] = df[col].isna().sum()
            ds_desc["unique_values"][col] = df[col].nunique()
            ds_desc["duplicate_values"][col] = df[col].duplicated().sum()

        return ds_desc


def summarize(df, output_format="html"):
    if output_format == "html":
        return df.describe().to_html(classes="table table-striped")
    elif output_format == "text":
        return df.describe()


def clean(df, strategy="NaNImputer"):
    imputer = NaNImputer()
    df_imputed = imputer.impute(df)
    print(f"Message from EDA.clean: Data is cleaned using '{strategy}'.")
    return df_imputed
