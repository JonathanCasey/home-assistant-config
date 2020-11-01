"""
Backups up home-assistant and related configurations.

This WILL backup sensitive information that is NOT suitable for commits to GH!

Module Attributes:


(C) Copyright 2020 JC.  All Rights Reserved Worldwide.
"""
import configparser
import datetime as dt
import os
import os.path
import subprocess
import zipfile


def get_root_dir():
    """Gets the absolute path to the root dir of this repo.

    Returns:
      (os.path): Absolute path to the repo root dir.
    """
    this_script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.dirname(this_script_dir)


def load_config_data():
    """Loads data from config file.

    Returns:
      dst_root_folder (str): Root destination folder for backups.  This dir
        MUST already exist -- it will NOT be created here to avoid mistakes
        causing possible multiple folders being generated.
    """
    backup_conf_filepath = os.path.join(get_root_dir(),
            'backup', 'backup.conf')

    cp = configparser.ConfigParser()
    cp.read(backup_conf_filepath)

    dst_root_folder = cp['backup']['destination']

    return dst_root_folder


def get_git_branch_code():
    """Gets the git branch and encodes into a code.

    Format is the branch code of `m`aster, `d`evelop, or other `b`ranch.

    Return:
      git_branch_code (str): The current git branch code.
    """
    ps = subprocess.Popen(('git', 'symbolic-ref', 'HEAD'),
            stdout=subprocess.PIPE,
            cwd=get_root_dir())
    git_branch = subprocess.check_output(
            ('sed', '-e', 's/^refs\/heads\///'),
            stdin=ps.stdout).decode("utf-8").strip()

    if git_branch == 'master':
        return 'm'
    elif git_branch == 'develop':
        return 'd'
    return 'b'


def get_git_status_code():
    """Gets the git status and encodes general file states.

    Format is `x-y`, where `x` is the listing of all `X` values from the short
    git status, and `y` is the listing of all `Y` values from the short git
    status.  Each section puts the letters in alphabetical order, and `?` is
    replaced by `u`, and `!` is replaced by `i`.

    Returns:
      git_status_code (str): The git status code summary string.
    """
    git_status = subprocess.check_output(
                ['git', 'status', '--short'],
                cwd=get_root_dir()
            ).decode("utf-8").strip()

    x_codes = set()
    y_codes = set()

    for line in git_status.splitlines():
        x = line[0].replace('?', 'u').replace('!', 'i')
        y = line[1].replace('?', 'u').replace('!', 'i')

        if x and x != ' ':
            x_codes.add(x)

        if y and y != ' ':
            y_codes.add(y)

    x_str = ''.join(sorted(x_codes))
    y_str = ''.join(sorted(y_codes))

    if not x_codes and not y_codes:
        return ''

    return f'{x_str}-{y_str}'


def build_backup_zip_name():
    """Builds the backup zip file name (no dirs).

    Returns:
      zip_name (str): The name of the zip file to use for this backup.
    """
    timestamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    git_hash = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD'],
            cwd=get_root_dir()
            ).decode("utf-8").strip()
    git_branch_code = get_git_branch_code()
    git_status_code = get_git_status_code()

    zip_name = f'ha_backup_{timestamp}_{git_hash}-{git_branch_code}'
    if git_status_code:
        zip_name += f'-{git_status_code}'
    zip_name += '.zip'
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
    src_dir = get_root_dir()
    zip_file = zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED)

    for current_dir, sub_dirs, files in os.walk(src_dir):
        cur_rel_dir = os.path.relpath(current_dir, src_dir)

        for file in files:
            full_filepath = os.path.join(current_dir, file)
            rel_filepath = os.path.join(cur_rel_dir, file)
            if not is_excluded(rel_filepath):
                try:
                    zip_file.write(full_filepath, rel_filepath)
                except FileNotFoundError as ex:
                    # File may have disappeared -- ignore
                    continue

        if not files and not sub_dirs:
            if not is_excluded(cur_rel_dir):
                try:
                    zip_file.write(current_dir, cur_rel_dir)
                except FileNotFoundError as ex:
                    # Dir may have disappeared -- ignore
                    continue

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
