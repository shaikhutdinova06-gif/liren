import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Also add backend directory to path
backend_dir = os.path.join(project_root, 'backend')
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

if __name__ == "__main__":
    import uvicorn
    from main import app
    uvicorn.run(app, host="0.0.0.0", port=8000)
