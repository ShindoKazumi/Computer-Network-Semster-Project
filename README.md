# Computer-Network-Semester-Project
This project needs to run in three separate hosts
# Need to install all required packages and run topology. There are two options.
# Option 1: 
    # Download update.sh and topo.sh files
    # On mininet run:
                        ./update.sh
                        ./topo.sh
# Option 2:
    # First update using:
                        sudo apt-get update
    # Install 'pip' by using: 
                        sudo apt-get install python-pip python-dev build-essential
    # Install 'pdftotext' using:
                        sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev
                        sudo pip install pdftotext
    # Install 'getch' using:
                        sudo pip install py-getch
    # Install 'process32' using:
                        sudo pip install "subprocess32>=3.2.6"
    # Run topology using:
                        sudo mn --custom topology.py --topo mytopo
