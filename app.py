from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple in-memory "database" for demo purposes
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": "$999"},
    {"id": 2, "name": "Phone", "price": "$699"},
    {"id": 3, "name": "Tablet", "price": "$499"},
    {"id": 4, "name": "Headphones", "price": "$199"},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Vibe Store</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        input { padding: 8px; width: 300px; margin-right: 10px; }
        button { padding: 8px 16px; background: #007bff; color: white; border: none; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #f4f4f4; }
        .no-results { color: #999; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Vibe Store</h1>
    <p>Search for products below:</p>

    <form method="GET" action="/search">
        <input 
            type="text" 
            name="q" 
            placeholder="Search products..." 
            value="{{ query }}">
        <button type="submit">Search</button>
    </form>

    {% if query %}
        <p>Results for: <strong>{{ query }}</strong></p>
        {% if results %}
            <table>
                <tr>
                    <th>ID</th>
                    <th>Product</th>
                    <th>Price</th>
                </tr>
                {% for product in results %}
                <tr>
                    <td>{{ product.id }}</td>
                    <td>{{ product.name }}</td>
                    <td>{{ product.price }}</td>
                </tr>
                {% endfor %}
            </table>
        {% else %}
            <p class="no-results">No products found for "{{ query }}"</p>
        {% endif %}
    {% else %}
        <table>
            <tr><th>ID</th><th>Product</th><th>Price</th></tr>
            {% for product in PRODUCTS %}
            <tr>
                <td>{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>{{ product.price }}</td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
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
    return render_template_string(
        HTML_TEMPLATE,
        query=query,
        results=results,
        PRODUCTS=PRODUCTS
    )

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
