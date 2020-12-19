# STEPS FOR INITIATE

- Create a virtual environment

  `python -m venv your_virtual_environment`
  
- Activate your virtual environment

  - WINDOWS:
  
    `your_virtual_environment\Scripts\activate`

  - MAC o LINUX:
  
    `. your_virtual_environment/bin/activate`

    >If your virtual environment is activated you can see ***(your_virtual_environment) C:/...*** in your terminal

- When the VE is activated we have to install **requirements.txt**

  `pip install -r requirements.txt`

- Last step, we must to rename the file **config_.py** to **config.py** and fill the vars **SECRET_KEY** and **API_KEY**

- Now you're ready for launch! ***Enjoy***
