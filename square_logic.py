import copy
import itertools
from utils import get_number, get_mask
class LineLogic:

    def __init__(self):
        self.same_links = {k : set() for k in range(11)}
        self.diff_links =  {k : set() for k in range(11)}
        self.is_palindromic = False
        self.black_squares = []
        self.logic_to_check = []

    @staticmethod
    def add_links_static(links,i,j):
        links[i].add(j)
        links[j].add(i)
    def add_link(self, i,j):
        self.add_links_static(self.same_links, i,j)

    def diff_link(self, i,j):
        self.add_links_static(self.diff_links, i,j)
    def add_palindrome_logic(self):
        self.is_palindromic = True

    def add_logic_test_gen(self, fun):
        self.logic_to_check.append(fun)
    def black_logic_destructor(self, black_logic, verbose=False):
        self.black_squares = black_logic
        links_set = [self.diff_links, self.same_links]
        for black_square in black_logic:
            for index_link,links in enumerate(links_set):
                for node,neighbors in links.items():
                    neighbors_to_take_down = []
                    for neighbor in neighbors:
                        if (black_square - node) * (black_square - neighbor)<=0:
                            neighbors_to_take_down.append(neighbor)
                    for neighbor in neighbors_to_take_down:
                        neighbors.remove(neighbor)
                        if verbose and index_link==0 and node<neighbor:
                            print(f"remove same link : {node, neighbor}")
                        if verbose and index_link==1 and node<neighbor:
                            print(f"remove diff link : {node, neighbor}")


    @staticmethod
    def get_palindrome_links(start,stop):
        return list(zip(range(start,stop+1), range(start,stop+1,-1)))


    @staticmethod
    def restrict_links(links, start,stop):
        key_to_pop = []
        for key in links:
            if key>stop:
                key_to_pop.append(key)
        for key in key_to_pop:
            links.pop(key)
        for key,item in links.items():
            stock=[]
            for elt in item:
                if elt<start or elt>stop:
                    stock.append(elt)
            item.difference_update(stock)

    def create_generator(self, start, length):
        stop = start + length-1

        same_links = copy.deepcopy(self.same_links)
        diff_links = copy.deepcopy(self.diff_links)
        for palindrom_link in self.get_palindrome_links(start, stop):
            i,j = palindrom_link
            self.add_links_static(same_links,i,j)


        self.restrict_links(same_links, start,stop)
        self.restrict_links(diff_links, start, stop)
        all_nodes = set()
        generation_L = []
        for i in range(start,stop+1):
            if i in all_nodes:
                continue
            all_nodes.add(i)
            all_nodes = all_nodes.union(same_links[i])
            same_links[i].add(i)
            generation_L.append(same_links[i])
        numbers = [1,2,3,4,5,6,7,8,9]
        dico = get_mask(generation_L)
        mask = [1000]* length
        for key,item in dico.items():
            mask[key-start]=item
        all_numbers = itertools.product(numbers, repeat=len(generation_L))
        def generator():
            for number in all_numbers:
                real_number = [number[index] for index in mask]
                is_stopped = False
                for node,neighbors in diff_links.items():
                    if is_stopped:
                        break
                    for neighbor in neighbors:
                        if real_number[node-start] == real_number[neighbor-start]:
                            is_stopped=True
                            break
                if is_stopped:
                    continue
                nb = get_number(real_number)
                is_stopped=False
                for logic_fun in self.logic_to_check:
                    if not logic_fun(nb):
                        is_stopped=True
                        break
                if is_stopped:
                    continue
                yield nb
        return generator()


def line_8_zones(line_logic: LineLogic):
    line = line_logic
    line.add_link(0,1)
    line.diff_link(1,2)
    line.diff_link(2,3)
    line.diff_link(3,4)
    line.diff_link(4,5)
    line.add_link(5,6)
    line.diff_link(6,7)
    line.add_link(7,8)
    line.diff_link(8,9)
    line.diff_link(9,10)


if __name__ == "__main__":
    line = LineLogic()
    line_8_zones(line)
    gen = line.create_generator(0,3)
    for elt in gen:
        print(elt)