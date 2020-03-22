from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__) # instantiate app
print(__name__)

# app.config['DEBUG'] = False

@app.route('/')  # root folder in website url
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject= data["subject"]
        message=data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline = '',mode='a') as database2:
        email = data["email"]
        subject= data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject,message])
@app.route('/submit_form', methods=['POST','GET']) #GET means browser wants us to send information, POST means that browser wants us to save information 
def submit_form():  # we dont call this on frontend
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # if server crashes or stops, the submitted info is lost. So, it is better to persist it (write to another storage)
            #write_to_file(data)  # write to text file
            write_to_csv(data)  # write to csv file
            #print(data)
            return redirect('/thankyou.html')
            #return 'form submitteed hoorayy'
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'
    
@app.route('/index.html')  
def home():
    return render_template('index.html')

@app.route('/works.html')  
def works():
    return render_template('works.html')

@app.route('/about.html')  
def about():
    return render_template('about.html')

@app.route('/contact.html')  
def contact():
    return render_template('contact.html')

@app.route('/components.html')  
def components():
    return render_template('components.html')



    

# if __name__ == '__main__':
#    app.run()

