# streamlit ui homepage
import streamlit as st
import pandas as pd
import numpy as np
from modules.EDA import clean, summarize, descriptive_stats


class AutomatorApp:
    def __init__(self):
        # Title of the app with logo (in future)
        st.title("The Automator")

        # CSV file input
        csv_file = st.file_uploader(label="Upload the CSV file: ", type="csv")

        # Process the uploaded file
        if csv_file is not None:
            # Read and display the uploaded CSV
            self.df = pd.read_csv(csv_file)
            with st.expander("View Data"):
                st.dataframe(self.df)
            # Create a copy of the uncleaned dataset
            # self.uncleaned_df = df.copy()
            # # Data Cleaning (placeholder for cleaning logic)
            # self.cleaned_df = clean(df)

            # Multiple Tabs for Data Analysis
            tab1, tab2 = st.tabs(["Data Description", "Data Vizualization"])

            with tab1:
                self.data_description(self.df)

            # # Data description
            # self.data_description(cleaned_df)
        # else:
        #     st.warning("Please upload a CSV file to proceed.")

    def data_description(self, df):

        # adding modules for different stat metrics
        st.subheader("Data Description")
        # creating an instance for the desc module
        d_stats = descriptive_stats()

        # Selection panels
        with st.container(key="desc_stat_selection_panel", border=True):
            col1, col2 = st.columns(2)
            ds_type_opt = col1.selectbox(
                "Type",
                (
                    "Central Tendency",
                    "Variability",
                    "Data Distribution",
                    "Shape & Spread",
                    "Multivariate Relationships",
                    "Frequency Analysis",
                    "Dataset Description",
                ),
            )
            dsm_options = []
            if ds_type_opt == "Central Tendency":
                dsm_options.append("All")
                dsm_options.append("Mean")
                dsm_options.append("Median")
                dsm_options.append("Mode")
            elif ds_type_opt == "Variability":
                dsm_options.append("All")
                dsm_options.append("Range")
                dsm_options.append("Variance")
                dsm_options.append("Standard Deviation")
                dsm_options.append("Inter Quartile Range")
                dsm_options.append("Mean Absolute Deviation")
                dsm_options.append("Coefficient of Variance")
            elif ds_type_opt == "Data Distribution":
                dsm_options.append("All")
                dsm_options.append("Skewness")
                dsm_options.append("Kurtosis")
                dsm_options.append("Positive/Negative Skewness")
                dsm_options.append("Heavy/Light tailed")
                dsm_options.append("Quantiles")
                dsm_options.append("Deciles")
            elif ds_type_opt == "Shape & Spread":
                pass
            elif ds_type_opt == "Multivariate Relationships":
                dsm_options.append("All")
                dsm_options.append("Correlation Coefficient")
                dsm_options.append("Covariance")
                dsm_options.append("Crosstab")
            elif ds_type_opt == "Frequency Analysis":
                dsm_options.append("All")
                dsm_options.append("Counts")
                dsm_options.append("Proportions")
                dsm_options.append("Cumulative Frequency")
            elif ds_type_opt == "Dataset Description":
                dsm_options.append("All")
                dsm_options.append("Dimensions")
                dsm_options.append("Datatypes")
                dsm_options.append("Missing Values")
                dsm_options.append("Unique Values")
                dsm_options.append("Duplicate Values")
            else:
                dsm_options.append("choose a type")

            ds_metric = col1.selectbox("Metric", dsm_options)

            dataset_choice = col2.segmented_control(
                "Dataset", options=("Cleaned", "Uncleaned")
            )

            ds_cols_options = []
            if ds_type_opt == "Shape & Spread":
                pass
            else:
                if dataset_choice == "Cleaned":
                    self.cleaned_df = clean(df)
                    ds_cols_options = self.cleaned_df.columns.tolist()
                    ds_cols_options.insert(0, "All")

                elif dataset_choice == "Uncleaned":
                    self.uncleaned_df = df.copy()
                    ds_cols_options = self.uncleaned_df.columns.tolist()
                    ds_cols_options.insert(0, "All")

            ds_cols = col2.selectbox("Columns", ds_cols_options)

            ds_submit = st.button("Submit")

        if ds_submit:
            st.write(ds_type_opt, ds_metric, dataset_choice, ds_cols)

            if ds_type_opt == "Central Tendency":
                # Central tendency
                ct = self.convert_dict_dtypes(d_stats.central_tendency(df))
                st.write(f"{ds_type_opt} Metrics:")
                ct_df = self.choosing_dd(ct, ds_cols, ds_metric)
                print(ct_df)
                st.dataframe(ct_df)

            elif ds_type_opt == "Variability":
                # variability metric
                var = self.convert_dict_dtypes(d_stats.variability(df))
                st.write(f"{ds_type_opt} Metrics:")
                var_df = self.choosing_dd(var, ds_cols, ds_metric)
                # print(var_df)
                st.dataframe(var_df)

            elif ds_type_opt == "Data Distribution":
                # Distribution Metric
                dist = self.convert_dict_dtypes(d_stats.distribution(df))
                st.write("Distribution Metrics:")
                dist_Data = pd.DataFrame(dist)
                pre_processed_dist_Data = self.preprocess_dataframe(dist_Data)
                # print(pre_processed_dist_Data)
                st.dataframe(pre_processed_dist_Data)

            elif ds_type_opt == "Shape & Spread":
                # Shape and Spread
                shapeNspread = self.convert_dict_dtypes(d_stats.shapeNspread(df))
                st.write("Shape & Spread:")
                sns_Data = pd.DataFrame(shapeNspread)
                pre_processed_sns_Data = self.preprocess_dataframe(sns_Data)
                # print(pre_processed_sns_Data)
                st.dataframe(pre_processed_sns_Data)

            elif ds_type_opt == "Multivariate Relationships":

                # Multivariate Relationships Metric
                rel = self.convert_dict_dtypes(d_stats.relationships_mvar(df))
                st.write("Multivariate Relationships Metric:")
                rel_Data = pd.DataFrame(rel)
                pre_processed_rel_Data = self.preprocess_dataframe(rel_Data)
                # print(pre_processed_rel_Data)
                st.dataframe(pre_processed_rel_Data)

            elif ds_type_opt == "Frequency Analysis":

                # frequency analysis
                freq_stats = self.convert_dict_dtypes(d_stats.freq_analysis(df))
                st.write("Frequency Analysis Metrics:")
                fs_Data = pd.DataFrame(freq_stats)
                pre_processed_fs_Data = self.preprocess_dataframe(fs_Data)
                # print(pre_processed_fs_Data)
                st.dataframe(pre_processed_fs_Data)

            elif ds_type_opt == "Dataset Description":

                # Describing the dataset
                dataset_description = self.convert_dict_dtypes(d_stats.dataset_desc(df))
                st.write("Dataset Description Metrics:")
                dd_Data = pd.DataFrame(dataset_description)
                pre_processed_dd_Data = self.preprocess_dataframe(dd_Data)
                # print(pre_processed_dd_Data)
                st.dataframe(pre_processed_dd_Data)

    def choosing_dd(self, df, ds_cols, ds_metric):
        tmp_Data = pd.DataFrame(df)
        tmp_Data.columns = tmp_Data.columns.str.lower()
        tmp_Data.index = tmp_Data.index.str.lower()
        pre_processed_tmp_Data = self.preprocess_dataframe(tmp_Data)
        print(pre_processed_tmp_Data)
        # choosing what col
        if ds_cols == "All" and ds_metric == "All":
            ct_df = pre_processed_tmp_Data
        elif ds_cols == "All" and ds_metric != "All":
            ct_df = pre_processed_tmp_Data.loc[:, ds_metric.lower()]
        elif ds_metric == "All" and ds_cols != "All":
            ct_df = pre_processed_tmp_Data.loc[ds_cols.lower(), :]
        else:
            ct_df = pre_processed_tmp_Data.loc[[ds_cols.lower()], [ds_metric.lower()]]
        return ct_df

    def convert_dict_dtypes(self, stats_dict):
        """Convert all keys and values in the dictionary to strings."""
        if isinstance(stats_dict, pd.DataFrame):
            # Convert DataFrame to a JSON-compatible dictionary & call a recursive func to make it string
            return self.convert_dict_dtypes(stats_dict.to_dict("dict"))
            # Converting rows into list of dicts
        elif isinstance(stats_dict, dict):
            new_dict = {}
            for key, value in stats_dict.items():
                # Convert keys to strings if they are not already
                new_key = str(key) if not isinstance(key, str) else key

                if isinstance(value, dict):
                    # Recursively handle nested dictionaries
                    new_dict[new_key] = self.convert_dict_dtypes(value)
                elif isinstance(value, (tuple, list)):
                    # Convert each element to string if it's a tuple or list
                    new_dict[new_key] = [str(item) for item in value]
                else:
                    # Convert the value to a string
                    new_dict[new_key] = str(value)
            return new_dict
        else:
            return str(stats_dict)  # Handle non-dict cases

    def preprocess_dataframe(self, df):
        # Ensure the dataframe is valid
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"Expected DataFrame, got {type(df).__name__}")

        # Process each column
        for col in df.columns:
            # Check if the column contains lists
            df[col] = df[col].apply(
                lambda x: ", ".join(map(str, x)) if isinstance(x, list) else str(x)
            )
        return df


if __name__ == "__main__":
    AutomatorApp()
