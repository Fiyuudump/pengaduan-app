# Insomnia API Test Collection - Quick Start Guide

## File: Insomnia_P9_P10_API_Tests.yaml

Comprehensive API test collection for Framework Programming P9 & P10 implementation.

## 📋 What's Included

### Total Requests: 24+
Organized into 7 folders covering:
- ✅ P9: Authentication & Token Management
- ✅ P9: Permission Testing (IsAuthenticatedOrReadOnly, IsAuthenticated)
- ✅ P10: Pagination Testing
- ✅ P10: Search Functionality
- ✅ P10: Ordering/Sorting
- ✅ P10: Combined Query Parameters

---

## 🚀 Quick Start

### Step 1: Import Collection
1. Open Insomnia REST Client
2. Click on **Create** or **Import**
3. Select **From File**
4. Choose `Insomnia_P9_P10_API_Tests.yaml`
5. Collection will be imported with all requests organized in folders

### Step 2: Configure Environment
1. Click on the **Environment** dropdown (top left)
2. Select **Base Environment**
3. Update the following variables:
   ```json
   {
     "base_url": "http://127.0.0.1:8000",
     "username": "your_superuser_username",
     "password": "your_superuser_password",
     "auth_token": ""
   }
   ```
4. Save the environment

### Step 3: Get Authentication Token
1. Navigate to **P9 - Authentication** folder
2. Open **[P9] Get Authentication Token** request
3. Click **Send**
4. Copy the token from response:
   ```json
   {
     "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
   }
   ```
5. Go back to **Environment** settings
6. Paste the token into `auth_token` variable
7. Save the environment

### Step 4: Start Testing!
All requests are now ready to use. The token will be automatically included in requests that need authentication.

---

## 📁 Collection Structure

### 1️⃣ P9 - Authentication (1 request)
**Purpose**: Get authentication token for protected endpoints

| Request | Method | Auth Required |
|---------|--------|---------------|
| Get Authentication Token | POST | No |

**Expected Response**: 200 OK with token

---

### 2️⃣ P9 - Warga Permissions (6 requests)
**Purpose**: Test IsAuthenticatedOrReadOnly permission class

| Request | Method | Auth Required | Expected Result |
|---------|--------|---------------|-----------------|
| List Warga - Public Access | GET | No | 200 OK |
| Create Warga - No Auth | POST | No | 401 Unauthorized |
| Create Warga - With Auth | POST | Yes | 201 Created |
| Warga Detail - Public Access | GET | No | 200 OK |
| Update Warga - With Auth | PUT | Yes | 200 OK |
| Delete Warga - No Auth | DELETE | No | 401 Unauthorized |

**Key Learning**: Public can READ, only authenticated users can WRITE

---

### 3️⃣ P9 - Pengaduan Permissions (2 requests)
**Purpose**: Test IsAuthenticated permission class

| Request | Method | Auth Required | Expected Result |
|---------|--------|---------------|-----------------|
| List Pengaduan - No Auth | GET | No | 401 Unauthorized |
| List Pengaduan - With Auth | GET | Yes | 200 OK |

**Key Learning**: Only authenticated users can access (all methods)

---

### 4️⃣ P10 - Pagination (2 requests)
**Purpose**: Test PageNumberPagination feature

| Request | Query Params | Expected Result |
|---------|--------------|-----------------|
| Pagination - Page 1 | page=1 | First 10 items |
| Pagination - Page 2 | page=2 | Next 10 items |

