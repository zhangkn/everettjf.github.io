import glob
import os
import hashlib
import subprocess

os.system("pwd")

# date: 2017-12-20T00:07:54+08:00

for f in glob.glob("_posts/*.md"):
    print(f)

    # filename = f.split('/')[1]
    # dateparts = filename.split('-')
    # if len(dateparts) < 4:
    #     continue
    # datestr = dateparts[0] + "-" + dateparts[1] + "-" + dateparts[2]+"T00:00:01+08:00"
    # print(datestr)

    # d = open(f, 'r').read()

    # titleline = d.split('---')[1].strip().split('\n')[0]

    # idx = d.find('---',4)
    # content = d[idx + 3:] + '\n'

    # with open(f, 'w') as g:
    #     g.write("---\n")
    #     g.write(titleline+"\n")
    #     g.write("date: " + datestr + "\n")
    #     g.write("---\n\n")
    #     g.write(content)
    #     g.write("\n")
    
