from tqdm import tqdm
import random


def main():
    with open('result_knock81.txt', 'r', encoding='utf-8') as i_file:
        with open('result_knock82.txt', 'w', encoding='utf-8') as w_file:
            for line in tqdm(i_file):
                words = line.strip().split()
                for i in range(len(words)):
                    d = random.randint(1, 5)
                    left = words[i-d:i]
                    right = words[i+1:i+d+1]
                    print(f'{words[i]}\t{" ".join(left + right)}', file=w_file)


if __name__ == '__main__':
    main()
