1) [Anon Club site](https://youthful-minsky-60409b.netlify.app/):<br>
For this challenge inspect the _source code_ you'll get a part of the flag in index page and other parts in _css_ and _javascript_ comments.

2) [Agent](https://web-challenges-anonctf.000webhostapp.com/agent/):<br>
Change the user agent of your browser to _evilbrowser_ either [manually](https://www.howtogeek.com/113439/how-to-change-your-browsers-user-agent-without-installing-any-extensions/) or by using add-ons to your browser.

3) [Login](https://web-challenges-anonctf.000webhostapp.com/login/):<br>
If you try to login you'll notice the error message that you are not the admin. Open the developer tools check the cookies. Change the value of _admin cookie_ to _true_ and login again.

4) [Under Construction](https://web-challenges-anonctf.000webhostapp.com/underConstruction/):<br>
It's always good to check for _robots.txt_ file to see which path or file is not allowed to crawl by the search engines.

5) [Egallery](https://web-challenges-anonctf.000webhostapp.com/Egallery/):<br>
If you try to login to this site you get an error message saying Invalid Credentials. There must be some kind of check for credentials. Try sql injection.<br>
Use `' or true -- ` for the username. Which will always evaluate the condition to always true and the first entry of the sql table is returned.<br>
```MySQL
SELECT * FROM users WHERE username = 'admin' AND password = 'adminpassword'; -- This is a sql query
SELECT * FROM users WHERE username = '' or true -- AND password = '1234'; SQL injection, here everything after -- will considered a comment
```
