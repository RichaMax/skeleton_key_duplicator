# Skeleton key duplicator for Tiny tina's Wonderlands
 
Small python script to duplicate Skeleton key in Tiny Tina's Wonderlands.

# Requirement

You need to have entered at least on shift code (in game or online) to obtain a skeleton key **(DO NOT TAKE THE KEY)**.

# Usage

:warning: **Please read the instructions carefully before launching the bot!** :warning:

Two options are available:

### From source 
1. Clone the repository
    ```
    $>git clone https://github.com/RichaMax/skeleton_key_duplicator.git
    ```
2. Install the libraries specified in `requirements.txt` files.
    ```
    $>python -m pip install -r requirements.txt
    ```
3. The `settings.json` file contains the arguments necessary to launch the bot.

The default parameters are the following:
   ```json
   {
    "nbr_keys": 10,
    "multiplicator": 1.0
   }
   ```

### Using executable

Just download the executable available here.

### Steps
:point_right: When you have set up one of the two solutions, follow these steps:

 1. Check that you have access to internet
 2. Launch the game and start your game (Game -> Continue) 
 3. Once you're in game, go to the mail tab in the social menu and check that you have at least on skeleton key available
 4. Disconnect from internet
 5. Go back to the game and exit to main menu
 6. Check that you are indeed disconnected from the internet (a wifi symbol with a red X should be present below you caracter name if it is the case)
 7. Start the bot  
  7.1. Script solution:  
    ```python
    $>python main.py
    ```  
    7.2 Executable solution:  
        Double click on the executable and press 'Launch' in the GUI (you can modify the default parameters as you pleased)  
 8. Go back to the game and press `m`
 9. Enjoy!

You can pause the bot at any time by pressing `m` again, it will finish the current loop and stay idle. If you repress `m` it will resume his execution. 

# How it works

The script automatize the actions necessary to retrieve the skelton(s) key(s) in the email tab of the social panel and leave the game to main menu. It repeat the loop until it have acquired the desired number of keys.

# Donation
### Monero
If you enjoy this bot consider donating: 88srv6fkc1FXPZg3xvirxpNsQ34ofocvWVfbSxCQJQre88efyDvT3ZFDLifmqUz1bke4BgKD26zDWPrKgVzWFZP36Eybp25
