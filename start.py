import sys
import os
import subprocess

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # Set PYTHONPATH and run uvicorn
    env = os.environ.copy()
    env['PYTHONPATH'] = project_root
    
    subprocess.run([
        'uvicorn', 'backend.main:app',
        '--host', '0.0.0.0',
        '--port', '8000'
    ], env=env)
