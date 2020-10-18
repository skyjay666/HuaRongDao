from cut_image import *
from judge import *
from PIL import Image
from similarity import *
from request import *
import os
import time

start = time.time()
ph = open("test.jpg", "wb")
ph.write(image_data)  # 获取题目图片
ph.close()

start = time.time()
filename = "test.jpg"  # 将题目图片切割并存放到cutmodify文件夹中
image = Image.open(filename)
image_list = Cut_image(image)
save_images("cutmodify/", image_list)

dest = os.walk("D://pythonProject//brother//gallery")

mmax, mname = general(filename, dest)

file_name = 'gallery/' + mname
image = Image.open(file_name)
image_list = Cut_image(image)
save_images("cutorigin/", image_list)

savearr = []  # 保存题目分割成的九张图片在原图的位置
record = []  # 记录原图的每个部分是否被匹配到即判断哪一张图被扣掉
position = -1
target = []

savearr, record, position, target = Judge(savearr, record, position, target)
print("对应原图所在位置：", savearr)
print("目标状态：", target)

print("相似度", mmax, "对应照片", mname)
end = time.time()
print("所耗时间:", (end - start))

list_savearr=[str(i) for i in savearr]
list_target=[str(i) for i in target]

savearr="".join(list_savearr)
target="".join(list_target)


_goal_state = [[2, 2, 3],
               [3, 5, 6],
               [6, 8, 0]]
count=0
for i in range(0,3):
    for j in range(0,3):
        _goal_state[i][j]=int(target[count])
        count=count+1
arr=[]
pos=4
"""帮助函数，对于未找到的seq索引值返回-1"""
def operation(x):#判断操作
    if x==-1:
        return 'a'
    if x==1:
        return 'd'
    if x==-3:
        return 'w'
    if x==3:
        return 's'
    if x==0:
        return '0'
def index(item, seq):
    try:
        return seq.index(item)
    except:
        return -1


class EightPuzzle:

    def __init__(self):
        # 搜索值
        self._hval = 0
        # 当前实例的搜索深度
        self._depth = 0
        # 搜索路径中的父节点
        self._parent = None
        self.adj_matrix = []
        for i in range(3):
            self.adj_matrix.append(_goal_state[i][:])

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        else:
            return self.adj_matrix == other.adj_matrix

    def __str__(self):
        res = ''
        for row in range(3):
            res += ' '.join(map(str, self.adj_matrix[row]))
            res += '\r\n'
        return res

    def _clone(self):
        p = EightPuzzle()
        for i in range(3):
            p.adj_matrix[i] = self.adj_matrix[i][:]
        return p

    def _get_legal_moves(self):  # 返回可以交换可用空间的元组列表
        # 获取空块的行和列
        row, col = self.find(0)
        free = []

        # 找出哪些位置可以移动到哪里
        if row > 0:
            free.append((row - 1, col))
        if col > 0:
            free.append((row, col - 1))
        if row < 2:
            free.append((row + 1, col))
        if col < 2:
            free.append((row, col + 1))
        return free
    def _generate_moves(self):
        free = self._get_legal_moves()
        zero = self.find(0)
        def swap_and_clone(a, b):
            p = self._clone()
            p.swap(a, b)
            p._depth = self._depth + 1
            p._parent = self
            return p

        return map(lambda pair: swap_and_clone(zero, pair), free)

    def _generate_solution_path(self, path):
        if self._parent == None:
            return path
        else:
            path.append(self)
            return self._parent._generate_solution_path(path)

    def solve(self, h):  # 执行A*搜索目标状态
        def is_solved(puzzle):
            return puzzle.adj_matrix == _goal_state

        openl = [self]
        closedl = []
        move_count = 0
        while len(openl) > 0:
            x = openl.pop(0)
            move_count += 1
            if (is_solved(x)):
                if len(closedl) > 0:
                    return x._generate_solution_path([]), move_count
                else:
                    return [x]

            succ = x._generate_moves()
            idx_open = idx_closed = -1
            for move in succ:
                # 是否遍历过该节点
                idx_open = index(move, openl)
                idx_closed = index(move, closedl)
                hval = h(move)
                fval = hval + move._depth

                if idx_closed == -1 and idx_open == -1:
                    move._hval = hval
                    openl.append(move)
                elif idx_open > -1:
                    copy = openl[idx_open]
                    if fval < copy._hval + copy._depth:
                        # 将move的值复制到现有的
                        copy._hval = hval
                        copy._parent = move._parent
                        copy._depth = move._depth
                elif idx_closed > -1:
                    copy = closedl[idx_closed]
                    if fval < copy._hval + copy._depth:
                        move._hval = hval
                        closedl.remove(copy)
                        openl.append(move)

            closedl.append(x)
            openl = sorted(openl, key=lambda p: p._hval + p._depth)
        # 如果未找到完成状态，则返回失败
        return [], 0

    def set(self, other):
        i = 0
        for row in range(3):
            for col in range(3):
                self.adj_matrix[row][col] = int(other[i])
                i = i + 1

    def find(self, value):  # 返回图形中指定值的行、列坐标
        if value < 0 or value > 8:
            raise Exception("value out of range")

        for row in range(3):
            for col in range(3):
                if self.adj_matrix[row][col] == value:
                    return row, col

    def peek(self, row, col):  # 返回指定行和列的值
        return self.adj_matrix[row][col]

    def poke(self, row, col, value):  # 设置指定行和列的值
        self.adj_matrix[row][col] = value

    def swap(self, pos_a, pos_b):  # 交换指定坐标处的值
        temp = self.peek(*pos_a)
        self.poke(pos_a[0], pos_a[1], self.peek(*pos_b))
        self.poke(pos_b[0], pos_b[1], temp)


def heur(puzzle, item_total_calc, total_calc):
    t = 0
    for row in range(3):
        for col in range(3):
            val = puzzle.peek(row, col) - 1
            target_col = val % 3
            target_row = val / 3

            # account for 0 as blank
            if target_row < 0:
                target_row = 2

            t += item_total_calc(row, target_row, col, target_col)

    return total_calc(t)


# 用来低估的启发式方法
def h_manhattan(puzzle):
    return heur(puzzle,
                lambda r, tr, c, tc: abs(tr - r) + abs(tc - c),
                lambda t: t)

def main():

    global arr
    p = EightPuzzle()
    begin = EightPuzzle()
    p.set(savearr)  # 设置初始状态
    begin.set(savearr)
#    print(p)
    path, count = p.solve(h_manhattan)
    path.reverse()
    step=0
    for i in path:
        step=step+1
        #print(i)
        if step==1:
            z=((i.find(0))[0]*3+(i.find(0))[1]+1)-((begin.find(0))[0]*3+(begin.find(0))[1]+1)
            arr=operation(z)
        else:
            z = ((i.find(0))[0]*3+(i.find(0))[1]+1)-((path[step-2].find(0))[0]*3+(path[step-2].find(0))[1]+1)
            arr = arr+operation(z)
#    print("Solved with Manhattan distance exploring", count, "states")
#    print(step)
    print(arr)
# 提交答案的接口
    headers = {'content-type': "application/json"}
    anserurl = "http://47.102.118.1:8089/api/challenge/submit"
    answer = {

        "uuid": uuid,
        "teamid": 44,
        "token": "b305a640-b3a9-4f25-a4fb-befb6b7db9d9",
        "answer": {
            "operations": arr,
            "swap": swap
        }
    }
    print(answer)
    response = requests.request("post", anserurl, headers=headers, json=answer)
    print(response.text)


if __name__ == '__main__':
    main()

