from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the clustered articles data
clustered_df = pd.read_csv('clustered_articles.csv')

@app.route('/')
def home():
    # Convert the DataFrame to a dictionary format that the template can understand
    clusters = clustered_df.groupby('prediction').apply(lambda x: x.to_dict(orient='records'))
    return render_template('clusters.html', clusters=clusters)

if __name__ == '__main__':
    app.run(debug=True)

