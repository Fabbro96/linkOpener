import webbrowser

i = 0
file = open(r'C:\Users\Kerah\Desktop\links.txt', 'r')
stringhe = ''
for x in file:
    i = x.rfind(' ')
    stringhe += x[:i]
    stringhe += "\n"

scrivi = open(r'C:\Users\Kerah\Desktop\links.txt', 'w')
scrivi.write(stringhe)
scrivi.close()
file.close()

links = open(r'C:\Users\Kerah\Desktop\links.txt', 'r')
for x in links:
    print("Link: ", x)
    pth = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth))
    chrome = webbrowser.get('chrome')
    chrome.open(x)
