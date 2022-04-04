from flask import Flask, url_for, render_template, request, Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('page1.html')    
    
def Alabama_Finance_Data():
    
    with open('finance.json') as finance_data:
        Alabama = json.load(finance_data)
    states=[]
    for c in Alabama:
       
        if c ["State"] == "ALABAMA" and c ["Year"] == 1992:
            
    


    
@app.route("/Data")
def render_response():
   
   
        if __name__=="__Main__":
        app.run(debug=False)

 
