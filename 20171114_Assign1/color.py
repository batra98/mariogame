colors = {
    'Black'            : '\x1b[1;30m',
    'Blue'             : '\x1b[1;94m',
    'Green'            : '\x1b[1;92m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m'
}

def getcolor(charac):

    if charac=="m":
        color="Light Red"
    elif charac in ["#"]:
        color="Brown"
    elif charac=="-":
        color="Blue"
    elif charac==")":
        color="Light Blue"
    elif charac=="(":
        color="Light Blue"
    elif charac in ["$"]:
        color="Purple"
    elif charac=="e":
        color="Yellow"
    elif charac=="&":
        color="Red"
    elif charac=="M":
        color="White"
    elif charac=="S":
        color="Yellow"
    elif charac==".":
        color="Purple"
    elif charac=="*":
        color="White"

    else:
        color="Yellow"

    return(colors[color]+charac+'\x1b[0m')