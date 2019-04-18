from flask import Flask, render_template, request

 
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
 
    midinumber = ''
    notename = ''
    freq = ''
    note_name = ("C","C#","D","D#","E","F","F#","G","G#","A","A#","B") #タプル
 
    if request.method == 'POST':
        text = request.form['text']
        midinumber = int(text)

        note = midinumber % 12 #ノート判定
        frequency = 440 *(pow (2 , (midinumber - 69) / 12))#周波数 f= 440×2(d-69)/12

        notename = note_name[note]
        freq = str('{:.2f}'.format(frequency))
 
        return render_template('index.html', midinum=midinumber , notename=notename , freq=freq)
     
    return render_template('index.html', midinum=midinumber , notename=notename , freq=freq)
 
 
if __name__ == "__main__":
    app.run(debug=True)