## Electricity Bill Splitter and Automatic Database Updater using tkinter and sqlite3

You need to install ```tkinter``` and ```python3``` in your computer before running the python code. For that, run the following commands in your terminal:
```
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install python3-pil.imagetk
```

After that, you just need to run the ```minor_project_db.py``` only once and for all in your computer, to create the database file.
After that, everytime you run the ```minor_project.py``` file, the database will automatically get updated. However, you must be careful the database file does not get deleetd from your computer.

***Remeber***: 
* You need to change the path of the database to a directory of your computer from what is already there in the code (```minor_project_db.py```).
         
* Incase the database file gets deleted ever in future, you just need to update the table in the code (```minor_project_db.py```) with values when last time bill was paid, and then run the file just once. Then again in future, this file is not needed to be run. The ```minor_project.py``` will automatically update the database with the current readings given as input.
