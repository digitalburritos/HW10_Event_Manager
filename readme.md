# Fixing Issue 5: Password Validation and Hashing

### **Password Validation Implementation**
- Added a password validation function to enforce security best practices, including minimum length and complexity requirements (uppercase, lowercase, numbers, and special characters).  
  See the code in [**`pass_val.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/utils/pass_val.py#L1-L18).

- When the password requirements aren't met, a HTTPException is raised with Error 400 to inform the user about not passing the password validation.
  See the code in [**`user_routes.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/routers/user_routes.py#L151-L155).


