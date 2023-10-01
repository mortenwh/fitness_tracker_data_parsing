from fdt_parsing.parse_tcx import get_dataframes

if __name__ == '__main__':
    
    from sys import argv
    fname = argv[1]  # Path to TCX file to be given as first argument to script
    laps_df, points_df = get_dataframes(fname)
    print('LAPS:')
    print(laps_df)
    print('\nPOINTS:')
    print(points_df)
