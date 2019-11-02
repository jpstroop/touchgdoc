from click import argument
from click import Choice
from click import command
from click import option
from sys import stderr
from touchgdoc import PERMISSIONS_CHOICES
from touchgdoc import TouchGoogleDoc

# TODO: follow this pattern, pulling as mucch from the application class
#   (including configured values) as possible
p_choice = Choice(PERMISSIONS_CHOICES, case_sensitive=False)
p_help = ''
p_default = ''

p_help = ''
p_default = ''


@command()
@option('--group', '-g', default='default_group', help='') # just -a
@option('--account', '-a', default='default_account', help='')
@option('--drive', '-d', default='default_drive', help='')
@option('--folder', '-f', default='default_folder', help='') # root
@option('--permissions', '-p', type=p_choice, default='rw', help='') # rw, co, ro
@option('--title', '-t', default=None, help='')
@argument('list', required=False, default=False) # See: https://click.palletsprojects.com/en/7.x/complex/#the-first-child-command
def touchgdoc_cli(group, account, drive, folder, permissions, title, list):
    """
    Command line application for quickly creating documents in Google Drive.
    """
    pass

if __name__ == '__main__':
    touchgdoc_cli()
