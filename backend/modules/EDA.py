from verstack import NaNImputer
import pandas as pd


class descriptive_stats:

    def __init__(self, df):
        self.data = df

    def central_tendency(self):
        # Measures of Central Tendency (per column): MEAN,MEDIAN,MODE
        ct_stats = {"mean": {}, "median": {}, "mode": {}}
        # 10% -> high cardinality threshold for mode
        mode_threshold = 0.1 * len(self.data)
        for col in self.data.columns:
            # mean and median
            if pd.api.types.is_numeric_dtype(self.data[col]):
                ct_stats["mean"][col] = self.data[col].mean()
                ct_stats["median"][col] = self.data[col].median()
            # mode
            if self.data[col].nunique() > mode_threshold:
                ct_stats["mode"][col] = "No Mode - High Cardinality"
            elif pd.api.types.is_datetime64_any_dtype(self.data[col]):
                ct_stats["mode"][
                    col
                ] = f"Earliest: {self.data[col].min()}, Latest: {self.data[col].max()}"
            elif self.data[col].nunique() == len(self.data[col]):
                ct_stats["mode"][col] = "No Mode - Unique Values"
            else:
                ct_stats["mode"][col] = self.data[col].mode().tolist()
        return ct_stats


def variability(self):
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
    for i in self.data.select_dtypes(include="number").columns:
        var_stats[i] = self.data[i].max() - self.data[i].min()  # range
        var_stats[i] = self.data[i].var()  # variance
        var_stats[i] = self.data[i].std()  # SD
        var_stats[i] = self.data[i].quantile(0.75) - self.data[i].quantile(0.25)  # IQR
        var_stats[i] = abs(self.data[i] - self.data[i].mean()).mean()  # MAD
        var_stats[i] = self.data[i].std() / self.data[i].mean()  # CV

    return var_stats


# def distribution(self):


def summarize(df, output_format="html"):
    if output_format == "html":
        return df.describe().to_html(classes="table table-striped")
    elif output_format == "text":
        return df.describe()


def clean(df, strategy="NaNImputer"):
    imputer = NaNImputer()
    df_imputed = imputer.impute(df)
    print(f"Message from EDA.clean: data is cleaned using '{strategy}'.")
    return df_imputed
