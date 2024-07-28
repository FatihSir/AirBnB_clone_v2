# 0x04. AirBnB clone - Web framework
![airbnb](1.jpeg)

Welcome to the Airbnb Clone project! This web application is a simplified version of the popular vacation rental platform, Airbnb. It is built using modern web development frameworks and technologies to provide a comprehensive and functional example of a full-stack web application.


## Resource :
[What is a web framework is ?](https://www.intelegain.com/what-are-web-frameworks-and-why-you-need-them)

## Tasks
#### 0. Hello Flask!

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
- You must use the option `strict_slashes=False` in your route definition

```shell
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
```
##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `0-hello_route.py`, `__init__.py`

#### 1. HBNB
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
    - /hbnb: display “HBNB”
- You must use the option `strict_slashes=False` in your route definition

```shelll
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
```

##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `1-hbnb_route.py`

#### 2. C is fun!
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
    - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
- You must use the option `strict_slashes=False` in your route definition

```shell
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```
##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `2-c_route.py`

#### 3. Python is cool!
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
    - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
        - The default value of `text` is “is cool”
- You must use the option `strict_slashes=False` in your route definition

```shell
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
```
##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `3-python_route.py`

#### Is it a number?
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
    - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
        - The default value of `text` is “is cool”
    - `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
- You must use the option `strict_slashes=False` in your route definition

```shell
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```
##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `4-number_route.py`

#### 5. Number template
Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
    - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
    - `/python/<text>`: display “Python ”, followed by the value of the `text` variable (replace underscore _ symbols with a space )
        - The default value of `text` is “is cool”
    - `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
    - `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
        - H1 tag: “Number: n” inside the tag BODY
- You must use the option `strict_slashes=False` in your route definition

```shell
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```shell
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```
##### Repo:

- GitHub repository: `AirBnB_clone_v2`
- Directory: `web_flask`
- File: `5-number_template.py`, `templates/5-number.html`

