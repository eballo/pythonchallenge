# http://www.pythonchallenge.com/pc/def/channel.html
#
# There is a hint that says <-- zip in the source code
# http://www.pythonchallenge.com/pc/def/channel.zip
# Downolad the file exract the content and there is a readme
#
import re
import zipfile

# path = '/Users/eballo/work/python/pythonchallange/06/'
zip_file = 'channel.zip'
the_zip = zipfile.ZipFile(zip_file)

comments = []

nothing = 90052
pattern = "[^and the next nothing is]([0-9]+)"
while True:
    text = the_zip.read(str(nothing) + '.txt').decode()
    match = re.search(pattern, text)
    if match:
        print(match.group(0))
        comment = the_zip.getinfo(str(nothing) + ".txt").comment.decode()
        print(comment)
        comments.append(comment)
        nothing = match.group(0)
    else:
        break
print(text)
print(comments)

result = "".join(message for message in comments)
print(result)

#  http://www.pythonchallenge.com/pc/def/hockey.html
#  it's in the air. look at the letters.
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

# each letter is using a different letter: oxygen

