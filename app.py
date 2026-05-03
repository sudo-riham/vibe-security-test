from flask import Flask, request, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": "$999"},
    {"id": 2, "name": "Phone", "price": "$699"},
    {"id": 3, "name": "Tablet", "price": "$499"},
    {"id": 4, "name": "Headphones", "price": "$199"},
]

@app.route('/')
def home():
    return render_template(
        'index.html',
        query="",
        results=[],
        PRODUCTS=PRODUCTS
    )

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = [
        p for p in PRODUCTS
        if query.lower() in p['name'].lower()
    ]
    return render_template(
        'index.html',
        query=query,
        results=results,
        PRODUCTS=PRODUCTS
    )

@app.route('/health')
def health():
    return {"status": "healthy"}, 200
