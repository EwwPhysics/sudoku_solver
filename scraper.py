import requests
from bs4 import BeautifulSoup


def get_puzzle(e='random.html?diff=1'):
    board = []
    if e == 'random.html?diff=1':
        URL = 'https://www.menneske.no/sudoku/eng/random.html?diff=1'
    else:
        URL = f'https://www.menneske.no/sudoku/eng/showpuzzle.html?number={e}'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find_all('tr', class_='grid')

    classes = ['bottomedge', 'bottomright', 'normal', 'rightedge']
    for i, row in enumerate(res):
        boxes = row.find_all('td', class_=lambda x: x in classes)
        add = []
        for box in boxes:
            if (box.text.strip()).isdigit():
                add.append(int(box.text.strip()))
            else:
                add.append(0)
        board.append(add)

    return board
