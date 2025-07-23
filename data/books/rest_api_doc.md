# 📘 REST API Documentation

## 🔗 Base URL
```
https://api.example.com/v1
```

---

## 📂 Endpoints

### ✅ GET /users
Fetch all users.

#### 🔸 Request
```
GET /users
```

#### 🔸 Query Parameters
| Name     | Type   | Required | Description              |
|----------|--------|----------|--------------------------|
| page     | int    | No       | Page number (default: 1) |
| limit    | int    | No       | Items per page           |

#### 🔸 Response (200 OK)
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
]
```

---

### 📄 GET /users/{id}
Get user by ID.

#### 🔸 Request
```
GET /users/{id}
```

#### 🔸 Path Parameters
| Name | Type | Required | Description  |
|------|------|----------|--------------|
| id   | int  | Yes      | User ID      |

#### 🔸 Response (200 OK)
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com"
}
```

---

### ✏️ POST /users
Create a new user.

#### 🔸 Request
```
POST /users
```

#### 🔸 Request Body
```json
{
  "username": "new_user",
  "email": "new_user@example.com",
  "password": "securePassword"
}
```

#### 🔸 Response (201 Created)
```json
{
  "id": 2,
  "username": "new_user",
  "email": "new_user@example.com"
}
```

---

### 🔄 PUT /users/{id}
Update an existing user.

#### 🔸 Request
```
PUT /users/{id}
```

#### 🔸 Path Parameters
| Name | Type | Required | Description  |
|------|------|----------|--------------|
| id   | int  | Yes      | User ID      |

#### 🔸 Request Body
```json
{
  "username": "updated_user",
  "email": "updated@example.com"
}
```

#### 🔸 Response (200 OK)
```json
{
  "id": 1,
  "username": "updated_user",
  "email": "updated@example.com"
}
```

---

### ❌ DELETE /users/{id}
Delete a user by ID.

#### 🔸 Request
```
DELETE /users/{id}
```

#### 🔸 Path Parameters
| Name | Type | Required | Description  |
|------|------|----------|--------------|
| id   | int  | Yes      | User ID      |

#### 🔸 Response (204 No Content)
No content returned.
