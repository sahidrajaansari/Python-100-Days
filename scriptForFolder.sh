#!/bin/bash

# Loop to create Day-1 to Day-5 folders
for day in {1..100}
do
    # Create the Day-X folder
    folder_name="Day-$day"
    mkdir -p $folder_name

    # Create the main.py file inside the Day-X folder
    touch "$folder_name/main.py"

    # Create the Project folder inside the Day-X folder
    mkdir -p "$folder_name/Project"

    echo "Created $folder_name with main.py and Project folder"
done
