# Ticket numerotation tool

With this tool it is possible to add numbers to a ticket backgound image in order to create unique numbered tickets and lay the tickets down on a page of different preset sizes and then saved as a PDF ready to print.

This repo is based on the layout process that was automated by this interesting code available here: https://github.com/navegotel/enumticket and made by Markus Barth : https://github.com/navegotel

A templating layer was added to the base code via config.py files listing all parameters needed to automate the tickets creation.

Note that even the numbering order based on the assembly automation needed is parametrable. Thus stackorder is possible instead of sequential order.

#Todo 
Add explanation in config.py file on what parameter does what and what are the acceptable values for each
make different demo (raffle ticket with double number, concert ticket one number)
put some image demo of done tickets