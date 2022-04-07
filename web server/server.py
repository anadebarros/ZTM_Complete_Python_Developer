from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

email = EmailMessage()


# home page


@app.route("/")
def home():
    return render_template("index.html")

# dinamically route any page


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# store the data in a csv file
def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database2:
        sender_email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([sender_email, subject, message])


# route to receive data from contact form and keep it


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            # stores data in the form of a dictionary
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except KeyError:
            return "Please try again"
    else:
        return "Something went wrong"


# debugger
if __name__ == "__main__":
    app.run(debug=True)
