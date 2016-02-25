from ast import literal_eval
import os


def create_directory(d):
    if not os.path.exists(d):
        os.makedirs(d)

with open('solutions.json', 'r') as f:
    jl = literal_eval(f.read())

dir_name = 'solutions'

create_directory(dir_name)

for j in jl:
    s_source = j['s_source']
    lang = j['s_lang']
    lang_dict = {'GNU C'        : 'c'       ,
                 'GNU C11'      : 'c'       ,
                 'GNU C++'      : 'cc'      ,
                 'GNU C++11'    : 'cc'      ,
                 'GNU C++0x'    : 'cc'      ,
                 'MS C++'       : 'cpp'     ,
                 'FPC'          : 'pp'      ,
                 'Delphi'       : 'pas'     ,
                 'Haskell'      : 'hs'      ,
                 'Java 8'       : 'java'    ,
                 'Java 7'       : 'java'    ,
                 'Java 6'       : 'java'    ,
                 'Python 3'     : 'py'      ,
                 'Python 2'     : 'py'      ,
                 'PyPy 3'       : 'py'      ,
                 'PyPy 2'       : 'py'      ,
                 'Perl'         : 'pl'      ,
                 'Ocaml'        : 'ml'      ,
                 'D'            : 'd'       ,
                 'MS C#'        : 'cs'      ,
                 'Mono C#'      : 'cs'      ,
                 'PHP'          : 'php'     ,
                 'JavaScript'   : 'js'      ,
                 'Go'           : 'go'      ,
                 'Ruby'         : 'rb'      ,
                 'Tcl'          : 'tcl'     ,
                 'Io'           : 'io'      ,
                 'Pike'         : 'pike'    ,
                 'Befunge'      : 'bf'      ,
                 'Cobol'        : 'cbl'     ,
                 'Factor'       : 'factor'  ,
                 'Picat'        : 'pi'      ,
                 'Secret_171'   : 'cbl'     ,
                 'Roco'         : 'roco'    ,
                 'Ada'          : 'adb'     ,
                 'FALSE'        : 'false'   ,
                 'Mysterious Language': 'f' ,
                 }
    ext = lang_dict[lang]

    filename = '{}_{}_{}_{}.{}'.format(j['s_pid'], j['s_index'], j[
                                       's_sid'], j['s_lang'], ext)

    print('Generating: ' + filename)

    create_directory('./{}/{}/{}'.format(dir_name, j['s_pid'], j['s_index']))

    with open('./{}/{}/{}/{}'.format(dir_name, j['s_pid'], j['s_index'], filename), 'w') as jf:
        jf.write(s_source)
