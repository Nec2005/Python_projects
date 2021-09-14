import sys
import sys

if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    OS.ENVIRON['LC_CTYPE'] = 'en_US.UTF-8'

import awscli.clidriver

def main():
    return awscli.clidriver.main()


if __name__ == '__main__':
    sys.exit(main())