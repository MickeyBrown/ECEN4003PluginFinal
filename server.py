from flask import Flask, render_template
import source

app = Flask(__name__)

if __name__ == "__main__":
	app.run()

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/addPlugin")
def form_add(): #data has to be sent to the add plugin function
    return render_template('addPlugin.html')

@app.route("/removePlugin")
def form_remove(): #data has to be sent to the remove plugin function
    return render_template('removePlugin.html')

@app.route("/urlStatus")
def urlStatus():
	status_database = source.url_status() 
	return render_template('urlStatus.html', status_database = status_database)

@app.route("/currentPlugin")
def currentPlugin():
	current_list = source.print_current() 
	print(current_list)
	return render_template('currentPlugin.html', current_list = current_list)
 

 
 