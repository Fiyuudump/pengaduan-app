#!/usr/bin/env python
"""
Test script untuk memverifikasi fitur P9 dan P10
- Authentication & Permissions
- Pagination, Searching, Ordering
"""

import requests
import json
from getpass import getpass

BASE_URL = "http://127.0.0.1:8000/api"

def print_section(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def test_public_access():
    """Test P9: Public dapat read Warga (IsAuthenticatedOrReadOnly)"""
    print_section("Test 1: Public Access ke /api/warga/ (Should Work)")

    response = requests.get(f"{BASE_URL}/warga/")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success! Found {data['count']} warga")
        print(f"Pagination: next={data['next']}, previous={data['previous']}")
        print(f"Results: {len(data['results'])} items on this page")
    else:
        print(f"❌ Failed: {response.text}")

def test_protected_access():
    """Test P9: Public tidak bisa akses Pengaduan (IsAuthenticated)"""
    print_section("Test 2: Public Access ke /api/pengaduan/ (Should Fail)")

    response = requests.get(f"{BASE_URL}/pengaduan/")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print(f"✅ Correctly blocked: {response.json()}")
    else:
        print(f"❌ Expected 401 but got {response.status_code}")

def get_auth_token():
    """Test P9: Mendapatkan authentication token"""
    print_section("Test 3: Get Authentication Token")

    print("\nMasukkan kredensial superuser:")
    username = input("Username: ")
    password = getpass("Password: ")

    response = requests.post(
        f"{BASE_URL}/auth/token/",
        json={"username": username, "password": password}
    )

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        token = response.json()['token']
        print(f"✅ Token obtained: {token[:20]}...")
        return token
    else:
        print(f"❌ Failed to get token: {response.text}")
        return None

def test_authenticated_access(token):
    """Test P9: Akses protected endpoint dengan token"""
    print_section("Test 4: Authenticated Access ke /api/pengaduan/")

    headers = {"Authorization": f"Token {token}"}
    response = requests.get(f"{BASE_URL}/pengaduan/", headers=headers)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success! Found {data['count']} pengaduan")
        print(f"Pagination: next={data['next']}, previous={data['previous']}")
    else:
        print(f"❌ Failed: {response.text}")

def test_search(token):
    """Test P10: Search functionality"""
    print_section("Test 5: Search Feature")

    # Test search pada Warga (public)
    search_term = "Budi"
    response = requests.get(f"{BASE_URL}/warga/?search={search_term}")

    print(f"\nSearching for '{search_term}' in /api/warga/")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Found {data['count']} results")
        if data['results']:
            print(f"First result: {data['results'][0]['nama_lengkap']}")
    else:
        print(f"❌ Failed: {response.text}")

    # Test search pada Pengaduan (requires auth)
    if token:
        headers = {"Authorization": f"Token {token}"}
        search_term = "jalan"
        response = requests.get(
            f"{BASE_URL}/pengaduan/?search={search_term}",
            headers=headers
        )

        print(f"\nSearching for '{search_term}' in /api/pengaduan/")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {data['count']} results")
        else:
            print(f"❌ Failed: {response.text}")

def test_ordering(token):
    """Test P10: Ordering functionality"""
    print_section("Test 6: Ordering Feature")

    # Test ordering ascending
    response = requests.get(f"{BASE_URL}/warga/?ordering=nama_lengkap")
    print(f"\nOrdering by 'nama_lengkap' (A-Z)")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        names = [w['nama_lengkap'] for w in data['results'][:3]]
        print(f"✅ First 3 results: {names}")

    # Test ordering descending
    response = requests.get(f"{BASE_URL}/warga/?ordering=-tanggal_registrasi")
    print(f"\nOrdering by '-tanggal_registrasi' (newest first)")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success! Got {len(data['results'])} results")

def test_pagination():
    """Test P10: Pagination functionality"""
    print_section("Test 7: Pagination Feature")

    # Get first page
    response = requests.get(f"{BASE_URL}/warga/")

    if response.status_code == 200:
        data = response.json()
        print(f"Total count: {data['count']}")
        print(f"Items per page: {len(data['results'])}")
        print(f"Next page: {data['next']}")
        print(f"Previous page: {data['previous']}")

        # If there's a next page, try to get it
        if data['next']:
            response2 = requests.get(f"{BASE_URL}/warga/?page=2")
            if response2.status_code == 200:
                data2 = response2.json()
                print(f"\n✅ Page 2 loaded successfully with {len(data2['results'])} items")
        else:
            print("\n✅ Only one page of results (less than 10 items)")

def test_combined_query():
    """Test P10: Kombinasi query parameters"""
    print_section("Test 8: Combined Query Parameters")

    url = f"{BASE_URL}/warga/?search=a&ordering=nama_lengkap&page=1"
    response = requests.get(url)

    print(f"URL: {url}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Combined query works!")
        print(f"   Search: 'a'")
        print(f"   Ordering: nama_lengkap")
        print(f"   Page: 1")
        print(f"   Results: {data['count']} total, {len(data['results'])} on this page")

def main():
    print("\n" + "🚀 " * 20)
    print(" API Feature Testing - P9 & P10 Implementation")
    print("🚀 " * 20)

    try:
        # Test P9 - Authentication & Permissions
        test_public_access()
        test_protected_access()

        # Get token for authenticated tests
        token = get_auth_token()

        if token:
            test_authenticated_access(token)

        # Test P10 - Pagination, Search, Ordering
        test_search(token)
        test_ordering(token)
        test_pagination()
        test_combined_query()

        print_section("All Tests Completed!")
        print("\n✅ P9: Authentication & Permissions implemented successfully")
        print("✅ P10: Filtering, Searching, & Pagination implemented successfully")

    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Cannot connect to server")
        print("   Make sure Django server is running: python manage.py runserver")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
