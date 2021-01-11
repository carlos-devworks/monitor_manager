# monitor_manager
A Python module that retrieves and changes the brightness of your monitor. Supports Windows and most distributions of Linux.

# Installation
#### Pip:
* Open a terminal and run `pip3 install monitor_manager`

#### Github:
* Clone/download the repository by running `git clone https://github.com/carlos-devworks/monitor_manager`
* Enter the folder it was cloned into with `cd monitor_manager`
* Install using `pip3 install .`

#### Note:
For running on Linux you will need to install one of these programs: `xrandr`, `ddcutil`, or `xbacklight`.
If you are using a desktop computer with proper monitors, install `ddcutil`. If you're using a laptop, try `xrandr` or `xbacklight`.

* Arch: `sudo pacman -S xorg-xrandr` or `sudo pacman -S ddcutil` or `sudo pacman -S light-git` or `sudo pacman -S xorg-xbacklight`
* Debian/Ubuntu: `sudo apt install x11-xserver-utils` or `sudo apt install ddcutil` or `sudo apt install light` or `sudo apt install xbacklight`
* Fedora: `sudo dnf install libXrandr` or `sudo dnf install light` or `sudo dnf install xbacklight`

# Usage
You can call this module from your command line or use it as a python library.

```
python -m monitor_manager --help
> usage: monitor_manager [-h] [-d DISPLAY] [-s SET] [-g] [-f FADE] [-v]
>
> optional arguments:
>   -h, --help            show this help message and exit
>   -d DISPLAY, --display DISPLAY
>                         the display to be used
>   -s SET, --set SET     set the brightness to this value
>   -g, --get             get the current screen brightness
>   -f FADE, --fade FADE  fade the brightness to this value
>   -m METHOD, --method METHOD
>                         specify which method to use
>   -l, --list            list all monitors
>   -v, --verbose         any error messages will be more detailed
>   -V, --version         print the current version
python -m monitor_manager -g
> 100
python -m monitor_manager -s 50
```

### ScreenBrightnessError(`Exception`)
A generic error class designed to make catching errors under one umbrella easy. Raised when the brightness cannot be set/retrieved.

**Usage:**
```python
import monitor_manager as sbc

try:
    sbc.set_brightness(50)
except sbc.ScreenBrightnessError as error:
    print(error)
```

### get_brightness(`verbose_error=False, **kwargs`)
**Summary:**
Returns the current screen brightness as a percentage by default. It may return a list of values if you have multiple, brightness adjustable monitors.
Raises `ScreenBrightnessError` upon failure

**Arguments:**

* `verbose_error` - a boolean value to control how much detail any error messages should contain
* `kwargs` - passed to the OS relevant brightness method

**Usage:**
```python
import monitor_manager as sbc

#get the current screen brightness (for all detected displays)
all_screens_brightness = sbc.get_brightness()
#get the brightness of the primary display
primary_display_brightness = sbc.get_brightness(display=0)
#get the brightness of the secondary display (if connected)
secondary_display_brightness = sbc.get_brightness(display=1)
```

### set_brightness(`value, force=False, verbose_error=False, **kwargs`)
**Summary:**
Sets the brightness to `value`. If `value` is a string and contains "+" or "-" then that value is added to/subtracted from the current brightness.
Raises `ScreenBrightnessError` upon failure

**Arguments:**

* `value` - the level to set the brightness to. Can either be an integer or a string.
* `force` (Linux only) - if set to `False` then the brightness is never set to less than 1 because on Linux this often turns the screen off. If set to `True` then it will bypass this check
* `verbose_error` - a boolean value to control how much detail any error messages should contain
* `kwargs` - passed to the OS relevant brightness method

**Usage:**
```python
import monitor_manager as sbc

#set brightness to 50%
sbc.set_brightness(50)

#set brightness to 0%
sbc.set_brightness(0, force=True)

#increase brightness by 25%
sbc.set_brightness('+25')

#decrease brightness by 30%
sbc.set_brightness('-30')

#set the brightness of display 0 to 50%
sbc.set_brightness(50, display=0)
```

### fade_brightness(`finish, start=None, interval=0.01, increment=1, blocking=True, **kwargs`)
**Summary:**
Fades the brightness from `start` to `finish` in steps of `increment`, pausing for `interval` seconds between each step.
If it runs in the main thread it will return the final brightness upon success, `ScreenBrightnessError` upon failure. Otherwise it returns the list of thread objects that the process is running in

**Arguments:**

* `finish` - The brightness value to fade to
* `start` - The value to start from. If not specified it defaults to the current brightness
* `interval` - The time interval between each step in brightness
* `increment` - The amount to change the brightness by each step in percent.
* `blocking` - If set to `False` it fades the brightness in a new thread
* `kwargs` - passed to `set_brightness`

**Usage:**
```python
import monitor_manager as sbc

#fade brightness from the current brightness to 50%
sbc.fade_brightness(50)

#fade the brightness from 25% to 75%
sbc.fade_brightness(75, start=25)

#fade the brightness from the current value to 100% in steps of 10%
sbc.fade_brightness(100, increment=10)

#fade the brightness from 100% to 90% with time intervals of 0.1 seconds
sbc.fade_brightness(90, start=100, interval=0.1)

#fade the brightness to 100% in a new thread
sbc.fade_brightness(100, blocking=False)
```

## License
This software is licensed under the [MIT license](https://mit-license.org/)

