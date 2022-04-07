# Skeleton key duplicator for Tiny tina's Wonderlands
 
Small python script to duplicate Skeleton key in Tiny Tina's Wonderlands.

**Disclamer**:

# Requirement

You need to have entered at least on shift code (in game or online) to obtain a skeleton key **(DO NOT TAKE THE KEY)**.

# Usage

:warning: **Please read the instruction carefully before launching the bot!** :warning:

First you need to have the bot on your computer, for that we offer two solutions, either using the **source code** or the compiled **executable**. Then, when you have set up one of the two solutions, follow these steps:

 1. Check that you have access to internet
 2. Launch the game and start your game (Game -> Continue) 
 3. Once you're in game, go to the mail tab in the social menu and check that you have at least on skeleton key available
 4. Disconnect from internet
 5. Go back to the game and exit to main menu
 6. Check that you are indeed disconnected from the internet (a wifi simbol with a red X should be present below you caracter name if it is the case)
 7. Start the bot  
  7.1. Script solution:  
    ```python
    $>python main.py settings.json
    ```  
    7.2 Executable solution:  
      Double click on the executable and press 'Launch' in the GUI (you can modify the default parameters as you pleased)  
 8. Go back to the game and press `m`
 9. Enjoy!

## From source 
1. Clone the repository on your computer
2. Install the libraries specified in `requirements.txt` files.
    ```python
    $> python -m pip install -r requirements.txt
    ```
3. The `settings.json` file contains the arguments to launch the bot the default parameters are the following:
   ```json
   ```

## Using executable

Just download the executable available here, and follow the steps above.

# How it works

The script automatize the actions necessary to retrieve the skelton(s) key(s) in the email tab of the social panel.

# Donation

If you enjoy this bot consider donating: 
