# Fastapi test

[![PyPI - Version](https://img.shields.io/pypi/v/fastapi-test.svg)](https://pypi.org/project/fastapi-test)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi-test.svg)](https://pypi.org/project/fastapi-test)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install fastapi-test
```

## Roadmap
Authentication:

* POST /auth/register: Register a new user.
* POST /auth/login: Login an existing user.
* POST /auth/logout: Logout the current user.
* GET /auth/me: Get the authenticated user's information.

User Management:

* GET /users: Get a list of users.
* GET /users/{id}: Get a user's information by ID.
* PUT /users/{id}: Update a user's information.
* DELETE /users/{id}: Delete a user's account.
* GET /users/{id}/followers: Get a list of a user's followers.
* GET /users/{id}/following: Get a list of users the user is following.
* POST /users/{id}/follow: Follow a user.
* DELETE /users/{id}/unfollow: Unfollow a user.

Posts:

* GET /posts: Get a list of posts.
* POST /posts: Create a new post.
* GET /posts/{id}: Get a post's information by ID.
* PUT /posts/{id}: Update a post's information.
* DELETE /posts/{id}: Delete a post.
* GET /users/{id}/posts: Get a user's posts.

Comments:

* GET /posts/{id}/comments: Get a list of comments for a post.
* POST /posts/{id}/comments: Create a new comment on a post.
* GET /comments/{id}: Get a comment's information by ID.
* PUT /comments/{id}: Update a comment's information.
* DELETE /comments/{id}: Delete a comment.

Likes:

* POST /posts/{id}/like: Like a post.
* DELETE /posts/{id}/unlike: Unlike a post.
* GET /posts/{id}/likes: Get a list of users who liked a post.
* POST /comments/{id}/like: Like a comment.
* DELETE /comments/{id}/unlike: Unlike a comment.
* GET /comments/{id}/likes: Get a list of users who liked a comment.

Messaging:

* GET /conversations: Get a list of user's conversations.
* POST /conversations: Start a new conversation.
* GET /conversations/{id}: Get a conversation's details.
* GET /conversations/{id}/messages: Get a list of messages in a conversation.
* POST /conversations/{id}/messages: Send a message in a conversation.
* PUT /messages/{id}: Update a message's information.
* DELETE /messages/{id}: Delete a message.

Notifications:

* GET /notifications: Get a list of user's notifications.
* PUT /notifications/{id}: Update a notification's status (e.g., read/unread).
* DELETE /notifications/{id}: Delete a notification.

Search:

* GET /search/users: Search for users based on query parameters.
* GET /search/posts: Search for posts based on query parameters.

## License

`fastapi-test` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
