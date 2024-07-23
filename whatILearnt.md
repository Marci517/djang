# Information about my learning process

## The tutorial I followed: https://youtu.be/rHux0gMZ3Eg?si=pBwhvKtiC43VjjhE

### Project setup

**Python and Django**

As the tutorial showed me I did the same, and set up my first django project.

- interpreter
- integrated terminal
- environment
- etc.

### App

I created my first app named as 'playeground'

### View/ api call

I created the first view, basically I send back a basic html or render a template

### Mapping URL

I had to map the url for the previous view

Now also you can try the following request: http://127.0.0.1:8000/playground/hello/

### Templates

I also created a basic template which I can render, also I can use variables in the template (dinamically).

### Debugging

I also learnt about the django debugging method and after that I set up the Django Debug Toolbar

### ORM

I learnt about models, relation between them and implement them.

Now I can use Django admin for CRUD in database

I made a basic library system, where are these api calls/ requests:

- get a book by name.
- get books from specific author
- get books by category name.

**Usage:**

127.0.0.1:8000/books/getBookByName/example
127.0.0.1:8000/books/getBooksByCategory/example
127.0.0.1:8000/books/getBooksByAuthor/example

In my database are:

- book titles: IDK, The Tree, Bear, Wolf

- book categories: comic, horror, historical

- author names: Istvan, Marci, Ali

(also there are book descriptions and author ages, but these do not matter when you make the requests)
