"""
Backups up home-assistant and related configurations.

This WILL backup sensitive information that is NOT suitable for commits to GH!

Module Attributes:


(C) Copyright 2020 JC.  All Rights Reserved Worldwide.
"""
import configparser
import os
import os.path
import zipfile



def load_config_data():
    """Loads data from config file.

    Returns:
      dst_root_folder (str): Root destination folder for backups.  This dir
        MUST already exist -- it will NOT be created here to avoid mistakes
        causing possible multiple folders being generated.
    """
    cp = configparser.ConfigParser()
    cp.read('backup.conf')

    dst_root_folder = cp['backup']['destination']

    return dst_root_folder


def build_backup_zip_name():
    """Builds the backup zip file name (no dirs).

    Returns:
      zip_name (str): The name of the zip file to use for this backup.
    """
    # TEMP: Hardcoding name for a hot sec...
    zip_name = 'test.zip'
    return zip_name


def is_excluded(path_to_check):
    """Checks if a path is meant to be excluded.

    These exclusions are relative to the home-assistant root.

    Args:
      path_to_check (str/os.path): The dir or file path to check.  Must be
        relative to home-assistant root.

    Returns:
      (bool): True if excluded; False if not.
    """
    exclusions = [
            '.git',
    ]
    for exclusion in exclusions:
        if os.path.commonprefix([path_to_check, exclusion]) == exclusion:
            return True
    return False


def zip_and_save(zip_filepath):
    """Creates a zip file, saves to the specified location.

    Skips all files and directories listed in the exlcusions list.  Includes
    all files and empty directories otherwise.

    Args:
      zip_filepath: The full path and filename of the zip file.
    """
    src_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    zip_file = zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED)

    for current_dir, sub_dirs, files in os.walk(src_dir):
        cur_rel_dir = os.path.relpath(current_dir, src_dir)

        for file in files:
            full_filepath = os.path.join(current_dir, file)
            rel_filepath = os.path.join(cur_rel_dir, file)
            if not is_excluded(rel_filepath):
                zip_file.write(full_filepath, rel_filepath)

        if not files and not sub_dirs:
            if not is_excluded(cur_rel_dir):
                zip_file.write(current_dir, cur_rel_dir)

    zip_file.close()



def main():
    """Main entry point."""
    dst_root_folder = load_config_data()

    dst_folder = os.path.join(dst_root_folder, 'home-assistant-backups')
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)

    zip_filepath = os.path.join(dst_folder, build_backup_zip_name())
    zip_and_save(zip_filepath)
    print('Done!')



if __name__ == '__main__':
    """Execute only when script executed directly, not when imported.

    This is intended to be the main entry point.
    """
    main()