**Response Structure**:
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/warga/?page=2",
  "previous": null,
  "results": [...]
}
```

---

### 5️⃣ P10 - Searching (5 requests)
**Purpose**: Test SearchFilter functionality

#### Warga Search Fields:
- `nama_lengkap` (full name)
- `nik` (ID number)
- `alamat` (address)

| Request | Query Params | Example |
|---------|--------------|---------|
| Search by Nama | search=Budi | Finds "Budi Santoso" |
| Search by NIK | search=3501234567890001 | Exact NIK match |
| Search by Alamat | search=Merdeka | Finds "Jl. Merdeka..." |

#### Pengaduan Search Fields:
- `judul` (title)
- `deskripsi` (description)

| Request | Query Params | Auth Required |
|---------|--------------|---------------|
| Search by Judul | search=jalan | Yes |
| Search by Deskripsi | search=rusak | Yes |

---

### 6️⃣ P10 - Ordering (5 requests)
**Purpose**: Test OrderingFilter functionality

#### Warga Ordering:
| Request | Query Params | Result |
|---------|--------------|--------|
| Order by Nama (A-Z) | ordering=nama_lengkap | Ascending |
| Order by Nama (Z-A) | ordering=-nama_lengkap | Descending |
| Order by Tanggal (Newest) | ordering=-tanggal_registrasi | Latest first |

#### Pengaduan Ordering:
| Request | Query Params | Auth Required |
|---------|--------------|---------------|
| Order by Status | ordering=status | Yes |
| Order by Tanggal (Newest) | ordering=-tanggal_lapor | Yes |

**Tip**: Use `-` prefix for descending order

---

### 7️⃣ P10 - Combined Queries (2 requests)
**Purpose**: Test multiple query parameters together

#### Example Combinations:
```
?search=a&ordering=nama_lengkap&page=1
```
- Search for "a"
- Order by nama_lengkap
- Show page 1

```
?search=jalan&ordering=-tanggal_lapor&page=1
```
- Search for "jalan"
- Order by tanggal_lapor (newest first)
- Show page 1

---

## 🎯 Testing Workflow

### Recommended Testing Order:

1. **Start Server**
   ```bash
   python manage.py runserver
   ```

2. **Get Token** (if not already done)
   - Run: [P9] Get Authentication Token
   - Update `auth_token` in environment

3. **Test Permissions** (P9)
   - Run all requests in "P9 - Warga Permissions"
   - Run all requests in "P9 - Pengaduan Permissions"
   - Observe 200 OK vs 401 Unauthorized responses

4. **Test Pagination** (P10)
   - Run: Pagination - Page 1
   - Check `count`, `next`, `previous` in response
   - Run: Pagination - Page 2 (if available)

5. **Test Searching** (P10)
   - Try different search terms
   - Test on both Warga and Pengaduan
   - Verify results match search criteria

6. **Test Ordering** (P10)
   - Try ascending and descending order
   - Verify order in response results
   - Test different fields

7. **Test Combined** (P10)
   - Run combined query requests
   - Modify parameters to test different combinations
   - Verify all features work together

---

## 💡 Tips & Tricks

### 1. Environment Variables
Use variables for flexible testing:
- `{{ _.base_url }}` - Base API URL
- `{{ _.auth_token }}` - Authentication token
- `{{ _.username }}` - Username for login
- `{{ _.password }}` - Password for login

### 2. Quick Token Refresh
If token expires or you need a new one:
1. Delete current token from environment
2. Run "Get Authentication Token" again
3. Update environment with new token

### 3. Testing Expected Failures
Requests marked "Should Fail" are intentional:
- They test security (401 responses)
- Verify permission classes work correctly
- Don't worry if you see red status codes!

### 4. Modify Requests
Feel free to customize:
- Change search terms in query params
- Try different ordering fields
- Adjust page numbers
- Modify request bodies for POST/PUT

### 5. Response Inspection
Check these in responses:
- ✅ Status codes (200, 201, 401, 404)
- ✅ Response body structure
- ✅ Pagination metadata (count, next, previous)
- ✅ Search results accuracy
- ✅ Ordering correctness

---

## 📊 Expected Response Codes

| Code | Meaning | When You'll See It |
|------|---------|-------------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 401 | Unauthorized | Missing or invalid token |
| 403 | Forbidden | Valid token but no permission |
| 404 | Not Found | Resource doesn't exist |

---

## 🐛 Troubleshooting

### Issue: All Requests Return 401
**Solution**: 
- Get new token via authentication endpoint
- Update `auth_token` in environment
- Make sure format is: `Token <your_token_here>` (not just the token)

### Issue: "Connection Refused"
**Solution**:
- Check if Django server is running
- Verify `base_url` in environment (should be `http://127.0.0.1:8000`)
- Make sure port 8000 is not blocked

### Issue: 404 Not Found
**Solution**:
- Check URL spelling
- Verify endpoint exists in Django URLs
- For detail endpoints, use existing ID (not 999)

### Issue: Search Returns Empty Results
**Solution**:
- Verify data exists in database
- Check search term spelling
- Try broader search terms (e.g., "a" instead of full name)

### Issue: Pagination Shows No Next Page
**Solution**:
- This is normal if you have < 10 items in database
- Add more data using `python populate_data.py`
- Or test with CREATE requests to add more items

---

## 🎓 Learning Objectives

By using this collection, you will understand:

### P9 Concepts:
- ✅ Token-based authentication flow
- ✅ Different permission classes (IsAuthenticated, IsAuthenticatedOrReadOnly)
- ✅ Public vs protected endpoints
- ✅ Role-based access control

### P10 Concepts:
- ✅ Pagination for large datasets
- ✅ Search functionality across multiple fields
- ✅ Dynamic ordering/sorting
- ✅ Combining query parameters
- ✅ RESTful API best practices

---

## 📝 Notes

- All requests use JSON format for request/response bodies
- Token format: `Authorization: Token <your_token>`
- Base URL can be changed for different environments
- Collection is designed for localhost testing
- Safe to experiment - uses test database

---

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. Review `IMPLEMENTATION_SUMMARY.md` for implementation details
3. Run `python test_api_features.py` for automated testing
4. Check Django server logs for errors
5. Verify database has data: `python populate_data.py`

---

**Happy Testing! 🚀**

Last Updated: November 12, 2025
