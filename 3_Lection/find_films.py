from films import film_list
titles = []

# print(film_list[0])

for film in film_list:
    if film['rating'] > 8.9:
        titles.append(film['title'])
# print(titles)

for index, title in enumerate(titles):
    print(f"{index+1}.{title}")

print('Hello')
