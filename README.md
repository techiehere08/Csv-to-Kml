# CSV-to-KML
==========
This code is a nice simple application that will convert csv files with lat/longs into KML point files. There are some products out there, but I would like to make an open source program for those who only need to convert simple kml files. Enjoy its use and I appreciate any comments or help.

## How to use?
### You must have installed following things
> 1. Python
> 2. Pip3
> 3. Simplekml lib
> 4. Padas lib
> 5. tkinter lib
> 6. Google Earth or anyother alternative application( for Arch : Marbel)

## 1.Installing python
   ### For Debian based System
      ```
      sudo apt-get install python3
      ```
   ### For Arch based system
      ```
      sudo pacman -S python3
      ```
## 2.Installing pip3
   ### For Debian based System
      ```
      sudo apt-get -y install python3-pip
      ```
   ### For Arch based system
      ```
      sudo pacman -S python3-pip
      ```
## 3,4,5. For libs
   ```
   pip install (name of lib) 
   ```
## 6. Google Earth
   ### For Debian based System
      ```
      wget https://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb
      sudo dpkg -i google-earth-stable*.deb
      sudo apt-get -f install
      ```
   ### For Arch based system
      ```
      yaourt -S google-earth
      ```
      
## After installing all of the above
   #### run the csvtokmlgui.py via python3
    ``` python3 csvtokmlgui.py ```
   #### A file name gui.kml will be generate launch in via google earth.
   
   # Output
   ![OUTPUT](https://github.com/anandhere8/Csv-to-Kml/blob/master/output/github.png)
