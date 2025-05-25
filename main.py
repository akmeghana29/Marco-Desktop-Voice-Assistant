from app import app
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        from cli import run_assistant
        run_assistant()
    else:
        app.run(debug=True)
