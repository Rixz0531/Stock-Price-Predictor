from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
 
    data = [0, 10, 15, 8, 22, 18, 25]
 
    return render_template(template_name_or_list='index.html', data=data, labels=labels)


if __name__=="__main__":
    app.run(debug=True)
