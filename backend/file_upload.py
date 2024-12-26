import os
from flask import Flask, request, render_template
import pandas import pd

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


def process_File(filename):
    file_path = os.path.join(filename)
    df = pd.read_csv(file_path)

    summary = df.describe().to_html(classes="table table-striped")
    return render_template("analysis.html", table=summary)


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
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)
            return (
                f"""printmessage: file uploaded successfully: {filename}
                  File Analysis : {process_File(filename)}""",
                200,
            )
        else:
            return "Invalid file type. Only CSV files are allowed", 400

    # For GET request, display the file upload form
    return """
    <!doctype html>
    <title>Upload a CSV File</title>
    <h1>Upload a CSV File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    """
