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

- Last step, we must to rename the file **config_.py** to **config.py** and fill the **API_KEY** var

  - For purchase an **API_KEY** we must to go to *<https://www.omdbapi.com/apikey.aspx>*

  - You can select *Become Patreon* or a free key *FREE*

  - Then, we must to put our email on the input box *EMAIL* and click on *SUBMIT* button

  - They send an email with our **API_KEY**

    - First of all, we must to activate the **KEY** with the url with the message:

      > *"Click the following URL to activate your key: ..."*

    - After that, we can use the KEY that they provide in the first line:

      > *"Here is your key: ..."*

  - Now we can fill the **API_KEY** var with the key

- Now you're ready for launch! ***Enjoy***
