# Fixing Issue 6: Pytest Coverage For Password Validation

### **Password Validation Coverage**
- With password validation function it enforces security best practices, including minimum length and complexity requirements (uppercase, lowercase, numbers, and special characters).  
  See the code in [**`pass_val.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/utils/pass_val.py#L1-L18).

- When the password requirements aren't met, a HTTPException is raised with Error 400 to inform the user about not passing the password validation.
  See the code in [**`user_routes.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/app/routers/user_routes.py#L151-L155).

- Test Coverage for various password inputs edge cases are in [**`test_pass_val.py`**](https://github.com/digitalburritos/hw10_event_manager/blob/main/tests/test_pass_val.py#L1-L44).
