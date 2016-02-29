import pandas as pd

def merge_stats(input_stats_files, output_merged_file):

    first_file = input_stats_files.pop()

    base = pd.read_csv(first_file, delim_whitespace=True, index_col=0)

    for stats_file_path in input_stats_files:

        stats_file = pd.read_csv(stats_file_path, delim_whitespace=True, index_col=0)
        base = pd.merge(base, stats_file, left_index=True, right_index=True)

    base.to_csv(output_merged_file, sep='\t')

def merge_stats_from_doit(dependencies, targets):

    assert len(targets) == 1
    merge_stats(dependencies, targets[0])
