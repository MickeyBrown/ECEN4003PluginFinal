from flask import Flask, render_template, request
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

@app.route("/add_submit/", methods = ['POST', 'GET'])
def data_add():
	if request.method == 'GET':
		return render_template("home.html")
		
	if request.method == 'POST':
		form_data = request.form
		source.addPlugin(form_data['Name'], form_data['Type'], form_data['Port'], form_data['Archive'], form_data['Language'], form_data['Test'], form_data['Description'], form_data['Endpoint'], form_data['Repository'], form_data['DockerFiler'], form_data['URL'])
		return render_template('add_submit.html', plugin_name = form_data['Name'])

@app.route("/removePlugin")
def form_remove(): #data has to be sent to the remove plugin function
    return render_template('removePlugin.html')

@app.route("/remove_submit/", methods = ['POST', 'GET'])
def data_remove():
	if request.method == 'GET':
		return render_template("home.html")
	if request.method == 'POST':
		form_data = request.form
		if source.removePlugin(form_data['Name']):
			return render_template("remove_submit.html", plugin_name = form_data['Name'])
		else:
			return render_template('remove_none.html')

@app.route("/urlStatus")
def urlStatus():
	status_database = source.url_status() 
	return render_template('urlStatus.html', status_database = status_database)

@app.route("/currentPlugin")
def currentPlugin():
	current_list = source.print_current() 
	print(current_list)
	return render_template('currentPlugin.html', current_list = current_list)
 

 
 
