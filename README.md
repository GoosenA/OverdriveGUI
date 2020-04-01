# OverdriveGUI
A simple GUI for the 2020 Entelect Challenge - Overdrive

## Description


## Requirements
The GUI is written in Python3 and requires pygame to run

## Usage
### Setup

The config.json file is used to set important parameters for the GUI.

*"Player" : "A - Snek",  -> This is the name of Player 1 (Also refers to the folder name in the match logs)
*"Opponent" : "B - CoffeeRef", -> This is the name of Player 2 (Also refers to the folder name in the match logs)
*"FolderPrepend" : "match/Round ", -> This refers to the parent directory of the match logs.
*"GlobalState" : "GlobalState.json", -> The name of the gloabl state file in the match logs.
*"game_speed" : 10 -> The speed at which to display each round as frames per second. Higher FPS means faster replay. 


### Run the GUI
Once all the settings have been configured, the GUI can be run using:
```bash
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.