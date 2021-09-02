from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('index.html', color1 = "red", color2 = "black", columns = 4, rows =4, counter=0)  
    
@app.route('/4')                           
def hello_world2():
    return render_template('index.html', color1 = "red", color2 = "black", columns = 4, rows =2, counter=0)  

@app.route('/<x>/<y>')                           
def hello_world3(x,y):
    return render_template('index.html', color1 = "red", color2 = "black", columns = int(x), rows =int(y), counter=0)  



if __name__=="__main__":
    app.run(debug=True)     