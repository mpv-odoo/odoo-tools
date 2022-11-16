# Usage

## Odoo Switch (odoo-switch.sh)
This script allows you to switch across different version of Odoo globally in 1 command. You can just call `source odoo-switch`

 ## Odoo Run (odoo-run.sh)
 This script allows you to run the odoo command globally and forwards any arguments you call it with to odoo. For example, you can just call `odoo -i base` rather than `/Users/martin/Documents/Work/Source/odoo/odoo-bin -i base`

## Odoo Conf (odoo-conf.sh)
This script will create a odoo.conf file in your current directory and add your current directory to odoo's addons path. 

 # Installation

## Pyenv
 - Install pyenv and create a virtual environment for each version of Odoo you want to run. 
   - Name them the integer of the version. E.g: `14`, `15`, `16`

## Setting Environment Variable
I use [zsh](https://ohmyz.sh/) (highly recommended for any terminal), so the steps might differ slightly if you use bash. Add an environment variable named `ODOO_SRC` for the location of your Odoo repos. It is used in both `odoo-switch.sh` and `odoo-run.sh` It assumes the following directory structure:
  .
  ├── odoo #odoo source code
  ├──enterprise #enterprise source code
  └──odoo-sample.conf #can copy from tools/odoo-sample.conf

```console
echo "
export ODOO_SRC=/odoo/root/directory
" >> ~/.zshrc.
```
> **_NOTE:_** If you are using bash, change `~/.zshrc` to `~/.bashrc`


## Adding to Global Bin
To be able to get these scripts running from any directory, you need to add them to your computer's bin directory. I would recommend adding them to `/usr/local/bin/` as this is for programs that are not managed by a distribution package.

I create a symlink instead of copying the files over. A symlink is just a shortcut to the file, so any change I make to the files in my current directory will change the behavior of my global versions.

Run the following script to symlink the files to the bin directory:
`ln -s $(pwd)/tools/odoo-switch.sh /usr/local/bin/odoo-switch`
`ln -s $(pwd)/tools/odoo-run.sh /usr/local/bin/odoo`

Now if you `ls` into /usr/local/bin, you should see both `odoo-switch` and `odoo`. Restart your terminal, and you should be able to call `odoo-switch` and `odoo` and have these 2 scripts run.

> **_IMPORTANT: _**, odoo-switch must be ran with `source` in front of it. This is to allow the script to run in the current shell so Pyenv keeps the newly switched virtual environment when the execution finishes. For ease of use, I also created a function called swodoo (switch odoo) in my .zshrc file that called odoo-switch with source. This way you don't need to call `source odoo-switch` and can just call `odoo-switch` directly. Run the following command if you want to do the same:
```console
echo "
function swodoo() {
    source odoo-switch $1
}
" >> ~/.zshrc
```
> **_NOTE:_** If you are using bash, change `~/.zshrc` to `~/.bashrc`


# Suggestions
If you notice anything is incorrect in the instructions, ***please*** correct it in the form of a PR. If you have any ideas for any other useful tools feel free to suggest them or even create them and make a PR. 


# TODO
- Make way to check version being valid more comprehensive in odoo-switch.sh