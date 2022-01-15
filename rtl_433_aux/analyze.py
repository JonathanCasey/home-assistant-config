#!/usr/bin/env python3
"""
Analyze results from a config file to help identify bit patterns.
"""
import argparse
import configparser



def main(filters):
    """
    """
    cp = configparser.ConfigParser()
    cp.read('analysis_data.ini')

    filter_data(cp, filters)
    add_binary_data(cp)
    print_keys_lens = build_print_keys_lens(cp)

    spacer = '  '

    header_vals = []
    separator_vals = []
    for k, l in print_keys_lens.items():
        header_vals.append(f'{k:{l}}')
        separator_vals.append(f'{"-"*len(k):{l}}')
    print(spacer.join(header_vals))
    print(spacer.join(separator_vals))

    for s in cp.sections():
        msg_vals = []
        for k, l in print_keys_lens.items():
            msg_vals.append(f'{cp.get(s, k):{l}}')
        print(spacer.join(msg_vals))
    
    total_len = sum([l for k, l in print_keys_lens.items()]) \
            + len(spacer) * (len(print_keys_lens) - 1)
    print('_'*total_len)
    
    wildcard_char = '*'
    msg_vals = []
    for k, l in print_keys_lens.items():
        sum_char_vals = []
        for i in range(l):
            chars = []
            for s in cp.sections():
                val = cp.get(s, k)
                if i < len(val):
                    chars.append(val[i])
            if len(chars) == 0:
                sum_char = ' '
            elif len(set(chars)) == 1 and len(chars) == len(cp.sections()):
                sum_char = chars[0]
            else:
                sum_char = wildcard_char
            sum_char_vals.append(sum_char)
        msg_vals.append(''.join(sum_char_vals))
    print(spacer.join(msg_vals))



def build_print_keys_lens(data:configparser.ConfigParser):
    """
    """
    desired_keys = [
        'brand',
        'family',
        'sensor_type',
        'sensor_num',
        'batch',
        'event',
        'hex_data',
        'binary_data',
    ]

    print_keys_lens = dict.fromkeys(desired_keys, 0)
    for key in desired_keys:
        for s in data.sections():
            print_keys_lens[key] = max(print_keys_lens[key],
                    len(data.get(s, key)))
        print_keys_lens[key] = max(print_keys_lens[key], len(key))
    
    return print_keys_lens



def add_binary_data(data:configparser.ConfigParser):
    """
    """
    for s in data.sections():
        data_len = int(data.get(s, 'data_len'))
        binary_data = bin(int(data.get(s, 'hex_data'), 16))[2:].zfill(
                len(data.get(s, 'hex_data')*4))[:data_len]
        data.set(s, 'binary_data', binary_data)



def filter_data(data:configparser.ConfigParser, filters):
    """
    """
    sections_to_remove = set()
    for f_key, f_vals in filters.items():
        if not f_vals:
            continue
        
        for s in data.sections():
            if s in sections_to_remove:
                continue

            if not data.has_option(s, f_key):
                sections_to_remove.add(s)
                continue
            
            if data.get(s, f_key) not in f_vals:
                sections_to_remove.add(s)
                continue
    
    for s in sections_to_remove:
        data.remove_section(s)



if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Process inputs.',
            epilog="Within each argument, the values will be or'd together to"
                + " select results that match any of the provided values.  With"
                + " multiple different arg types, each arg type will be and'd"
                + " together to effectively exclude results that don't contain"
                + " a match from each specified arg.")
    ap.add_argument('--filename', nargs='*')
    ap.add_argument('-t', '--sensor_type', nargs='*')
    ap.add_argument('-n', '--sensor_num', nargs='*')
    ap.add_argument('-b', '--brand', nargs='*')
    ap.add_argument('-f', '--family', nargs='*')
    ap.add_argument('-g', '--batch', nargs='*')
    ap.add_argument('-j', '--jumper_hex_id', nargs='*')
    ap.add_argument('-e', '--event', nargs='*')
    ap.add_argument('-l', '--data_len', nargs='*')
    ap.add_argument('-d', '--hex_data', nargs='*')
    filters = vars(ap.parse_args())
    main(filters)