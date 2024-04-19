from flask import Flask, request, jsonify
from validator import validate_table_format  # Import the validate_table_format function

app = Flask(_name_)


@app.route("/validate-table", methods=["POST"])
def validate_table():
    # Check if a file is uploaded
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    # Validate file extension
    if file.filename.endswith(".csv") or file.filename.endswith(".xlsx"):
        # Save the file temporarily
        file_path = "temp_file." + file.filename.rsplit(".", 1)[1]
        file.save(file_path)

        # Validate table format
        is_valid = validate_table_format(file_path)

        # Delete the temporary file
        os.remove(file_path)

        return jsonify({"is_valid": is_valid})
    else:
        return jsonify(
            {"error": "Unsupported file format. Please upload a CSV or Excel file"}
        )


if _name_ == "_main_":
    app.run(debug=True)
