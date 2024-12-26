import os
from flask import Flask, request, jsonify, render_template
import pandas as pd
from modules.EDA import clean, summarize, descriptive_stats

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = {"csv"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/")
def home():
    return "Welcome to The Automator"


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if the request contains a file
        if "file" not in request.files:
            return "No file part", 400
        file = request.files["file"]

        # If the user did not select a file
        if file.filename == "":
            return "No selected file", 400

        # Check if the file has the correct extension
        if file and allowed_file(file.filename):
            print(f"File: {file}, File.Filename{file.filename}")
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)
            return render_template("file_uploaded.html", filename=filename)

        else:
            return "Invalid file type. Only CSV files are allowed", 400

    # For GET request, display the file upload form
    return render_template("upload_file.html")


@app.route("/process", methods=["GET"])
def process_file():
    filename = request.args.get("filename")
    if not filename:
        return "No filename provided", 400
    file_path = os.path.join(filename)

    try:

        df = pd.read_csv(file_path)
        summary = summarize(df)
        # print("Null vals in uncleaned data: ", df.isnull().sum())
        # Cleaning the DataFrame
        cleaned_df = clean(df)
        # print("Null vals in clean data: ", cleaned_df.isnull().sum())

        dstats = descriptive_stats(cleaned_df)
        print(dstats.central_tendency())
        return render_template(
            "analysis.html",
            table=summary,
            cleaned_table=cleaned_df.head().to_html(classes="table table-striped"),
        )

    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
