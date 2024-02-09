from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the clustered images data
clustered_df = pd.read_csv('clustered_images_data.csv')

@app.route('/')
def home():
    # Organize the data by clusters
    clusters = clustered_df.groupby('cluster_id').apply(lambda x: x.to_dict(orient='records')).to_dict()
    # Render the data to the HTML template
    return render_template('img_clusters.html', clusters=clusters)

if __name__ == '__main__':
    app.run()