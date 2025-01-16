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
            df = pd.read_csv(csv_file)
            st.dataframe(df)

            # Create a copy of the uncleaned dataset
            uncleaned_df = df.copy()
            # Data Cleaning (placeholder for cleaning logic)
            cleaned_df = clean(df)
            # Data description
            self.data_description(cleaned_df)
        else:
            st.warning("Please upload a CSV file to proceed.")

    def data_description(self, df):

        # adding modules for different stat metrics
        st.subheader("Data Description")
        # creating an instance for the desc module
        d_stats = descriptive_stats()

        # Central tendency
        ct = self.convert_dict_dtypes(d_stats.central_tendency(df))
        st.write("Central Tendency Metrics:")
        ct_Data = pd.DataFrame(ct)
        pre_processed_ct_Data = self.preprocess_dataframe(ct_Data)
        # print(pre_processed_ct_Data)
        st.dataframe(pre_processed_ct_Data)

        # variability metric
        var = self.convert_dict_dtypes(d_stats.variability(df))
        st.write("Variability Metrics:")
        var_Data = pd.DataFrame(var)
        pre_processed_var_Data = self.preprocess_dataframe(var_Data)
        # print(pre_processed_var_Data)
        st.dataframe(pre_processed_var_Data)

        # Distribution Metric
        dist = self.convert_dict_dtypes(d_stats.distribution(df))
        st.write("Distribution Metrics:")
        dist_Data = pd.DataFrame(dist)
        pre_processed_dist_Data = self.preprocess_dataframe(dist_Data)
        # print(pre_processed_dist_Data)
        st.dataframe(pre_processed_dist_Data)

        # Shape and Spread
        shapeNspread = self.convert_dict_dtypes(d_stats.shapeNspread(df))
        st.write("Shape & Spread:")
        sns_Data = pd.DataFrame(shapeNspread)
        pre_processed_sns_Data = self.preprocess_dataframe(sns_Data)
        # print(pre_processed_sns_Data)
        st.dataframe(pre_processed_sns_Data)

        # Multivariate Relationships Metric
        rel = self.convert_dict_dtypes(d_stats.relationships_mvar(df))
        st.write("Multivariate Relationships Metric:")
        rel_Data = pd.DataFrame(rel)
        pre_processed_rel_Data = self.preprocess_dataframe(rel_Data)
        # print(pre_processed_rel_Data)
        st.dataframe(pre_processed_rel_Data)

        # frequency analysis
        freq_stats = self.convert_dict_dtypes(d_stats.freq_analysis(df))
        st.write("Frequency Analysis Metrics:")
        fs_Data = pd.DataFrame(freq_stats)
        pre_processed_fs_Data = self.preprocess_dataframe(fs_Data)
        # print(pre_processed_fs_Data)
        st.dataframe(pre_processed_fs_Data)

        # Describing the dataset
        dataset_description = self.convert_dict_dtypes(d_stats.dataset_desc(df))
        st.write("Dataset Description Metrics:")
        dd_Data = pd.DataFrame(dataset_description)
        pre_processed_dd_Data = self.preprocess_dataframe(dd_Data)
        # print(pre_processed_dd_Data)
        st.dataframe(pre_processed_dd_Data)
        # haha dd ..more like P.Diddy XD!!

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
        for col in df.columns:
            # Convert lists to strings for better compatibility
            df[col] = df[col].apply(
                lambda x: ", ".join(map(str, x)) if isinstance(x, list) else x
            )
        return df


if __name__ == "__main__":
    AutomatorApp()
