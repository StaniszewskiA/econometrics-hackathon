from data import Data

def main():
    my_root = "./Dane"
    my_filename = "dane_close.csv"

    print(Data.read_csv_from_root(my_root, my_filename))

if __name__ == '__main__':
    main()