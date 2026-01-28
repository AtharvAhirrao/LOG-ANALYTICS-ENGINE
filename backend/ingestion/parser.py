import re

def parse_log_line(line):
    log_pattern = r'^(?P<timestamp>\S+ \S+)  (?P<level>\S+)  (?P<services>\S+)  (?P<message>.*)$'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()
    else:
        return None
    
# r '' -> raw data
# ?P<> -> name group
# #s+ -> for spaces one or more
#^ -> start of line
#$ -> end of line
# \S -> non space character
    
