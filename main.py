def text_to_html(firFile, secFile, outFile):
    import difflib, re

    ft = open(firFile, 'r').readlines()
    sd = open(secFile, 'r').readlines()

    diff = difflib.HtmlDiff().make_file(ft, sd, first_file, second_file)
    tbody = diff[diff.find('<tbody>')+len('<tbody>'):diff.find('</tbody>')]
    tbody_list = tbody.split("\n")

    for line in tbody_list[1:-1]:
        if 'diff_add' not in line:
            if 'diff_chg' not in line:
                if ('diff_sub') not in line:
                    tbody_list.remove(line)

    n=1
    for line in tbody_list[1:-1]:
        no1 = re.search('id="from(\d*)_(\d*)">(\d*)<', line).group(1)
        no2 = re.search('id="from(\d*)_(\d*)">(\d*)<', line).group(2)
        line = line.replace('id="from'+str(no1)+'_'+str(no2)+'">'+str(no2)+'<', 'id="from'+str(no1)+'_'+str(n)+'">'+str(n)+'<', 1)
        tbody_list[n] = line.replace('id="from'+str(no1)+'_'+str(no2)+'">'+str(no2)+'<', 'id="from'+str(no1)+'_'+str(n)+'">'+str(n)+'<', 1)
        n+=1
  
    tbody = '\n'.join(tbody_list)
    diff_split = diff.split('</tbody>')
    diff_split_2 = diff_split[0].split('<tbody>')
    diff = diff_split_2[0]+tbody+'</tbody>'+diff_split[1]

    with open(outFile, 'w') as f:
        f.write(diff)

def pdf_to_text(path, file):
    import PyPDF2
    pdfreader = PyPDF2.PdfFileReader(path+file)
    x = pdfreader.numPages
    for a in range(x):
        pageobj = pdfreader.getPage(a)
        text = pageobj.extractText()
        file1 = open(path + str(a) + '.txt', 'w')
        file1.writelines(text)
        file1.close()

def get_parameter():
    from sys import argv
    return argv
    #for num in range(1, len(argv)):
    #    print("parameter %d is %s "%(num, argv[num]))

if __name__ == "__main__":
    get_parameter()
    #pdf_to_text('/users/chinchuankuo/documents/python/different_report/', 'first.pdf')