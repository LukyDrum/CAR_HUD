# About

This project aims to create a custom Heads-Up display for cars (particulary my car - Mazda 6).

It is made to run on top of RaspbianOS on RPi using Python for the GUI and other functionalities.

To make AndroidAuto functional I had to use the OpenAuto project. I had some trouble getting the OpenAuto to work, but using a fork from [OpenDsh](https://github.com/openDsh) with their installation script that installs all dependencies I finally got it to run.

# Additional requirements

- As mentioned, you need to have OpenAuto installed
- You may need to install Tkinter, Font-noto
```
sudo apt install python3-tk fonts-noto
```

# To-do

- [x] Mockup of the UI with AndroidAuto functionality
- [ ] Show dashboard information (velocity, rpm, ...)
- [ ] Show engine warnings
- [ ] Add more customization options
   - [ ] Colors
   - [ ] Hiding tabs
- [ ] Add swipe controls
- [x] Add Bluetooth connectivity and music streaming
- [ ] Add automatic bluetooth connection
- [ ] Make LED controls functional
- [ ] Add automatic AndroidAuto start on phone connecting
- [ ] Custom installation script
