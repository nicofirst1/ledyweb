Please clone this project and install all the dependencies through
<br>`pip install -r requirements.txt`<br>
then to run on 8000 port just run<br>
`python3 manage.py runserver`<br> then visit
http://127.0.0.1:8000
<br>
or to run on any specified port like 2222<br>
`python3 manage.py runserver 0.0.0.0:2222`
http://127.0.0.1:2222
to run on port 80 and 443 you need sudo access<br>
`sudo python3 manage.py runserver 0.0.0.0:80` <br>
to pass any addition arguments to web please set them as environment variables before runing the program via above commands
 
`export var_name="My value"` 

and to get these value i have written function in 
`Home/views.py -> get_val_from_env` and pass variable as arg
`get_val_from_env('var_name')`

`templates/home/index.html` is html file you want to change in case

all the functions are in `Home/views.py`
you can write you own code within them
 you can import scripts as well and use them in functions
 
 make sure you have <b>python3<b> installed.
 and if any issues please get back to me.
 
# todo
- fix readme []
- fix double call in get_form_values []
- fix compatibility with controller []
- fix android app []
- []