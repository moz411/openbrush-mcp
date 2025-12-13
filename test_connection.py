#!/usr/bin/env python3
"""
Test script to check connection to Open Brush API
"""

import httpx
import sys

API_BASE_URL = "http://localhost:40074/api/v1"

def test_connection():
    """Test connection to Open Brush API"""
    print("🔍 Testing connection to Open Brush API...")
    print(f"📡 URL: {API_BASE_URL}")
    print()
    
    try:
        # Test 1: Check that API responds
        print("1️⃣ Connectivity test...")
        response = httpx.get(API_BASE_URL, params={"help": ""}, timeout=5.0)
        response.raise_for_status()
        print("   ✅ API accessible!")
        print()
        
        # Test 2: Test a simple command
        print("2️⃣ Testing simple command (undo)...")
        response = httpx.get(API_BASE_URL, params={"undo": ""}, timeout=5.0)
        response.raise_for_status()
        print("   ✅ Command executed successfully!")
        print(f"   📄 Response: {response.text[:100]}...")
        print()
        
        # Test 3: Get help
        print("3️⃣ Retrieving help...")
        response = httpx.get(API_BASE_URL, params={"help": ""}, timeout=5.0)
        if response.status_code == 200:
            print("   ✅ Help page available!")
            print(f"   📄 Response size: {len(response.text)} characters")
        print()
        
        print("=" * 60)
        print("✨ All tests passed!")
        print("=" * 60)
        print()
        print("The MCP server should work correctly.")
        print("You can now:")
        print("  1. Configure Claude Desktop with this server")
        print("  2. Run: python openbrush_mcp_server.py")
        
        return True
        
    except httpx.ConnectError:
        print("   ❌ Cannot connect to API")
        print()
        print("Check that:")
        print("  • Open Brush is running")
        print("  • HTTP API is enabled in settings")
        print("  • Port 40074 is being used")
        return False
        
    except httpx.HTTPError as e:
        print(f"   ❌ HTTP Error: {e}")
        return False
        
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
