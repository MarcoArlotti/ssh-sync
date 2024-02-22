
libro = {
    "title": "come non programmare in python",
    "author": "me medesimo",
    "year_published": "2020",
}
libro["genre"] = "istructive"
libro["genre"] = "2021"
libro.pop("year_published")

print(libro.keys())
print(libro.values())
print(libro.items())