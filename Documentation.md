# Polling API Detailed Documentation

## Authentication (`/auth.py`)

### Register User (`/auth.py`)

- **Endpoint:** `/auth/register`
- **HTTP Method:** POST
- **Request Headers:**
  - `Content-Type: application/json`
- **Response Headers:**
  - `Content-Type: application/json`
- **Media Type:** application/json
- **Request Body Format:** 

```json
{
  "username": "newUser",
  "password": "password123",
  "email": "user@example.com",
  "firstName": "First",
  "lastName": "Last"
}

```
### Registers a new user with provided details. 
**Code ** (`/auth.py`):

```python
@auth_bp.route("/auth/register", methods=["POST"])
def register():
    # Parses registration details from incoming json request
    register_dto = RegisterDto.from_json(request.json)
    # Creates a new user in the database
    User.prisma().create(data=register_dto.to_insertable())
    # Returns HTTP status 201 to indicate successful creation with no body
    return Response(status=201)
```
**Response Body Format:** HTTP 201 (Created), no body for successful registration.

**Error Conditions:**

- `BadRequest("username not unique")`: Returned if the username already exists, along with HTTP status 400.

**User Login (/auth.py)**

- **Endpoint:** `/auth/login`
- **HTTP Methods:** POST
- **Request Headers:** Content-Type: application/json
- **Response Headers:** Content-Type: application/json
- **Media Type:** application/json
- **Request Body Format:**
```json
{
  "username": "newUser",
  "password": "password123"
}
```
Attempts to log in with the specified username and password.

**Code** (`/auth.py`):
```python
@auth_bp.route("/auth/login", methods=["POST"])
def login():
    login_dto = LoginDto.from_json(request.json)
    user = User.prisma().find_first(where={"username": login_dto.username})
    if user and login_dto.verify(user.hash):
        token = JWTService.create_token({"sub": user.id, "username": user.username})
        return make_response({"access_token": token})
    raise Unauthorized("unauthorized request")
```
**Response Body Format:**

```json
{
  "access_token": "eyJhbG..."
}
```
Provides a JWT token for authenticated sessions.

**Error Conditions:**

- `Unauthorized("unauthorized request")`: If the username or password is incorrect, along with HTTP status 401.

**Poll Items (/poll_items.py)**

- **Creating a Poll Item (/poll_items.py)**
  - **Endpoint:** `/pollitems`
  - **HTTP Methods:** POST
  - **Request Headers:** Authorization: Bearer `<token>`
  - **Response Headers:** Content-Type: application/json
  - **Media Type:** application/json
  - **Hypermedia Implementation:** Not specified.
  - **Request Body Format:**

```json
{
  "pollId": "poll123",
  "description": "Favorite programming language?"
}
```
Creates a poll item under the specified poll.

Code (`/poll_items.py`):
```python
@poll_items_bp.route("", methods=["POST"])
def post():
    pollitem_dto = PollItemDto.from_json(request.json)
    poll_item = PollItem.prisma().create(data=pollitem_dto.to_insertable())
    return make_response(poll_item.model_dump(exclude=["poll"]), 201)
```
**Response Body Format:**
```json
{
  "id": "item456",
  "description": "Favorite programming language?",
  "votes": 0
}
```
Confirms the creation of the poll item.

**Error Conditions:**

- `NotFound("user has no polls matching given id")`: If no matching poll is found, along with HTTP status 404.

**Polls (/polls.py)**

- **Creating a Poll (/polls.py)**
  - **Endpoint:** `/polls`
  - **HTTP Methods:** POST
  - **Request Headers:** Authorization: Bearer `<token>`
  - **Response Headers:** Content-Type: application/json
  - **Media Type:** application/json
  - **Hypermedia Implementation:** Not specified.
  - **Request Body Format:**
```json
{
  "title": "Finnish Election",
  "description": "A poll to determine the best candidate according to voters",
  "expires": "2024-12-31T23:59:59Z",
  "multipleAnswers": true,
  "private": false
}
```
**Code ** (/polls.py):
```python
@polls_bp.route("", methods=["POST"])
def post():
    poll_dto = PollDto.from_json(request.json)
    poll = Poll.prisma().create(data=poll_dto.to_insertable())
    return make_response(poll.model_dump(exclude=["user", "items"]), 201)
```
Creates a new poll with the specified attributes and returns its details.

**Response Body Format:**
```json
{
  "poll_id": "poll789",
  "title": "Best Condidate"
}
```
Acknowledges the creation of the poll with its ID and title.

**Error Conditions:**

- `BadRequest`: If required fields are missing in the request body, along with HTTP status 400.
- `Unauthorized`: If the user is not authenticated or lacks permission to create a poll, along with HTTP status 401.
