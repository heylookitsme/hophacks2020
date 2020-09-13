# hophacks2020

Got the server, pages, and database parts to work, however, the CSS/JS needs some things not in the repo, so idk how well that works

Slight changes to login.html, register.html
  - changed the form attribute action to point towards the intended address (i.e. action="/login")
  - changed some id stuff, namely made the login rely on email rather than name, cause email is more unique than names irl
  
 New file structure is important, kept all the frontend stuff in /templates/ which is where Flask exclusively draws pages from
 
 current directories are
 
 - '/' - index
 - '/login' - login
 - '/register' - register
 - '/supplies' - requires log in, currently shows the supplies RAW
 - '/boler' - just something for testing, boiler.html
 - made a placeholder 404, 404err.html
