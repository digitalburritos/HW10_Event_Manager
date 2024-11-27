# Fixing Issue 2: Nickname Does Not Match
***

### **Nickname Handling**
- Added logic to generate a nickname if the user does not provide one.  
  See the code in [**`user_routes.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/routers/user_routes.py#L146-L150).

---

### **Custom Exception for Nickname Uniqueness**
- Introduced a `NicknameAlreadyTakenError` exception when a user tries to register with an already taken nickname.  
  See the code in [**`user_service.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/services/user_service.py#L70-L87).

---

### **Nickname Validation**
- If a nickname is provided, the system checks its availability.  
- If no nickname is provided, a unique one is generated.  
  See the code in [**`user_service.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/services/user_service.py#L63-L70).

