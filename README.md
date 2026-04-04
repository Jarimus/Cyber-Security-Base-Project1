# Cyber Security Base: Project

## Features
- An app for storing notes
- Notes are separate for each registered users
- Notes are searchable.

## Vulnerabilities

### Flaw 1: SQL-injection
- A03: Injection
- Dynamic queries or non-parameterized calls without context-aware escaping are used directly in the interpreter.
- Search function does not sanitize user input.
- [Fix location](./notes/views.py#L23)


### Flaw 2: URL-tampering
- A01: Broken Access Control
- Permitting viewing or editing someone else's account, by providing its unique identifier
- no 'login_required()' for detail.html
- [Fix location](./notes/views.py#L50)


### Flaw 3: Strong passwords are not enforced
- A07: Identification and authentication failures
- Permits default, weak, or well-known passwords, such as "Password1" or "admin/admin".
- Password validators disabled in the project settings.py
- [Fix location](./SecBaseProject/settings.py#L76)


### Flaw 4: Stored XSS
- User can write in a note's content scripts that can harm the system.
- CWE-80: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)


### Flaw 5: Debug on (Too much detail about the inner workings of the server)
- A05: Security Misconfiguration
- Error handling reveals stack traces or other overly informative error messages to users.
- Leave debug on
- [Fix location](./SecBaseProject/settings.py#L20)