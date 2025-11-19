from astropy.table import Table

# column format per https://www.astro.gsu.edu/wds/Webtextfiles/wdsweb_format.txt

# parse the file and return an array of rows
def parse_file(filename, columns, header_lines):
   with open(filename, "r") as file:
      line_num = 0
      rows = []
      #read the file line by line
      for line in file:
         line_num += 1
         #skip the header
         if line_num <= header_lines: 
            continue

         row = parse_line(line_num, line, columns)
         rows.append(row)
      
      # load data into an astropy table
      table = Table(rows=rows)

      return table

# parse a line and return a dictionary of fields
def parse_line(line_num, line, columns):
   row = {}
   for column in columns:
      (start,end,format,key) = column
      if end<=len(line):
         data_str = line[start-1:end]
         data = parse_field(line_num, data_str, format)
         row[key]=data

   return row

# parse the string field data with the given format
def parse_field(line_num, data_str, format):
   data_str = data_str.rstrip()
   # empty strings stay empty strings
   match(format):
      case 's':
         return data_str
      # conversion errors produce NaN
      case 'i':
         try:
            return int(data_str)
         except Exception as e:
            return float('nan')
      case 'f':
         try:
            return float(data_str)
         except Exception as e:
            return float('nan')

      # unknown formats are empty strings
      case _:
         return ""
         
