"""
Backups up home-assistant and related configurations.

This WILL backup sensitive information that is NOT suitable for commits to GH!

Module Attributes:


(C) Copyright 2020 JC.  All Rights Reserved Worldwide.
"""
import configparser



def load_config_data():
    """Loads data from config file.

    Returns:
      dst_root_folder (str): Root destination folder for backups.
    """
    cp = configparser.ConfigParser()
    cp.read('backup.conf')

    dst_root_folder = cp['backup']['destination']

    return dst_root_folder



def main():
    """Main entry point."""
    dst_root_folder = load_config_data()



if __name__ == '__main__':
    """Execute only when script executed directly, not when imported.

    This is intended to be the main entry point.
    """
    main()
