# Apartment-Management-DBMS_1

##### Step1: Clone repo.
```
git clone https://github.com/anmolharsh/Apartment-Management-DBMS_1.git
```

##### Step2: Installation

1. Install python virtual environment
```bash
cd Apartment-Management-DBMS_1
sudo apt-get install python3-venv  
```

2. Create a new virtual environment and activate it.
```bash
mkdir newenv
python3 -m venv newenv
source newenv/bin/activate
```

3. Install required packages and libraries
```bash
 cd Apartment_Management
 pip install django django-phonenumber-field phonenumbers image django-crispy-forms django-autofixture django-extensions wheel bootstrap4
 pip install django-bootstrap-datepicker-plus django-searchable-select django-bootstrap4
  ```
4. To create new admin(Manager)</br>
 ```bash
 python3 manage.py createsuperuser
  ``````
5. Execute the following command to run the server:
```bash
python3 manage.py runserver
```
6. Open the following address in your browser
```bash
http://127.0.0.1:8000/
```
