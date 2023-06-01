import numpy as np

if __name__ == '__main__':
    shark_names = ['Gil', 'Shay', 'Odded']
    x1 = [idx + 0.5 for idx, _ in enumerate(shark_names, start=1)]
    x2 = np.arange(1, len(shark_names), 0.5)
    print()
