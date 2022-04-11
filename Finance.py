from flask import Flask, url_for, render_template, request, Markup

import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/D")
def render_Definition():
    return render_template('Definition.html')    

@app.route("/")
def render_main():
    return render_template('Main.html')   
    
@app.route("/Data")
def Alabama_Finance_Data():
    
    with open('finance.json') as finance_data:
        Alabama = json.load(finance_data)
    states=[]
    for c in Alabama:
       
        if c ["State"] == "ALABAMA" and c ["Year"] == 2019:
            return render_template('page1.html',co= c ["Totals"] ["Capital outlay"],r= c["Totals"]["Revenue"],e= c["Totals"]["Expenditure"]
            ,ge= c["Totals"]["General expenditure"],gr=c["Totals"]["General revenue"],itr=c["Totals"]["Insurance trust  revenue"],i= c["Totals"]["Intergovernmental"],t= c["Totals"]["Tax"])
            
  


    

   
   
if __name__=="__main__":
    app.run(debug=False)

 
