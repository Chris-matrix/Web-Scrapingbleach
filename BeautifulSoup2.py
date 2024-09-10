yre.findall("ab*c", "abdc")
re.findall("a.*?c", "abc")
re.findall("a.*?c", "abbc")
re.findall("a.*?c", "ac")
re.findall("a.*?c", "acc")
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())
end_index = html.find("<title>")
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<title.*?>.*?</title>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)