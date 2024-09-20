from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('Project_9/cosine_item_similarity_svd.pkl', 'rb') as file:
    cosine_item_similarity_svd = pickle.load(file)

with open('Project_9/user_item_matrix_svd.pkl', 'rb') as file:
    user_item_matrix_svd = pickle.load(file)



if __name__ == '__main__':
    app.run(debug=True)
