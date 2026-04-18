#!/usr/bin/env python3

# Simple test to check if the app loads properly
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
    print("SUCCESS: App imported successfully")
    
    # Test app configuration
    with app.test_client() as client:
        response = client.get('/')
        print(f"GET / Status: {response.status_code}")
        if response.status_code == 200:
            print("SUCCESS: Basic route works")
        else:
            print(f"ERROR: Basic route failed with status {response.status_code}")
            print(f"Response: {response.data}")
            
except Exception as e:
    print(f"ERROR: Failed to import or run app: {str(e)}")
    import traceback
    traceback.print_exc()
