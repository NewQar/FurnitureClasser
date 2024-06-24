from flask import Flask, render_template, request, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('MainPage.html')

@app.route('/search', methods=['POST'])
def search():
    # Retrieve the search query from the form
    search_query = request.form['search_query']
    
    # Execute the Part3.py script passing the search query as an argument
    subprocess.run(['python', 'C:/Users/User/Downloads/GroupAssignmentAiCSC577/Part3.py', search_query])
    
    # Redirect to the checkout page or any other page you want to display after the search
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    return render_template('CheckoutPage.html')

if __name__ == '__main__':
    app.run()
