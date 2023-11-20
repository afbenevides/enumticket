# Ticket numerotation tool

With this tool it is possible to add numbers to a ticket backgound image in order to create unique numbered tickets and lay the tickets down on a page of different preset sizes and then saved as a PDF ready to print.

This repo is based on the layout process that was automated by this interesting code available here: https://github.com/navegotel/enumticket and made by Markus Barth : https://github.com/navegotel

A templating layer was added to the base code via config.py files listing all parameters needed to automate the tickets creation.

Note that even the numbering order based on the assembly automation needed is parametrable. Thus stackorder is possible instead of sequential order.

## Installation

```bash
make install
```

## Create your private data project

i use another private repo to host the private data associated to a ticket version made. So you can do same by cloning your private repo.

```bash
git clone "adress of private repo" data
cp sample_config.py data/config.py
```

or simply create you folder and files locally

```bash
mkdir data
cp sample_config.py data/config.py
```
change values in data/config.py according to your needs.

## Run the script
In order to add numbers and make your ticket printing files:

```bash
make run
```
```
Tickets in preparation, please wait ...
Done! Thanks!
```



This should output a PDF (or multiple PDF with the bundle option to True) in data folder.


## Todo 
- Add explanations in config.py file on what parameter does what and what are the acceptable values for each
- Make different demo (raffle ticket with double number, concert ticket one number)
- Add some image demo of done tickets