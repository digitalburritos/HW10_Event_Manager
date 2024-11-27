# Fixing Issue 3: LinkedIn and GitHub URLs Null
***

### **Ensure LinkedIn and GitHub Links are not Null in Response Body**
- Inlcuded the links in response body whenever a new user is created.  
  See the code in [**`user_routes.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/routers/user_routes.py#L162-L178).

---

### **Added Validation for Links**
- Make sure user links match the specified formats.  
  See the code in [**`user_schemas.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/schemas/user_schemas.py#L24-L54).


