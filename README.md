# oats
Threading security

## Windows Network User Scanner

This tool scans the Windows network every second to look for new users. If a new user is detected, it displays a message:
```
new user detected and directed
```
If the new user is not the current user (me), the tool will delete the user from the network.

### Example Python Implementation

Below is a conceptual Python script for such a tool (requires `pywin32` and admin privileges):

```python
import time
import getpass
import win32net
import win32netcon

def get_network_users():
    # Retrieves list of users on the local computer (can be adapted for domain)
    resume = 0
    users = []
    while True:
        try:
            user_list, total, resume = win32net.NetUserEnum(
                None,
                0,
                win32netcon.FILTER_NORMAL_ACCOUNT,
                resume
            )
            users += [u['name'] for u in user_list]
            if resume == 0:
                break
        except Exception as e:
            print("Error retrieving users:", e)
            break
    return set(users)

def delete_user(user):
    try:
        win32net.NetUserDel(None, user)
        print(f"Deleted user: {user}")
    except Exception as e:
        print(f"Failed to delete user {user}: {e}")

def main():
    me = getpass.getuser()
    seen_users = get_network_users()
    while True:
        time.sleep(1)
        current_users = get_network_users()
        new_users = current_users - seen_users
        for user in new_users:
            print("new user detected and directed")
            if user != me:
                delete_user(user)
        seen_users = current_users

if __name__ == "__main__":
    main()
```

**Note:**  
- This example works on local machine accounts. For network/domain users, adapt code to use domain queries and permissions.
- Requires Administrator privileges.
- Deleting users from a network/domain may have serious consequences; use with caution!
- Use in a controlled/test environment only.
