import asyncio
import multiprocessing as mp
import yaml
import random
from typing import List

MATRIX1_FILE = "./data/matrix1.yml"
MATRIX2_FILE = "./data/matrix2.yml"
RESULT_FILE = "./data/result.yml"

async def matrix_generator(n: int, m: int, queue: mp.Queue):
    """Асинхронная генерация матрицы"""
    matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]
    queue.put(matrix)

async def matrix_multiplier(matrix1: List[List[int]], matrix2: List[List[int]], queue: mp.Queue):
    """Асинхронное перемножение матриц"""
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
    queue.put(result)

def matrix_writer(matrix: List[List[int]], file_name: str) -> None:
    """Записывает матрицу в указанный файл"""
    with open(file_name, "w") as file:
        yaml.safe_dump(matrix, file)

def main():
    n, m = int(input("Введите кол-во строк в матрице -> ")), int(input("Введите кол-во столбцов в матрице -> "))

    matrix_queue = mp.Queue()
    asyncio.run(matrix_generator(n, m, matrix_queue))  # Генерируем первую матрицу
    matrix1 = matrix_queue.get()
    asyncio.run(matrix_generator(m, n, matrix_queue))  # Генерируем вторую матрицу
    matrix2 = matrix_queue.get()

    matrix_writer(matrix1, MATRIX1_FILE)
    matrix_writer(matrix2, MATRIX2_FILE)

    matrix_queue = mp.Queue()
    asyncio.run(matrix_multiplier(matrix1, matrix2, matrix_queue))  # Перемножаем матрицы
    matrix_result = matrix_queue.get()

    matrix_writer(matrix_result, RESULT_FILE)
    print("Результат перемножения:")
    for row in matrix_result:
        print(row)

if __name__ == "__main__":
    main()
