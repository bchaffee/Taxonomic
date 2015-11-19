Taxonomical Catalog Program version 1.0 11/16/2015

Name: Brandon Chaffee
Number: (415)720-4705
Email: Brandon Chaffee

General Usage Notes
---------------------------------------------------
-This program is used to implement a catalog of taxonomical kingdom, and their corresponding phyla. The program consist of 3 python files, two directories and 1 json. The python files are used to create the database, add items to the database and establish the server side functionality of the catalog. The two directories, static and templates. Static contains the static stylistic components of the catalog. Templates contain the html files for each of the catalog routes. client_secrets.json is necessary for the oauth functionality for the google+ login in.


Running the Program
---------------------------------------------------
-To run the Taxonomic Program please do the following:
1. Install Vagrant 1.1.4
2. Install VirtualMachine or similar application
3. Open a new terminal shell
4. Within the terminal shell, run the command: vagrant Up
--This command powers up the virtual machine
5. Once Vagrant has finished installing, run the command: vagrant ssh
--This command logs into the virtual machine
6. Once logged into the virtual machine, navigate to the taxonomic folder
--This can be done by running the prompt: cd vagrant/taxonomic
7. Once in the linked taxonomic folder, run the command: python database_setup.py
8. Follow the previous command with: python phyla.py
--Should this run without errors, the message: added Kingdoms and Phyla items!
9. Finally, run the command: python project.py
10. Once all three shell commands have been entered, navigate to a web browser
11. Within the web browser, naivagate to http:localhost:5000
12. From localhost:5000, login and reading functionality should appear

Required Software
---------------------------------------------------
-Python 2.x
-Texteditor
-Vagrant
-VirtualMachine
--Web Browser
--Access to open localhost:5000

Required Login
---------------------------------------------------
-Google+ or Gmail account for CRUD capabilities
--Note: this is not required for reading purposes