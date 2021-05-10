import csv
import operator
import itertools

row_template = """\
{{0:{sorcery_length}}}{{<1:{location_length}}}{{>2:{MerchantPrice_length}}}"""

with open('/Sorceries_Wisdom_of_a_Sage.csv') as inf:
    reader = csv.reader(inf)
    pre_process, reader = itertools.tee(reader)
    columns = zip(*pre_process)
    col_widths = {k: len(max(col, key=len)) for k,col in zip(
        ['sorcery_length', 'location_length', 'MerchantPrice_length'],
        columns)}
    