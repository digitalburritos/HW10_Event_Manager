# Fixing Issue 4: Username Validation
***

### **Email Uniqueness Validation**
- Implemented a check to ensure that the email address used for registration is unique to each user. This is enforced during the user creation process in the `create_user` function, where the system verifies if the provided email already exists in the database before allowing the registration to proceed. Using an email as a username ensures uniqueness and integrity.  
  See the code in [**`user_routes.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/routers/user_routes.py#L142-L146).



