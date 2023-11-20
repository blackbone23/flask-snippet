installation : 

- create folder "upload" on project root folder
- rename .env_default to .env
- add JWT_SECRET value inside .env file
- go to project root folder on terminal, make sure install virtualenv
    - run : virtualenv env
    - run : source env/bin/activate
    - run : 
        - pip install -r path/to/requirements.txt 
        or 
        - pip3 install -r path/to/requirements.txt


db migration : 
- fill database config on .env
- on terminal
    - run : flask db migrate -m 'comment'
    - run: flask db upgrade