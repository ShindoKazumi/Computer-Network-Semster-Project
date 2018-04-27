# Computer-Network-Semester-Project
This project needs to run in three separate hosts
# Need to install all required packages and run topology. There are two options.
# Option 1: 
    #1 Download update.sh and topo.sh files
    #2 On mininet run:
                        ./update.sh
# Option 2:
    #1 First update using:
                            sudo apt-get update
    #2 Install 'pip' by using: 
                            sudo apt-get install python-pip python-dev build-essential
    #3 Install 'pdftotext' using:
                            sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev
                            sudo pip install pdftotext
    #4 Install 'getch' using:
                            sudo pip install py-getch
    #5 Install 'process32' using:
                            sudo pip install "subprocess32>=3.2.6"
    #6 Run topology using:
                            sudo mn --custom topology.py --topo mytopo

# To Run Program:
    #1 Put all program files in same directory
    #2 Create a subdirectory called files
    #3 Add all pdf files to that directory
    #4 Run: ./topo.sh
    #5 Run: xterm h1 h2 h3
    #6 On h1 run: ./server.py
    #7 On h2 run: ./controller.py
    #8 On h3 run: ./client.py
