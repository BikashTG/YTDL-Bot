class bcolors: #COLORS CLASS FOR COLOR CODING PRINT LOGS
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class replies: #TEXT FOR REPLIES
    HELP = ('/start: Display welcome message!\n'+
	       '/help: Display all commands available with descriptions\n' +
           '/errors: Display info about the errors that can happen\n')
    HOW_TO = ('Just send a URL to the bot and select a download option, no commands, just a message π\n' +
              'The bot will take care of the rest π¨π»βπ§')
    NEW_WAY = 'There is a new way to download!! Check it out β¬οΈ'
    WELCOME = ('Hi!! ππ»\n' +
               'Welcome to the Social Downloader π¨π»βπ§β¬οΈ bot, made by @galisteo02 βοΈπ»')
    ERRORS = ('π¨ No URL given π¨: You haven\'t given a URL\n'+
	       'π¨ Invalid URL given π¨: You have given an invalid URL\n' +
	       'π¨ DOWNLOAD ERROR! π¨: Video couldn\'t be downloaded due to an unexpected YTDL error, try again later. '
           'Remember itΒ΄s not possible to download Instagram videos\n' +
           'π¨ EXCEPTION ERROR π¨: Exception raised in code (contact @galisteo02 so it can get fixed)')
    URL_ERROR = 'π¨ No URL given π¨'
    SUPP_ERROR = 'π¨ Invalid URL given π¨'
    OTW = 'On the way! ππ»'
    DOWNLOADING = 'β¬οΈ Downloading β¬οΈ'
    SND_AUDIO = 'β¬οΈ Sending audio β¬οΈ'
    SND_VIDEO = 'β¬οΈ Sending video β¬οΈ'
    CHK_FILE_SIZE = 'Checking File Size π§'
    FILE_TOO_BIG = 'File too big! π'
    GET_DWLINK = 'Getting Download Link...π'
    DONE = 'β Done β'
    DWN_ERROR = 'π¨ DOWNLOAD ERROR! π¨'
    EXC_ERROR = 'π¨ EXCEPTION ERROR! π¨'
    TIKTOK_ERROR = 'π¨ TikTok is no longer supported π π¨'
