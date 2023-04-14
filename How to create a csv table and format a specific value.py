import xlsxwriter
data = {
    "Gene":["Bna123","Bna124"],
    "Class":["RLK","RLP"],
    "Size":[100,150]
}
workbook = xlsxwriter.Workbook('Genes_Table.xlsx')
book_format = workbook.add_format(properties={'bold': True, 'font_color': 'red'})
worksheet = workbook.add_worksheet('Gene')
for col_num, header in enumerate(data.keys()):
    worksheet.write(0,col_num, (header))
for row_num,row_data in enumerate(zip(*data.values())):
    for col_num, cell_data in enumerate(row_data):
        if cell_data ==  "RLK":
            worksheet.write(row_num+1, col_num, cell_data, book_format)
        else:
            worksheet.write(row_num+1, col_num, cell_data)
workbook.close()
