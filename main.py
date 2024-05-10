from data import Data

def main():
    my_root = "./Dane"
    my_filename = "dane_close.csv"

    print(Data(my_root, my_filename).read_csv_from_root().head())

if __name__ == '__main__':
    main()