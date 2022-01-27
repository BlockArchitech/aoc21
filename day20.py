import numpy as np
from time import perf_counter

def scanner_enhance(file_path, max_run):

    with open(file_path) as fin:
        algo, image = fin.read().strip().split('\n\n')

    algo_b = {}

    for i, val in enumerate(algo):
        if val == '#':
            algo_b[i] = 1
        else:
            algo_b[i] = 0

    image = image.split('\n')
    image_b = np.zeros((len(image), len(image[0])), dtype=int)

    for i, row in enumerate(image):
        for j, val in enumerate(row):
            if val == '#':
                image_b[i,j] = 1
            else:
                image_b[i,j] = 0

    run = 1

    while run <= max_run:
        if algo_b[1] == 1 and not run % 2:
            image_pad = np.ones((image_b.shape[0] + 4,
                                 image_b.shape[1] + 4),
                                dtype=int)
        else:
            image_pad = np.zeros((image_b.shape[0] + 4,
                                  image_b.shape[1] + 4),
                                 dtype=int)

        image_pad[2:-2,2:-2] = image_b

        e_image = np.zeros((image_b.shape[0] + 2,
                            image_b.shape[1] + 2),
                           dtype=int)

        for loc, val in np.ndenumerate(image_pad):
            x, y = loc
            if (x in range(1, len(image_pad) - 1)
                and y in range(1, len(image_pad) - 1)):
                sub_pix = image_pad[x-1:x+2, y-1:y+2]
                pix_str = ''
                for row in sub_pix:
                    for s_val in row:
                        pix_str += str(s_val)

                e_image[x-1, y-1] = algo_b[int(pix_str, 2)]

        image_b = e_image.copy()
        run += 1

    return np.count_nonzero(image_b)

def main():

    assert scanner_enhance('input.txt', 2)
    print(scanner_enhance('input.txt', 2))

    assert scanner_enhance('input.txt', 50)
    start = perf_counter()
    print(scanner_enhance('input.txt', 50), perf_counter() - start)

if __name__ == '__main__':
    main()
