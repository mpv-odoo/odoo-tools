

# TODO
- Need some sort of global setting to keep track of all containers
  - So we can have a prune command as well
- Figure out how to add a git to the addons folder
- add a pgadmin or some other db monitor
- Add commands to start/stop/restart
- Add physical volumes for database
- Scan current directory for nearest project settings.json
- open chrome after docker start?
- link enterprise addons somehow
- create symlink with odoo 
  - Switch the version to be correct




# General
 - Global Settings
   - username
   - password
   - enterprise addons
     - Switch
 - Project Settings
   - Project randomly generated name
   - odoo version
   - odoo port


# Docker Commands
 - Start
 - Stop
 - Restart
 - logs
 - update module
  

# Command Structure
 - ./odoo-tools init <version> <folder>
   - Creates addons, config, & data folder
   - 
 - ./odoo-tools start/stop/restart