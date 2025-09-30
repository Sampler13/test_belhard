from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='34.118.26.67', port=5000, debug=True)