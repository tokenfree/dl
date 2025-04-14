from app import app

if __name__ == "__main__":
    # Enable debug mode only in development
    # For production deployment, debug should be False
    app.run(host="0.0.0.0", port=5000, debug=False)
