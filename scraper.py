import requests
from bs4 import BeautifulSoup

from typing import Optional

def get_puzzle(e: Optional[int]):
    template = 'https://www.menneske.no/sudoku/eng/{}'.format
    if e is None:
        URL = template('random.html?diff=1')
    else:
        URL = template(f'showpuzzle.html?number={e}')

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('tr', class_='grid')

    classes = ['bottomedge', 'bottomright', 'normal', 'rightedge']
    board = []
    for row in rows:
        boxes = row.find_all('td', class_=lambda x: x in classes)
        add = []
        for box in boxes:
            if (box.text.strip()).isdigit():
                add.append(int(box.text.strip()))
            else:
                add.append(0)
        board.append(add)

    return board
