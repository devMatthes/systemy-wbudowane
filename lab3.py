import re

dictionary = {}

text = """From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com"""

sender = r"From:\s*(.*)"
mailClient = r"User-Agent:\s*(.*)"
mime = r"MIME-Version:\s*(.*)"
receiver = r"To:\s*(.*)"

allSenders = re.findall(sender, text)
allMailClients = re.findall(mailClient, text)
allMimes = re.findall(mime, text)
allReceivers = re.findall(receiver, text)

dictionary["From"] = allSenders
dictionary["User-Agent"] = allMailClients
dictionary["Mime-Version"] = allMimes
dictionary["To"] = allReceivers


for key, value in dictionary.items():
    print(key, " : ", value)